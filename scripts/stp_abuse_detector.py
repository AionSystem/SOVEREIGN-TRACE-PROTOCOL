#!/usr/bin/env python3
"""
STP Tiered Abuse Detector – Green/Yellow/Red scoring.
Green: pass through. Yellow: warn + label, human review. Red: close + lock.
"""

import os
import re
import json
import sys
import base64
from datetime import datetime, timezone
from pathlib import Path

# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------
PROHIBITED_PATTERNS = [
    (r"\b(kill|murder|assassinate|execute|torture|bomb|explosive|weapon)\b.*\b(president|person|people|user|you|them)\b", 1.0),
    (r"\b(rape|sexual assault|pedophile|cp|child porn)\b", 1.0),
    (r"\b(dox|doxxing|address|phone number|ssn|social security)\b.*\b(post|share|reveal)\b", 0.9),
    (r"\b(swat|swatting)\b", 0.9),
    (r"\b(csam|child sexual abuse material)\b", 1.0),
    (r"\b(credential|password|api key|secret key|token)\b.*\b(leak|expose|share)\b", 0.8),
    (r"\b(terrorist|terrorism|islamic state|isis)\b", 0.9),
]

# Thresholds (0–1)
GREEN_THRESHOLD = 0.4   # below this: pass
YELLOW_THRESHOLD = 0.7  # 0.4–0.7: warn + label, no lock
RED_THRESHOLD = 0.7     # above: close + lock

# External API
ENABLE_PERSPECTIVE = os.environ.get("ENABLE_PERSPECTIVE", "false").lower() == "true"
PERSPECTIVE_API_KEY = os.environ.get("PERSPECTIVE_API_KEY")
PERSPECTIVE_THRESHOLD = float(os.environ.get("PERSPECTIVE_THRESHOLD", "0.7"))

ABUSE_LOG_FILE = ".github/abuse_log.json"
BAD_ACTORS_FILE = ".github/bad_actors.yml"

# ----------------------------------------------------------------------
# Helper Functions
# ----------------------------------------------------------------------
def decode_common_encodings(text: str) -> str:
    """Try to decode base64, rot13, etc. Return original if fails."""
    # Base64
    try:
        decoded = base64.b64decode(text).decode('utf-8')
        # If decoded text is readable (low ratio of non-printable), use it
        if sum(c.isprintable() for c in decoded) / len(decoded) > 0.8:
            text += "\n" + decoded
    except:
        pass
    # ROT13
    try:
        import codecs
        rot13 = codecs.decode(text, 'rot_13')
        text += "\n" + rot13
    except:
        pass
    return text


def score_prohibited_patterns(text: str) -> float:
    """Return max score from matched patterns (0–1)."""
    max_score = 0.0
    for pattern, weight in PROHIBITED_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            max_score = max(max_score, weight)
    return max_score


def get_toxicity_score(text: str) -> float:
    """Return Perspective API toxicity score (0–1), or 0 if unavailable."""
    if not ENABLE_PERSPECTIVE or not PERSPECTIVE_API_KEY:
        return 0.0
    import requests
    url = "https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze"
    headers = {"Content-Type": "application/json"}
    data = {
        "comment": {"text": text[:2000]},  # truncate for API
        "languages": ["en"],
        "requestedAttributes": {"TOXICITY": {}},
    }
    params = {"key": PERSPECTIVE_API_KEY}
    try:
        resp = requests.post(url, headers=headers, params=params, json=data, timeout=5)
        if resp.status_code == 200:
            return resp.json()["attributeScores"]["TOXICITY"]["summaryScore"]["value"]
    except Exception:
        pass
    return 0.0


def compute_final_score(text: str) -> float:
    """Combine pattern score and toxicity score (max of both, not average)."""
    decoded = decode_common_encodings(text)
    pattern_score = score_prohibited_patterns(decoded)
    toxicity = get_toxicity_score(decoded)
    return max(pattern_score, toxicity)


def log_abuse(issue_number: int, user: str, score: float, tier: str, reason: str):
    """Append to abuse log."""
    import yaml  # for writing YAML
    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "issue_number": issue_number,
        "user": user,
        "score": score,
        "tier": tier,
        "reason": reason,
    }
    if os.path.exists(ABUSE_LOG_FILE):
        with open(ABUSE_LOG_FILE, "r") as f:
            log = json.load(f)
    else:
        log = []
    log.append(log_entry)
    with open(ABUSE_LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)


