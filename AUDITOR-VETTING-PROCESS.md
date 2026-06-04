# AUDITOR VETTING PROCESS
## Sovereign Trace Protocol — Certified Auditor Program

**Document Version:** AVP-v1.1
**Governing Standard:** FROZEN-4.0
**Effective:** June 2026
**Supersedes:** AVP-v1.0 (March 2026)

---

## WHAT A CERTIFIED AUDITOR IS

An STP Certified Auditor is an independent professional authorized
to conduct AI output audits and file audit completions directly to
the Sovereign Trace Protocol ledger under their own badge number.

A Certified Auditor is not an employee or contractor of the
Sovereign Trace Protocol. They are an independently operating
professional who has demonstrated the specific capability to
assess AI outputs honestly and has accepted the obligations
that come with a badge.

The badge is not a credential. It is a commitment.

---

## THE CORE CRITERION

There is one criterion for certification:

**Demonstrated ability to assess AI outputs honestly.**

This is skills-based. It is not credential-based. A PhD in
computer science does not qualify someone who cannot assess
AI outputs honestly. A high school diploma does not disqualify
someone who can.

The vetting process is designed to surface genuine capability —
not to filter by institutional affiliation.

---

## THE VETTING PROCESS — FOUR STAGES

### Stage 1 — Application

File a `12-auditor-application.yml` issue in the Sovereign Trace
Protocol repository.

The application must include:
- Full legal name
- LinkedIn profile URL (required — badge is bound to LinkedIn permanently)
- Professional background summary (2–3 sentences)
- Why you are applying (1 paragraph)
- Any relevant experience with AI systems, audit, or quality assurance

Applications are reviewed Monday and Tuesday only.
Not every application proceeds to Stage 2.

**If the Architect is unavailable** due to illness, travel, or other
circumstances, applications will be reviewed on the next available
Monday or Tuesday following the Architect's return. Applicants will
be notified of any extended delay.

---

### Stage 2 — Skills Assessment

Applicants who pass Stage 1 review receive a Skills Assessment
directly via LinkedIn message from the Architect.

The Skills Assessment consists of 10 real AI outputs selected
from the STP ledger or from publicly available sources.
Applicants must:

1. Identify whether each output contains a failure, and if so,
   classify the failure type using the STP schema.
2. Assess the severity of each failure (Low / Medium / High / Critical).
3. Explain their reasoning for each assessment in plain language.
4. Identify any **epistemic debt** outstanding — gaps in the record
   that would prevent a clean certification finding.

**Definition:** *Epistemic debt* means gaps in the audit record—
missing evidence, unsubstantiated claims, or unresolved contradictions—
that would prevent a clean certification finding.

