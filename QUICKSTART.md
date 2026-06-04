# QUICKSTART — Sovereign Trace Protocol

**Seal what is true. Permanently. In under 5 minutes.**

---

## Install

```bash
pip install sovereign-trace
Requires Python 3.11+. No external dependencies. stdlib only.

Verify the Install
bash
python -m sovereign_trace_stamp --test
All 40+ checks must pass. If any fail — stop. Do not use a broken stamp.
A failed test means the stamp is not trustworthy. The test is part of the protocol.

Seal Your First Entry
python
from sovereign_trace_stamp import stamp, display, verify

# Write exactly what is true right now — no narrative, no framing
entry = "Hypothesis: transformer attention is not sufficient for persistent identity. Sealed before any experiment."

# Seal it
ts = stamp(entry)

# Display in all three calendar systems
print(display(ts))
Output:

text
📅 Gregorian:  June 4, 2026
🌑 Hebrew:     18 Sivan 5786
🌀 Dreamspell: Day 2, Solar Moon 10/13
🔒 Seal:       8f3a9c2e7d1b...  (SHA-256, first 12 chars shown)
Note on timestamps: The stamp function records time in UTC.
If you are in a timezone behind UTC, the Gregorian date in your
seal may read as the following day. This is correct behavior —
UTC is the standard. Record your local time separately in your
ledger entry if the distinction matters for your use case.

Verify Integrity
python
# Later — prove the entry was not altered
result = verify(entry, ts)
print(result)  # True — entry unchanged
If verify returns False — the content was changed after sealing.
That is the point of the seal. It catches the change.

The Full Stamp Object
python
import json
from sovereign_trace_stamp import stamp, to_dict

ts = stamp("My sealed observation.")
print(json.dumps(to_dict(ts), indent=2))
json
{
  "gregorian": "June 4, 2026",
  "hebrew": "18 Sivan 5786",
  "dreamspell": "Day 2, Solar Moon 10/13",
  "unix_utc": 1741372800,
  "seal": "8f3a9c2e7d1b4f6a...",
  "version": "FROZEN-4.0"
}
The seal field is the SHA-256 hash of the entry + timestamp.
Store this. It is your proof.

Log an AI Failure
python
from sovereign_trace_stamp import stamp, display

failure = """
MODEL: GPT-4o
PROMPT: Summarize the Q3 earnings call.
OUTPUT: Hallucinated a revenue figure of $4.2B. Actual: $3.1B.
IMPACT: Report sent to board before error caught.
"""

ts = stamp(failure)
print(display(ts))
This is what organizational use looks like. The seal is generated before
remediation begins. The pre-remediation record cannot be altered after the fact.

Running Without pip
If you are not using pip, download sovereign_trace_stamp.py directly from
stamp/sovereign_trace_stamp.py in this repository. It has zero external
dependencies. Drop it into your project and import it directly.

python
import sys
sys.path.insert(0, './stamp')
from sovereign_trace_stamp import stamp, display, verify
What Not To Do
Do not seal vague entries.
"Something important happened today" is not a seal. It is a note.
The seal is only useful if the content is specific enough to be contested.
Seal the exact text. Seal the exact output. Seal the exact claim.

Do not edit after sealing.
The entry you pass to stamp() must be identical to the entry you pass to verify().
One changed character breaks the seal. That is the design.

Do not run a failed test suite in production.
The self-test exists to catch drift in the stamp function.
All 40+ checks. Every deploy. No exceptions.

Next Steps
What you want	Where to go
Understand all use cases	concept/USE-CASES.md
Near-miss reporting for regulated industries	14-near-miss.yml issue template
Submit a sealed trace via GitHub Issues	README.md → Submission Layer
Enterprise certification	CERTIFICATION.md
Audit methodology and epistemic debt framework	AUDIT-METHODOLOGY.md
License terms	LICENSE-EXPLANATION.md
STP Certified Auditor program	AUDITOR-VETTING-PROCESS.md
Full technical spec	concept/SOVEREIGN-TRACE-SPEC.md
*Sovereign Trace Protocol · FROZEN-4.0 · Sheldon K. Salmon — AI Reliability & ADI/AGI Architect · June 2026*
The stamp is permanent. The stamp is the resolution.