def update_bad_actors(user: str, issue_number: int):
    """Increment violation count for user (only for red tier)."""
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


def handle_yellow(issue_number: int, user: str, score: float, reason: str):
    """Add warning comment and label, but do NOT close/lock."""
    import requests
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    # Add label 'needs-review'
    labels_url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/labels"
    labels_data = {"labels": ["needs-review"]}
    requests.post(labels_url, headers=headers, json=labels_data)
    # Add warning comment
    comment_data = {
        "body": f"""## ⚠️ Yellow Alert – Manual Review Required

**Risk score:** {score:.2f} (threshold for yellow: {YELLOW_THRESHOLD})

This submission triggered the abuse detection system but did not reach the red threshold. It has been labeled `needs-review` for human review. **No seal has been created yet.**

**Reason:** {reason}

A maintainer will review this issue shortly. If no violation is found, the seal will proceed normally. If you believe this is an error, please contact the Architect at `aionsystem@outlook.com`.

Thank you for your patience."""
    }
    comments_url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"
    requests.post(comments_url, headers=headers, json=comment_data)
    log_abuse(issue_number, user, score, "YELLOW", reason)


def handle_red(issue_number: int, user: str, score: float, reason: str):
    """Close and lock issue, add comment, log, update bad actors."""
    import requests
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    # Close issue
    close_url = f"https://api.github.com/repos/{repo}/issues/{issue_number}"
    close_data = {"state": "closed"}
    requests.patch(close_url, headers=headers, json=close_data)
    # Add comment
    comment_data = {
        "body": f"""## 🚫 Submission Rejected – Red Alert

**Risk score:** {score:.2f} (threshold for red: {RED_THRESHOLD})

This submission was automatically rejected because it contained prohibited content and exceeded the red threshold.

**Reason:** {reason}

**No seal was created.** The issue has been closed and locked.

If you believe this is a false positive, you may **appeal** by contacting the Architect directly at `aionsystem@outlook.com` with the issue number #{issue_number}. Appeals will be reviewed manually.

Repeat violations will result in a permanent block from submitting to this repository."""
    }
    comments_url = f"https://api.repos/{repo}/issues/{issue_number}/comments"
    requests.post(comments_url, headers=headers, json=comment_data)
    # Lock issue
    lock_url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/lock"
    lock_data = {"lock_reason": "off-topic"}
    requests.put(lock_url, headers=headers, json=lock_data)
    log_abuse(issue_number, user, score, "RED", reason)
    update_bad_actors(user, issue_number)


def check_bad_actors(user: str) -> bool:
    """Return True if user has >=3 red violations."""
    import yaml
    if not os.path.exists(BAD_ACTORS_FILE):
        return False
    with open(BAD_ACTORS_FILE, "r") as f:
        bad_actors = yaml.safe_load(f) or {}
    return bad_actors.get(user, {}).get("violation_count", 0) >= 3


def main():
    # Load GitHub event
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path:
        print("Not in GitHub Actions context. Exiting.")
        return
    with open(event_path, "r") as f:
        event = json.load(f)
    if event.get("action") != "opened":
        print("Only run on newly opened issues.")
        return

    issue = event.get("issue", {})
    issue_number = issue.get("number")
    user = issue.get("user", {}).get("login")
    title = issue.get("title", "")
    body = issue.get("body", "")

    # Concatenate all text from issue (including any additional fields via body)
    # GitHub already provides markdown body; we can also extract from comments? Not needed.
    full_text = f"{title}\n{body}"

    # Check repeat offender first
    if check_bad_actors(user):
        handle_red(issue_number, user, 1.0, "Repeat offender with 3+ prior red violations.")
        return

    # Compute score
    score = compute_final_score(full_text)

    if score < GREEN_THRESHOLD:
        print(f"Green: score {score:.2f}. Passing through.")
        return
    elif score < YELLOW_THRESHOLD:
        handle_yellow(issue_number, user, score, f"Score {score:.2f} exceeded green threshold but below yellow threshold.")
    else:
        handle_red(issue_number, user, score, f"Score {score:.2f} exceeded red threshold.")


if __name__ == "__main__":
    main()
