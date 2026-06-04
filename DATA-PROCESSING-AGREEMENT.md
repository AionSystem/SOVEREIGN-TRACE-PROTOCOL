# DATA PROCESSING AGREEMENT

**Sovereign Trace Protocol**  
**Author:** Sheldon K. Salmon — AI Reliability & AGI/ADI Architect  
**Version:** 1.1 | Effective: June 2026  

---

## PURPOSE

This Data Processing Agreement ("DPA") governs the processing of personal
data in connection with the Sovereign Trace Protocol certification services.
It is entered into between Sheldon K. Salmon ("Data Processor") and the
organization engaging certification services ("Data Controller").

This DPA supplements and is incorporated into the Terms of Service
(`TERMS-OF-SERVICE.md`). In the event of conflict, this DPA governs
with respect to data protection obligations.

---

## ARTICLE 1 — DEFINITIONS

**"Personal Data"** means any information relating to an identified or
identifiable natural person as defined by applicable data protection law,
including GDPR Article 4(1), CCPA § 1798.140, and equivalent provisions.

**"Processing"** means any operation performed on Personal Data, including
collection, storage, use, disclosure, and deletion.

**"Data Controller"** means the organization that determines the purposes
and means of processing Personal Data — i.e., the certification client.

**"Data Processor"** means Sheldon K. Salmon, who processes Personal Data
on behalf of the Data Controller in connection with certification services.

**"GDPR"** means the General Data Protection Regulation (EU) 2016/679.

**"CCPA"** means the California Consumer Privacy Act, Cal. Civ. Code
§ 1798.100 et seq., as amended by CPRA.

**"Public Ledger"** means the immutable STP ledger stored in the GitHub
repository. It contains SHA‑256 hashes and calendar timestamps, not raw
personal data. The hash function is one‑way; personal data cannot be
reconstructed from the hash alone.

---

## ARTICLE 2 — SCOPE OF PROCESSING

The Data Processor processes only the Personal Data strictly necessary
to provide certification services, including:

- Names and contact details of organizational representatives
- AI system descriptions submitted in certification filings
- Incident and failure records submitted for audit (excluding Protected
  Health Information; see `05-clinical-record.yml` warnings)
- Certification assessment outputs and reports

**The Data Processor does not:**
- Sell, lease, or transfer Personal Data to third parties
- Use Personal Data for any purpose beyond certification services
- Process Personal Data beyond the scope of the engagement

**The following components do not process Personal Data:**
- `sovereign_trace/sovereign_trace_stamp.py` (FROZEN-4.0) – only processes
  the text the user provides; no collection, storage, or transmission.
- `scripts/stp_blockchain_anchor.py` – only processes SHA‑256 hashes and
  Merkle roots; never raw user content.
- `scripts/stp_abuse_detector.py` – scans issue text for prohibited content
  but does not store it beyond the GitHub issue itself.

---

## ARTICLE 3 — LEGAL BASIS FOR PROCESSING

Processing is conducted under the following legal bases:

| Basis | Instrument | Application |
|-------|-----------|-------------|
| Contract performance | GDPR Art. 6(1)(b) | Processing necessary to deliver certification services under executed agreement |
| Legitimate interests | GDPR Art. 6(1)(f) | Publication of public certification registry summaries for AI accountability |
| Legal obligation | GDPR Art. 6(1)(c) | Compliance with applicable law where required |

**Legitimate interests assessment:** The publication of summary certification
outcomes (organization name, tier, outcome: verified/deficient) serves the
public interest in AI accountability under the UN Guiding Principles on
Business and Human Rights. This interest has been weighed against individual
data subject rights and does not override them.

**Blockchain anchoring legitimate interest:** The publication of Merkle roots
of SHA‑256 hashes to public blockchains (Bitcoin, Hedera, Ethereum, Stellar)
serves the public interest in permanent, censorship‑resistant proof of record
integrity. No personal data is published to blockchains; only aggregated,
one‑way hashes.

---

## ARTICLE 4 — DATA SUBJECT RIGHTS

