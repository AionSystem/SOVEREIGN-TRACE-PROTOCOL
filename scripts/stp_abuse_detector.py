#!/usr/bin/env python3
"""
STP Abuse Detector – Scans new issues for prohibited content.
Runs as a GitHub Action. If flagged, closes and locks the issue.
"""

import os
import re
import json
import sys
from pathlib import Path

# ----------------------------------------------------------------------
# Configuration (can be moved to a config file)
# ----------------------------------------------------------------------
# Prohibited patterns (regex)
PROHIBITED_PATTERNS = [
    r"\b(kill|murder|assassinate|execute|torture|bomb|explosive|weapon)\b.*\b(president|person|people|user|you|them)\b",
    r"\b(rape|sexual assault|pedophile|cp|child porn)\b",
    r"\b(dox|doxxing|address|phone number|ssn|social security)\b.*\b(post|share|reveal)\b",
    r"\b(swat|swatting)\b",
    r"\b(csam|child sexual abuse material)\b",
    r"\b(credential|password|api key|secret key|token)\b.*\b(leak|expose|share)\b",
    r"\b(terrorist|terrorism|islamic state|isis)\b",
    r"\b(suicide|kill myself|self-harm)\b",  # sensitive, but may need handling
]

# External API (optional, requires token)
ENABLE_PERSPECTIVE = os.environ.get("ENABLE_PERSPECTIVE", "false").lower() == "true"
PERSPECTIVE_API_KEY = os.environ.get("PERSPECTIVE_API_KEY")
PERSPECTIVE_THRESHOLD = float(os.environ.get("PERSPECTIVE_THRESHOLD", "0.8"))

ABUSE_LOG_FILE = ".github/abuse_log.json"
BAD_ACTORS_FILE = ".github/bad_actors.yml"


def check_prohibited_patterns(text: str) -> list:
    """Return list of matched patterns."""
    matches = []
    for pattern in PROHIBITED_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            matches.append(pattern)
    return matches


def check_toxicity(text: str) -> float:
    """Call Google Perspective API to get toxicity score (0-1)."""
    if not ENABLE_PERSPECTIVE or not PERSPECTIVE_API_KEY:
        return 0.0
    import requests
    url = "https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze"
    headers = {"Content-Type": "application/json"}
    data = {
        "comment": {"text": text},
        "languages": ["en"],
        "requestedAttributes": {"TOXICITY": {}},
        "clientToken": "stp_abuse_detector",
    }
    params = {"key": PERSPECTIVE_API_KEY}
    try:
        resp = requests.post(url, headers=headers, params=params, json=data, timeout=5)
        if resp.status_code == 200:
            score = resp.json()["attributeScores"]["TOXICITY"]["summaryScore"]["value"]
            return score
    except Exception:
        pass
    return 0.0


def log_abuse(issue_number: int, user: str, matches: list, toxicity: float, reason: str):
    """Append to abuse log."""
    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "issue_number": issue_number,
        "user": user,
        "matches": matches,
        "toxicity_score": toxicity,
        "reason": reason,
        "action": "closed_and_locked"
    }
    # Load existing log
    if os.path.exists(ABUSE_LOG_FILE):
        with open(ABUSE_LOG_FILE, "r") as f:
            log = json.load(f)
    else:
        log = []
    log.append(log_entry)
    with open(ABUSE_LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)


def update_bad_actors(user: str, issue_number: int):
    """Increment violation count for user in YAML file."""
    import yaml
    bad_actors = {}
    if os.path.exists(BAD_ACTORS_FILE):
        with open(BAD_ACTORS_FILE, "r") as f:
            bad_actors = yaml.safe_load(f) or {}
    if user not in bad_actors:
        bad_actors[user] = {"violation_count": 0, "issues": []}
    bad_actors[user]["violation_count"] += 1
    bad_actors[user]["issues"].append(issue_number)
    with open(BAD_ACTORS_FILE, "w") as f:
        yaml.dump(bad_actors, f, default_flow_style=False)


def close_and_lock_issue(issue_number: int, reason: str, matches: list, toxicity: float):
    """Use GitHub API to close and lock the issue."""
    import requests
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    }
    # Close issue
    close_url = f"https://api.github.com/repos/{repo}/issues/{issue_number}"
    close_data = {"state": "closed"}
    requests.patch(close_url, headers=headers, json=close_data)

    # Add comment
    comment_data = {
        "body": f"""## ⚠️ Submission Rejected

This submission was automatically rejected because it contained prohibited content.

**Reason:** {reason}

**Matched patterns:** {', '.join(matches)}

**Toxicity score:** {toxicity:.2f} (threshold {PERSPECTIVE_THRESHOLD})

The issue has been closed and locked. No seal was created.

If you believe this was a false positive, please contact the Architect at `aionsystem@outlook.com`."""
    }
    comments_url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"
    requests.post(comments_url, headers=headers, json=comment_data)

    # Lock issue (prevents further comments)
    lock_url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/lock"
    lock_data = {"lock_reason": "off-topic"}  # or "spam", "resolved"
    requests.put(lock_url, headers=headers, json=lock_data)


def main():
    # Get issue data from GitHub event
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path:
        print("Not running in GitHub Actions context.")
        return
    with open(event_path, "r") as f:
        event = json.load(f)

    action = event.get("action")
    if action != "opened":
        print("Only run on newly opened issues.")
        return

    issue = event.get("issue", {})
    issue_number = issue.get("number")
    user = issue.get("user", {}).get("login")
    title = issue.get("title", "")
    body = issue.get("body", "")
    full_text = f"{title}\n{body}"

    # Check bad actors list for repeat offender
    import yaml
    if os.path.exists(BAD_ACTORS_FILE):
        with open(BAD_ACTORS_FILE, "r") as f:
            bad_actors = yaml.safe_load(f) or {}
        if user in bad_actors and bad_actors[user].get("violation_count", 0) >= 3:
            reason = "Repeat offender with multiple prior violations."
            matches = ["repeat_offender"]
            toxicity = 0.0
            close_and_lock_issue(issue_number, reason, matches, toxicity)
            log_abuse(issue_number, user, matches, toxicity, reason)
            update_bad_actors(user, issue_number)
            sys.exit(0)

    # Run pattern matching
    matches = check_prohibited_patterns(full_text)
    toxicity = 0.0
    if ENABLE_PERSPECTIVE:
        toxicity = check_toxicity(full_text)

    if matches or (ENABLE_PERSPECTIVE and toxicity >= PERSPECTIVE_THRESHOLD):
        reason = "Prohibited content detected."
        if matches:
            reason += f" Matched patterns: {', '.join(matches)}"
        if toxicity >= PERSPECTIVE_THRESHOLD:
            reason += f" Toxicity score {toxicity:.2f} exceeds threshold."
        close_and_lock_issue(issue_number, reason, matches, toxicity)
        log_abuse(issue_number, user, matches, toxicity, reason)
        update_bad_actors(user, issue_number)
        print("Issue rejected and locked.")
    else:
        print("Issue passed abuse check.")


if __name__ == "__main__":
    from datetime import datetime, timezone
    main()