**What the assessment measures:**
- Accuracy of failure detection (can you find what's wrong?)
- Calibration of severity (do you know how wrong it is?)
- Honest reasoning (do you say "I don't know" when you don't know?)
- Epistemic discipline (do you distinguish what you can prove from
  what you suspect?)

**What the assessment does not measure:**
- Speed
- Credential pedigree
- Familiarity with STP-specific terminology

---

### Stage 3 — Review and Decision

The Architect reviews the Skills Assessment and makes a binary
determination: certified or not certified.

There is no partial certification. There is no provisional badge.
There is no score. Either the capability is present or it is not.

**Criteria for certification:**
- All 10 outputs assessed with honest reasoning
- Failure classification accurate on at least 8 of 10
- No overconfident findings on genuinely ambiguous outputs
  (marking uncertain cases as `[?]` is correct behavior,
  not a failure)
- No fabricated findings — assessments must be traceable to
  the actual output, not to assumed context

**Grounds for immediate rejection:**
- Fabricated findings not grounded in the provided output
- Confident assessment on outputs with insufficient evidence
- Plagiarized or AI-generated assessment submitted as own work

**Appeals process:** Rejected applicants may request a one‑time
review by submitting a written appeal via GitHub issue with label
`auditor-appeal` within 30 days of rejection. The Architect will
respond within 14 days. The decision on appeal is final.

---

### Stage 4 — Badge Issuance

Upon certification:

1. Badge number assigned: `STP-AUDITOR-XXXX` (sequential)
2. Badge SVG generated with auditor name and badge number
3. Entry added to `.github/verified-auditors.json`
4. Badge SHA-256 sealed at issuance — the seal is the issuance record
5. Auditor agreement issued — terms and platform percentage confirmed

**Badge properties at issuance:**
- Non-transferable — bound to legal name and LinkedIn permanently
- SHA-256 sealed — cryptographically anchored to issuance moment
- Term: 1 year from issuance date
- Annual cap: 50 sealed audits per calendar year per badge
- Renewal: reapplication only — prior certification does not
  guarantee renewal

**LinkedIn fallback:** If an auditor's LinkedIn profile becomes
permanently unavailable, the auditor must notify the Architect
within 30 days and provide an alternative professional identity
(e.g., ORCID, GitHub, or verified email) to rebind the badge.
Failure to do so may result in revocation. If an auditor fails
to provide an alternative identity within 90 days of LinkedIn
becoming unavailable, the badge shall be automatically revoked
and recorded as such in the revocation registry.

**Audit cap quality control:** The Architect may, at their
discretion, reject an audit completion that appears to be
submitted solely to meet the cap without substantive assessment.
Such rejection will be noted in the auditor's record but does
not count toward the cap.

---

## AUDITOR OBLIGATIONS

By accepting a badge, the certified auditor agrees to:

1. Conduct all assessments personally — no delegation or
   AI-generated findings submitted under the badge
2. Decline assessments where a conflict of interest exists
3. Report any integrity concern via `13-integrity-violation.yml`
   immediately upon discovery
4. Maintain the confidentiality of any non-public client
   information encountered during an engagement
5. Cease using the badge immediately upon expiration or revocation
   and remove it from any public-facing materials

---

## REVOCATION

A badge may be revoked for:

- Fabricated or falsified audit findings
- Conflict of interest not disclosed
- Bribery, coercion, or integrity violations
- Badge use after expiration without renewal
- Badge transfer or sharing
- Any conduct that materially undermines the integrity of the
  STP ledger

**Revocation procedure (initial phase, first 10 auditors):**
During the initial phase (first 10 certified auditors), the Architect
holds unilateral revocation authority.

**Revocation procedure (production phase, 10+ auditors):**
After the network reaches 10 active auditors, revocation shall require
a 2/3 majority vote of active auditors, with the Architect having a
tie‑breaking vote only.

**Revocation record:**
1. Integrity violation reported via `13-integrity-violation.yml`
   or identified by the Architect
2. Architect reviews within 5 business days
3. If revocation is warranted: badge removed from
   `.github/verified-auditors.json` and added to
   `revoked-auditors.json` with sealed revocation record
4. All future audit completions filed with the revoked badge
   will be automatically flagged `AUDITOR_REVOKED` — permanently
   and immutably

The revocation record itself is sealed and permanent.

---

## THE AUDITOR NETWORK AS INSTITUTION

There are no STP Certified Auditors yet. The first badge has
not been issued.

This document exists because the process of becoming a certified
auditor must be defined before the first badge is issued — not
after. An institution that defines its standards retroactively
is not an institution. It is a retrofit.

The vetting process described here will govern the first
application the same way it governs the fiftieth.

---

## DATA PROTECTION AND RETENTION

All applicant personal data (name, LinkedIn URL, email) will be
used solely for vetting and badge administration. It will not be
shared with third parties except as required by law. Data will be
retained for 7 years after badge expiration or revocation.

---

## GOVERNING LAW AND DISPUTES

This vetting process and any disputes arising from it shall be
governed by the laws of the State of New York, USA, without regard
to its conflict of laws principles. Any legal action shall be brought
exclusively in the state or federal courts located in New York County,
New York.

---

## BADGE REFERENCE

| Field | Value |
|-------|-------|
| Format | `STP-AUDITOR-XXXX` |
| Badge file | `badges/stp-auditor-badge-v2.svg` |
| Registry | `.github/verified-auditors.json` |
| Revocation registry | `.github/revoked-auditors.json` |
| Term | 1 year from issuance |
| Annual audit cap | 50 sealed audits |

---

*Sheldon K. Salmon · AI Reliability & ADI/AGI Architect · June 2026*
*Sovereign Trace Protocol · FROZEN-4.0*
*aionsystem@outlook.com*
*github.com/AionSystem/SOVEREIGN-TRACE-PROTOCOL*