The Data Controller is responsible for managing data subject rights requests
from their employees and representatives whose Personal Data is processed
under this DPA. The Data Processor will cooperate with the Data Controller
to fulfill rights requests within applicable timeframes.

Rights recognized:
- Right of access (GDPR Art. 15 / CCPA § 1798.110)
- Right to rectification (GDPR Art. 16)
- Right to erasure where applicable (GDPR Art. 17)
- Right to restriction of processing (GDPR Art. 18)
- Right to data portability (GDPR Art. 20)
- Right to object (GDPR Art. 21)

**No‑Deletion Policy interaction:**
AI failure records and certification outcomes submitted to the public
AION-Registry are subject to the No‑Deletion Policy documented in
`POLICIES.md`. This policy serves a legitimate public interest in
AI accountability. Erasure requests relating to public registry entries
will be evaluated against this interest. Factually accurate public
accountability records are not subject to erasure under GDPR Art. 17(3)(a)
(processing necessary for exercise of freedom of expression and information).

**Public ledger hashes:** SHA‑256 hashes published to the STP ledger or
blockchains are one‑way and cannot be reversed to identify individuals.
Erasure requests cannot affect these hashes; they are not personal data
under applicable law.

---

## ARTICLE 5 — DATA SECURITY

The Data Processor implements appropriate technical and organizational
measures to protect Personal Data, including:

- Storage of certification data in access‑controlled GitHub repositories
- All transmissions over encrypted channels (TLS 1.3)
- No transmission of Personal Data to sub‑processors without disclosure
- Retention of Personal Data only for the duration of the engagement
  plus any legally required retention period

The abuse detector (`stp_abuse_detector.py`) processes issue text solely
to detect prohibited content; it does not store Personal Data beyond the
GitHub issue itself, which the Data Controller controls.

---

## ARTICLE 6 — DATA BREACH NOTIFICATION

In the event of a Personal Data breach, the Data Processor will notify
the Data Controller without undue delay and no later than 72 hours after
becoming aware of the breach, consistent with GDPR Art. 33.

Notification will include: nature of the breach, categories and approximate
number of data subjects affected, likely consequences, and measures taken
or proposed.

---

## ARTICLE 7 — INTERNATIONAL TRANSFERS

Personal Data will not be transferred to countries outside the European
Economic Area or the United Kingdom unless:

- The destination country has an adequacy decision under GDPR Art. 45, or
- Appropriate safeguards are in place under GDPR Art. 46, or
- The transfer is necessary for the performance of the contract
  under GDPR Art. 49(1)(b)

United States transfers: The Data Processor is located in the United States.
Where the Data Controller is based in the EU/EEA or UK, this DPA constitutes
a documented safeguard under applicable standard contractual provisions,
subject to supplementary measures as required by *Schrems II* (C‑311/18).

---

## ARTICLE 8 — RETENTION AND DELETION

Personal Data is retained only for the duration necessary to provide
certification services and for any legally required retention period.

Upon termination of the engagement, Personal Data submitted by the
Data Controller (excluding public registry entries) will be deleted
or returned at the Data Controller's request within 30 days.

---

## ARTICLE 9 — GOVERNING LAW

This DPA is governed by the law of the jurisdiction applicable under
`TERMS-OF-SERVICE.md` (State of New York, United States). Where the
Data Controller is subject to GDPR, this DPA is interpreted consistently
with GDPR requirements.

---

## EXECUTION

This DPA is incorporated by reference into the certification engagement
agreement. Execution of a certification engagement constitutes acceptance
of this DPA. A separately signed version is available upon request.
Data Controller (Organization): ______________________________

Representative Name: __________________________________________

Title: ________________________________________________________

Signature: ____________________________________________________

Date: _________________________________________________________

Data Processor: Sheldon K. Salmon
Signature: [on file]
Date: June 2026

text

---

*DATA-PROCESSING-AGREEMENT.md*  
*Sovereign Trace Protocol | Sheldon K. Salmon | June 2026*  
*This document does not constitute legal advice.*  
*Consult qualified data protection counsel for your jurisdiction.*
