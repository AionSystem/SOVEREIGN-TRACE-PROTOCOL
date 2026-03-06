# PRIVACY POLICY

**Sovereign Trace Protocol**
**Author:** Sheldon K. Salmon — AI Reliability & AGI Architect
**Version:** 1.0 | Effective: March 2026
**Applies to:** sovereign-trace PyPI package, certification services,
and AionSystem/SOVEREIGN-TRACE-PROTOCOL repository interactions

---

## SUMMARY (Plain Language)

The stamp function runs entirely on your device. It makes no network
calls. No personal data is transmitted anywhere when you use
`sovereign_trace_stamp.py`. Your trace entries never leave your machine
unless you choose to send them somewhere.

Certification services require sharing some information with the author.
This policy explains what that is and how it is handled.

---

## 1. WHO THIS APPLIES TO

This policy applies to:

- Users of the `sovereign-trace` Python package (PyPI)
- Organizations engaging certification services
- Individuals who file issues, submit pull requests, or otherwise
  interact with AionSystem/SOVEREIGN-TRACE-PROTOCOL on GitHub

---

## 2. THE STAMP FUNCTION — ZERO DATA COLLECTION

`sovereign_trace_stamp.py` (FROZEN-2.0) collects no personal data.

When you run `stamp()`, the function:
- Takes your entry text as input
- Computes calendar representations using local date/time
- Generates a SHA-256 hash
- Returns a SovereignStamp object

No data is transmitted. No analytics are collected. No identifiers are
created or stored outside your local environment. The stamp function
has no network capability — by design and by inspection.

This is verifiable: read `stamp/sovereign_trace_stamp.py`. It imports
only `hashlib`, `json`, and `datetime` from the Python standard library.
There is no `requests`, `urllib`, `http`, or any network import.

---

## 3. CERTIFICATION SERVICES — DATA COLLECTED

When you engage certification services, the following personal data
may be collected and processed:

| Data | Purpose | Retention |
|------|---------|-----------|
| Name and title of organizational representative | Identifying the certifying organization | Duration of engagement + 7 years |
| Email address | Communication about the certification | Duration of engagement + 3 years |
| Organization name | Public registry listing | Permanent (AION-Registry — No-Deletion Policy) |
| AI system descriptions | Assessment scope | Duration of engagement + 7 years |
| Incident and failure records | Audit assessment | Permanent for public entries; assessment period for confidential records |
| Payment information | Processing fees | Per payment processor terms — not retained by author |

**Public registry entries are permanent.** Organization name, certification
tier, and outcome are listed in the public AION-Registry. This is a
design commitment, not a modifiable preference. See the No-Deletion Policy
in `POLICIES.md`.

---

## 4. GITHUB INTERACTIONS

When you interact with AionSystem/SOVEREIGN-TRACE-PROTOCOL on GitHub:

- GitHub collects and processes data per its own Privacy Policy
  (github.com/privacy). This author does not control GitHub's data practices.
- Issues, pull requests, and comments you submit are publicly visible
  and become part of the repository record.
- Contributor information submitted via the CLA process is retained
  as part of the contribution record.

---

## 5. LEGAL BASIS FOR PROCESSING (GDPR)

For individuals in the EU/EEA and UK:

| Processing Activity | Legal Basis | GDPR Article |
|--------------------|-------------|--------------|
| Certification engagement | Contract performance | Art. 6(1)(b) |
| Public registry listing | Legitimate interests (AI accountability) | Art. 6(1)(f) |
| Legal record retention | Legal obligation | Art. 6(1)(c) |
| Contributor records | Legitimate interests (IP management) | Art. 6(1)(f) |

---

## 6. YOUR RIGHTS

Depending on your jurisdiction, you may have the following rights
regarding your personal data:

**All jurisdictions:**
- Right to know what personal data is held about you
- Right to correct inaccurate personal data

**EU/EEA/UK (GDPR/UK GDPR):**
- Right of access (Art. 15)
- Right to rectification (Art. 16)
- Right to erasure where applicable (Art. 17) — subject to the
  No-Deletion Policy for public registry entries (Art. 17(3)(a))
- Right to restriction of processing (Art. 18)
- Right to data portability (Art. 20)
- Right to object (Art. 21)
- Right to lodge a complaint with your supervisory authority

**California (CCPA/CPRA):**
- Right to know categories and specific pieces of personal information
- Right to delete (subject to exceptions)
- Right to opt out of sale — note: no personal data is sold
- Right to non-discrimination for exercising CCPA rights

**Canada (PIPEDA):**
- Right of access and correction per PIPEDA Schedule 1, Principles 4.9 and 4.10

---

## 7. DATA SHARING AND THIRD PARTIES

Personal data is not sold, rented, or shared with third parties
for marketing purposes. Period.

Data may be shared only in the following circumstances:
- With service providers necessary to deliver certification services
  (payment processors, legal counsel) — under written confidentiality
  obligations
- When required by law, regulation, or valid legal process
- When necessary to protect the rights, property, or safety of the
  author or others

---

## 8. INTERNATIONAL TRANSFERS

If you are located in the EU/EEA or UK, your personal data may be
transferred to the United States where the author is located.
Such transfers are conducted under appropriate safeguards consistent
with GDPR Chapter V and the UK GDPR. See `DATA-PROCESSING-AGREEMENT.md`
for DPA terms applicable to certification clients.

---

## 9. SECURITY

Reasonable technical and organizational measures are implemented to
protect personal data against unauthorized access, disclosure,
alteration, and destruction. For security concerns, see `SECURITY.md`.

---

## 10. CHILDREN

The Sovereign Trace Protocol is not directed at individuals under
the age of 13. Personal data from children under 13 is not
knowingly collected. If you believe such data has been submitted,
contact via a GitHub issue with label `privacy-concern`.

---

## 11. CHANGES TO THIS POLICY

This policy may be updated. Material changes will be announced
via a GitHub release note. The version history is preserved in
git — prior versions are not deleted.

---

## 12. CONTACT

Privacy inquiries: file a GitHub issue with label `privacy-concern`.
For EU/EEA data subject rights requests under GDPR, use the same channel.
Response within 30 days.

---

*PRIVACY-POLICY.md*
*Sovereign Trace Protocol | Sheldon K. Salmon | March 2026*
*This document does not constitute legal advice.*
*Consult qualified data protection counsel for your jurisdiction.*
