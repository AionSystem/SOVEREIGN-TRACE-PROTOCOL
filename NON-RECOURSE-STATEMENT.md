# NON-RECOURSE STATEMENT
## Sovereign Trace Protocol — Scope of Guarantee

**Document Version:** NRS-v1.1
**Governing Law:** State of New York, United States
**Arbitration:** JAMS Commercial Rules
**Effective:** June 2026
**Supersedes:** NRS-v1.0 (March 2026)

---

## THE FUNDAMENTAL DISTINCTION

The Sovereign Trace Protocol separates two things that are frequently and dangerously confused:

**The Ink** — the SHA-256 cryptographic seal.
**The Contract** — the content that was sealed.

The Protocol guarantees the Ink. It makes no representation about the Contract.

A SHA-256 seal proves three things with mathematical certainty:

1. This exact content existed at this exact moment in time.
2. This content has not been altered since it was sealed.
3. Any alteration — however small — is immediately detectable.

A SHA-256 seal does **not** prove:

1. That the content is true.
2. That the content is accurate.
3. That the content is complete.
4. That the content was not fabricated before sealing.

This distinction is not a limitation of the Protocol. It is the honest boundary of what mathematics can prove.

---

## SCOPE OF GUARANTEE

### What STP guarantees — absolutely and unconditionally:

**Temporal integrity.** The seal anchors content to a specific moment. The timestamp cannot be backdated. The Unix UTC value is the ground truth, verifiable by any party with Python 3.11+ and the raw ledger file.

**Tamper evidence.** Any modification to sealed content — including a single character, space, or punctuation mark — produces a completely different SHA-256 hash. Tampering is not merely detected. It is mathematically impossible to conceal.

**Immutability of the ledger record.** Once a ledger entry is committed to the public repository, it is permanent. It cannot be deleted, altered, or hidden. The Git history is the proof.

**Verification independence.** Any party can verify any seal without contacting Sheldon K. Salmon, without internet access, and without any tool beyond a standard Python interpreter and the raw JSON ledger file. The protocol does not require trust in any person or institution to function.

---

### What STP does **not** guarantee:

**Content truthfulness.** The Protocol seals what was submitted. It does not verify whether the submission is accurate, honest, or representative of reality. A false record, if sealed, is sealed as a false record — permanently and immutably.

**Pre-seal accuracy.** The Protocol has no visibility into events before the seal is applied. It cannot verify that an AI failure occurred as described, that a remediation was effective, or that the submitting party has accurately represented the situation.

**Completeness.** The Protocol seals what is submitted. It cannot verify that nothing material was omitted.

**Legal compliance.** A certified STP ledger entry is evidence of process integrity. It is not legal advice and does not constitute legal compliance with any regulatory framework unless explicitly assessed under a Tier 3 or Tier 4 certification engagement with Sovereign Trace Protocol.

---

## RESPONSIBILITY OF THE SUBMITTING PARTY

By submitting content for sealing under the Sovereign Trace Protocol, the submitting party acknowledges and accepts sole responsibility for:

1. The accuracy of all content submitted for sealing.
2. The completeness of the record as submitted.
3. The legal and regulatory implications of the sealed content.
4. Any consequences arising from false, misleading, or incomplete submissions.

The act of sealing transfers no responsibility for content accuracy to Sheldon K. Salmon or the Sovereign Trace Protocol.

---

## THE PARADOX OF THE HONEST LEDGER

A ledger with sealed failures is more trustworthy than a ledger with no failures. The Protocol does not reward clean records — it rewards honest ones.

An organization that has sealed AI failures, remediated them, and maintained an honest epistemic record is demonstrably more trustworthy than an organization with no failures on record and no ledger. The former has proof of process integrity. The latter has proof of nothing.

This is the epistemic foundation of the certification system. The seal is not a grade. It is a witness.

---

## LIABILITY LIMITATION

To the maximum extent permitted by applicable law:

Sheldon K. Salmon and the Sovereign Trace Protocol shall not be liable for any damages arising from:

- The content of any sealed ledger entry
- Reliance on any sealed record as evidence of content truth
- Any decision made on the basis of a certified STP record
- Failure to detect pre-seal fabrication or misrepresentation
- Any use of the Protocol outside its documented scope

The Protocol's mathematical guarantee is absolute within its scope. Outside that scope, no warranty is made or implied.

All certification engagements are subject to `TERMS-OF-SERVICE.md`.

---

## PLAIN LANGUAGE SUMMARY

The seal proves the record was not changed after it was created.  
It does not prove the record was true when it was created.

Use it accordingly.

---

*Sheldon K. Salmon · AI Reliability & ADI/AGI Architect · June 2026*  
*Sovereign Trace Protocol · FROZEN-4.0*  
*aionsystem@outlook.com*  
*github.com/AionSystem/SOVEREIGN-TRACE-PROTOCOL*
