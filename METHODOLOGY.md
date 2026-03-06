# METHODOLOGY.md — Certification Assessment Methodology

**Sovereign Trace Protocol**
**Author:** Sheldon K. Salmon — AI Reliability & AGI Architect
**Version:** 1.0 — FROZEN at publication
**Date:** March 2026
**Repository:** AionSystem/SOVEREIGN-TRACE-PROTOCOL

---

## PURPOSE

This document specifies the exact methodology used to produce all
certification assessments and audit findings under the Sovereign
Trace Protocol. Every finding issued by the Architect is grounded
in this documented, versioned, falsifiable methodology.

A finding produced under this methodology is a documented factual
assessment — not an opinion, not an editorial judgment, and not
a commercial comparison. It is a structured evaluation of observable,
measurable criteria against a published standard.

Any party disputing a finding has a documented process for doing so.
See Section 6.

---

## SECTION 1 — SCORING STANDARD

**The FROZEN-2.0 Standard**

The Sovereign Trace Protocol FROZEN-2.0 standard defines the
canonical interface and behavioral contract for a compliant
immutable audit ledger. It specifies:

1. The `log()` interface signature — immutable after FROZEN designation
2. The `remediate()` operation — appends only, never modifies original
3. The `query()` operation — read-only, no state mutation
4. The JSONL schema — backwards-compatible across 2.x versions
5. The SHA-256 seal computation — deterministic JSON payload,
   sort_keys=True, compact separators, UTF-8 encoding

A deployment is **compliant** if it implements all five specifications
without modification or substitution. A deployment is **non-compliant**
if any specification is violated, approximated, or bypassed.

**There is no partial compliance.** A seal that computes correctly
on most inputs but fails on Unicode content is non-compliant.
A ledger that appends correctly except for entries marked as
confidential is non-compliant.

---

## SECTION 2 — ASSESSMENT CRITERIA

Each certification assessment evaluates the following criteria:

| Criterion | Code | Assessment Method |
|-----------|------|------------------|
| Schema integrity | C-1 | Direct inspection of JSONL output against FROZEN-2.0 schema |
| Seal computation | C-2 | Verification of SHA-256 seal reproducibility using known test vectors |
| Append-only behavior | C-3 | Attempt to modify a sealed entry — observe behavior |
| Remediation integrity | C-4 | Verify remediation record links correctly and original entry is unchanged |
| Interface compliance | C-5 | Verify `log()`, `remediate()`, `query()` signatures match FROZEN-2.0 |
| Calendar accuracy | C-6 | Verify Gregorian, Hebrew, and Dreamspell outputs against verified anchor cases |

Each criterion is assessed as **PASS**, **FAIL**, or **NOT APPLICABLE**.

A **FAIL** on any criterion produces a finding.
A finding is a documented statement of fact about the criterion that failed.

---

## SECTION 3 — FINDING FORMAT

Every finding issued under this methodology is structured as follows:

```
FINDING [ID]
Date:        [ISO 8601 date of assessment]
System:      [System identifier as provided by Client]
Version:     [Version string as provided by Client]
Criterion:   [C-1 through C-6]
Status:      FAIL
Observation: [Exact description of what was observed]
Test vector: [Exact input used to produce the observation, where applicable]
Expected:    [What FROZEN-2.0 specifies]
Actual:      [What the system produced]
Severity:    [CRITICAL / MAJOR / MINOR — defined in Section 4]
```

Every field is required. A finding with any field omitted is not a
valid finding under this methodology and will not be issued.

---

## SECTION 4 — SEVERITY CLASSIFICATION

| Severity | Definition |
|----------|-----------|
| CRITICAL | A failure that compromises the integrity of the seal or allows post-seal modification of a sealed entry |
| MAJOR | A failure that produces incorrect calendar representations, malformed schema, or broken remediation linking |
| MINOR | A deviation from specification that does not affect seal integrity or calendar accuracy — interface signature mismatch, non-standard field naming |

Severity is determined by the Architect. It is not negotiated.

---

## SECTION 5 — REMEDIATION VERIFICATION

A remediated finding is assessed as follows:

1. **Original finding is retrieved** — the finding record as issued
2. **Remediation record is located** — linked by finding ID
3. **Remediation claim is verified** — the Architect re-runs the
   test vector that produced the original FAIL
4. **Outcome is one of:**
   - `REMEDIATION VERIFIED` — re-run produces PASS. Original finding
     stands in the record. Remediation record is appended permanently.
   - `REMEDIATION INCOMPLETE` — re-run still produces FAIL, or
     remediation claim cannot be reproduced
   - `REMEDIATION DEFICIENT` — the fix introduces a new non-compliance
     in resolving the original

Only `REMEDIATION VERIFIED` achieves a clean certification status
on the affected criterion.

---

## SECTION 6 — DISPUTE PROCESS

Any party that disputes a finding issued under this methodology
may initiate the following process:

**Step 1 — Technical Submission**
File a `Structural_Audit.md` issue in this repository containing:
- The finding ID being disputed
- The exact test vector used by the disputing party
- The output produced by that test vector
- The specific section of this methodology the party claims
  was incorrectly applied

**Step 2 — Review**
The Architect will review the submission within 14 days and respond
in writing in the issue thread.

**Step 3 — Outcome**
- If the test vector reveals a methodology error: the finding is
  marked `FINDING REVISED` with a note. The original finding
  remains in the record.
- If the test vector confirms the original finding: the dispute
  is closed as `DISPUTE REJECTED` with documented reasoning.
- If the disputing party provides a corrected implementation that
  now passes the relevant criterion: initiate Tier 1 Verification.

**What the dispute process does not do:**
It does not remove the original finding from the record.
It does not negotiate the severity classification.
It does not produce a revised finding that is retroactively
dated to before the original finding was issued.

---

## SECTION 7 — METHODOLOGY VERSIONING

This methodology is versioned. Version 1.0 is published with
this repository. Updates will be versioned, timestamped, and
appended to the git history. Prior versions are preserved.

A finding issued under a specific methodology version is assessed
against that version. Retroactive reapplication of a newer
methodology version to older findings requires a new assessment
engagement.

---

## SECTION 8 — FACTUAL BASIS DECLARATION

All findings issued under this methodology are factual assessments
of observable system behavior against a published, versioned
technical standard. They are not:

- Opinions about the quality, safety, or suitability of any system
- Editorial commentary on any vendor, organization, or individual
- Comparative rankings or commercial recommendations
- Predictions about future system behavior

A finding that says "criterion C-2 (seal computation) failed on
test vector X" is a documented observation of a specific behavior.
It is no different in legal character from a software test reporting
a failed assertion. It is not defamatory. It is not trade libel.
It is a measurement.

The falsifiability of every finding under this methodology is its
legal protection.

---

*METHODOLOGY.md — Sovereign Trace Protocol*
*Version 1.0 | Author: Sheldon K. Salmon | March 2026*
*This document is part of the immutable epistemic record.*
*Methodology versioning preserves the basis for every finding ever issued.*
