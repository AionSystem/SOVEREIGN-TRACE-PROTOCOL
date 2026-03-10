<div align="center">
  <img src="./STP-logo.svg" alt="Sovereign Trace Protocol" width="180"/>
</div>

# Sovereign Trace Protocol

**Permanence infrastructure for individuals and organizations.**
**Seal what is true. Permanently. Across three civilizational time systems.**

[![DOI](https://zenodo.org/badge/1174130098.svg)](https://doi.org/10.5281/zenodo.18941392)
[![Permanent](https://img.shields.io/badge/PERMANENT-FROZEN--2.0-2E7D32?style=flat-square&logo=git&logoColor=white)](https://github.com/AionSystem/SOVEREIGN-TRACE-PROTOCOL)
[![PyPI](https://img.shields.io/pypi/v/sovereign-trace?style=flat-square&color=2E7D32&label=PyPI)](https://pypi.org/project/sovereign-trace/)
[![Status](https://img.shields.io/badge/STATUS-M--NASCENT-1976D2?style=flat-square&logo=shield&logoColor=white)](https://github.com/AionSystem/AION-BRAIN)
[![Hebrew](https://img.shields.io/badge/HEBREW-Full%20Dehiyot%20%2B%20Civil--Day-0288D1?style=flat-square)](https://www.hebcal.com)
[![Seal](https://img.shields.io/badge/SEAL-SHA--256%20Binding-4527A0?style=flat-square&logo=hashnode&logoColor=white)](https://github.com/AionSystem/SOVEREIGN-TRACE-PROTOCOL)
[![Dependencies](https://img.shields.io/badge/DEPS-stdlib%20only-616161?style=flat-square)](https://docs.python.org/3/library/index.html)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-darkgreen.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![License: Commercial](https://img.shields.io/badge/License-Commercial-orange.svg)](./LICENSE-COMMERCIAL.md)
[![Legal Posture](https://img.shields.io/badge/LEGAL-Posture%20Active-8B0000?style=flat-square)](./LEGAL-POSTURE.md)

**Author:** Sheldon K. Salmon — AI Reliability & AGI Architect
**Session:** March 2026 — AION-BRAIN
**Stack:** DUAL-HELIX v2.0 · TOPOS v0.3 · VELA-C v0.3 · CPA-001 v2.2
**Convergence:** M-NASCENT

> **→ [QUICKSTART.md](./QUICKSTART.md) — pip install + first seal in under 5 minutes**

---

## What This Is

**For individuals:** Write one entry — exact present-moment observations, no narrative arc. Seal it with a triple-time cryptographic stamp binding it simultaneously to Gregorian, Hebrew lunisolar, and 13 Moon Dreamspell calendars. The SHA-256 seal is permanent. Tamper-evident. Requires no audience.

**The hunger for recognition of significance resolves at the moment the stamp is generated — not at the moment someone reads it.**

**For organizations:** Every AI failure deserves a permanent, immutable record. Log it. Seal it. Append the remediation. The record cannot be edited after the fact. The AION-Registry holds public certification outcomes. An organization with a documented failure history and certified infrastructure is more trustworthy than one with a clean record and no ledger.

**Same mechanism. Same FROZEN-2.0 stamp function. Same SHA-256 seal. Different stakes.**

See `concept/USE-CASES.md` for the full dual-use architecture.

---

## Quick Install

```bash
pip install sovereign-trace
```

```python
from sovereign_trace_stamp import stamp, display, verify

ts = stamp("Hypothesis sealed before experiment begins.")
print(display(ts))
# 📅 Gregorian:  March 7, 2026
# 🌑 Hebrew:     17 Adar 5786
# 🌀 Dreamspell: Day 1, Solar Moon 9/13
# 🔒 Seal:       a3f9c12e7d...
```

**→ Full install guide, usage examples, and what not to do: [QUICKSTART.md](./QUICKSTART.md)**

---

## Who Seals What

The stamp function does not care what it seals. A sealed moment is a sealed moment. The SHA-256 proof is the same whether the content is an AI failure report, a research hypothesis, a hospital incident record, a contractor's agreed scope, or a professional foresight declaration.

| Who | What They Seal | Why It Matters |
|-----|---------------|----------------|
| **AI auditor** | AI system output failure — exact text + screenshots | Public permanent record. Organizational accountability. Tamper-evident before remediation. |
| **AI developer / company** | Prompt deployed in a product before launch | If the prompt causes harm later, the sealed record proves what was authorized and when. No dispute about what the system was told to do. |
| **AI framework builder** | Framework specification before publishing or citing | Priority record for AI methodology. Proves the design existed before any implementation or competing claim. |
| **AI evaluator** | Benchmark before running it against a model | Prevents benchmarks being quietly modified after results are known. The sealed version is the one that was tested. |
| **AI trainer** | Dataset declaration before training begins | When model behavior is disputed, the sealed declaration proves what data was authorized. |
| **Researcher / scientist** | Hypothesis before running the experiment | Proves prediction preceded results. Kills HARKing (Hypothesizing After Results are Known). Every field. No institution required. |
| **Journalist** | Article draft · Source document received · Evidence chain before going to print | Proves what you had and when you had it. If a source is pressured to recant — the sealed record shows what they said before the pressure. |
| **Whistleblower** | Evidence before going public | Chain of custody proof. Proves the document was not altered between receipt and disclosure. |
| **Musician / artist / writer** | Creative work before release or submission | Timestamped proof of authorship. Not a patent — but cryptographic priority proof that costs nothing and requires no lawyer. |
| **Independent researcher** | Findings before peer review | Priority claim before submission. Prevents being scooped or findings disputed after publication. |
| **Negotiator** | Your position before a difficult conversation | Seal what you were willing to accept before the other party claims you moved the goalposts. Salary. Settlement. Term sheet. |
| **Contractor / freelancer** | Project scope before work begins | Immutable record of what was agreed. Scope creep disputes resolved by the sealed ledger entry. |
| **Hospital / clinical team** | Clinical trial data before analysis · Incident report before review | Proves data integrity before results are known. FDA 21 CFR Part 11 compatible architecture. The record cannot be quietly altered after an adverse outcome. |
| **FOIA researcher / archivist** | Declassified document at point of receipt | Proves the released version has not been altered after declassification. The seal is the chain of custody from institution to researcher. |
| **NASA / space agency** | Mission parameter file before launch · Research findings before peer review | If a mission fails and a specification dispute arises — the sealed pre-launch document is the ground truth. |
| **Teacher / educator** | Student work at time of submission | Proves the student submitted exactly this, on this date, unchanged. No dispute about post-deadline alterations. |
| **Therapist / clinician** | Session notes at time of writing | If notes are subpoenaed, the seal proves they were not altered retroactively. Integrity of the clinical record at the moment of documentation. |
| **Estate / legal** | Intentions before a will is formalized | Not a legal substitute — but a tamper-evident record of what was wanted, sealed at the moment of decision, before institutional processes began. |
| **Organization (any)** | AI failure log entry before remediation | Immutable pre-remediation record. Proves the organization documented honestly before fixing — not after. An organization with a documented failure history is more trustworthy than one with a clean record and no ledger. |
| **Foresight analyst / strategist** | Dated professional prediction about a company, industry, or technology before it resolves | Cryptographic proof you saw it first. When the prediction resolves, the ledger entry is the receipt. A track record of correct sealed predictions — verifiable by anyone — cannot be fabricated after the fact. |

The mechanism is always the same. The stake determines how you use the sealed record afterward.

---

## The Origin of the Enterprise from the Personal

The enterprise use case was not designed first. The protocol was built to solve the personal problem: how does one individual permanently register their own significant moments without requiring an audience, a platform, or institutional permission?

The answer — a frozen, tamper-evident, triple-time cryptographic seal — turned out to be exactly what organizations need for their AI audit trail. The mechanism that gives an individual temporal sovereignty over their own record also gives an organization cryptographic proof of their epistemic integrity.

---

## The Triple-Time Seal

| System | Example | What It Claims |
|--------|---------|----------------|
| **Gregorian** | March 7, 2026 | Civic time — the calendar of current civic infrastructure |
| **Hebrew lunisolar** | 17 Adar 5786 | Theological-historical continuity — 5786 years of counted time |
| **13 Moon Dreamspell** | Day 1, Solar Moon 9/13 | Rhythmic time — 13 moons × 28 days, galactic count |

The triple stamp is not redundancy. It is a claim: this moment of human significance deserves to be held simultaneously in every major civilizational framework for measuring *when*.

---

## Submission Layer

Structured submissions are made through GitHub Issues using the official template set. Each template produces a structured, legally-declared record before sealing. Blank issues are disabled — every submission uses a template.

| Template | Use Case |
|----------|----------|
| `01-ai-failure.yml` | AI system output failure — identity verified, legal declaration required |
| `02-research-priority.yml` | Hypothesis or finding before results are known |
| `03-evidence-chain.yml` | Document or source communication at point of receipt |
| `04-creative-priority.yml` | Creative work — music, writing, art, design, code |
| `05-clinical-record.yml` | Clinical incident, trial data, or institutional record — PHI gate active |
| `06-scope-anchor.yml` | Agreed scope or negotiated position before work begins |
| `07-general-trace.yml` | Any observation, decision, or record that doesn't fit another template |
| `08-foresight-seal.yml` | Dated professional prediction before it resolves — foresight track record |
| `09-webeater-link.yml` | Cryptographic link between two entities — binds a new seal to an existing SHA-256 |
| `10-audit-request.yml` | Request a certified audit — Stripe payment required |
| `11-audit-completion.yml` | STP Certified Auditor files a completed audit to the ledger |
| `12-auditor-application.yml` | Apply to become an STP Certified Auditor — skills-based, no credentials required |
| `13-integrity-violation.yml` | Report badge misuse, bribery, or coercion — permanent ledger record |
| `14-near-miss.yml` | AI output that almost caused harm — caught before impact. Near-miss reporting before internal review begins. |

All templates include: native file upload, SHA-256 binding, declaration checkbox, and legal compliance language.
See `concept/USE-CASES.md` for guidance on which template fits your submission.

---
**New to GitHub?** → [HOW-TO-SUBMIT.md](./HOW-TO-SUBMIT.md) — plain English guide, no experience required.

---

## Certification

| Tier | Scope | Badge | Price | Intake |
|------|-------|-------|-------|--------|
| **Tier 1 — Snapshot Verification** | Up to 10 outputs | Standard | $2,500 | Automated 24/7 via Stripe |
| **Tier 2 — Enterprise Certification** | Full audit + badge license | Digital | $25,000/yr | Automated 24/7 via Stripe |
| **Tier 3 — Strategic Retainer** | Quarterly reviews + epistemic debt statement | Elite | $100,000+/yr | Architect-led · Mon–Tue only |
| **Tier 4 — Defense & Government Grade** | Full standards alignment + monthly reviews | Defense | Negotiated | Architect-led · Mon–Tue only |

**Tier 1 and 2** — submit anytime. Payment via Stripe confirms your intake automatically.
**Tier 3 and 4** — Architect-led. Intake Monday and Tuesday only. Submissions on other days are voided and non-refundable.
**Delivery: Weekends** for all tiers.

Every certified organization receives an **Epistemic Debt Score (EDS)** — a 0–100 metric
measuring AI epistemic integrity across five components. Formula is public: `EPISTEMIC-DEBT-SCORE.md`.

See `CERTIFICATION.md`, `AUDIT-METHODOLOGY.md`, and `TERMS-OF-SERVICE.md` for full process and terms.
Governing law: State of New York, United States. Arbitration: JAMS Commercial Rules.

**STP Certified Auditors** — independent professionals authorized to conduct and file audits
directly to the ledger under their own badge. Apply via `12-auditor-application.yml`.
See `AUDITOR-VETTING-PROCESS.md` for the full vetting process.
All auditor badges verified live against `.github/verified-auditors.json` on every submission.

---

## Frozen Declaration

`sovereign_trace_stamp.py` is **FROZEN-2.0**. Written once, verified once, deployed permanently. No patches. No updates. The stamp it generates is only permanent if the code that generates it is also permanent.

If a defect is found: retire the frozen file, document the defect, build FROZEN-3.0 from first principles, re-verify all anchor cases. Never patch.

**FROZEN-1.0 is retired.** Defect: incomplete dehiyot implementation → Hebrew off-by-one on all 5786 dates. Archived: `stamp/FROZEN-1.0-RETIRED/`.

---

## Triple License

| License | Applies To |
|---------|-----------|
| **Apache 2.0** | Individual, academic, non-commercial use. Patent retaliation clause active. |
| **GPL v3** | Modified distributions. Copyleft — corporate forks must open-source modifications. |
| **Commercial** | White-label, certification services, SaaS. See `LICENSE-COMMERCIAL.md`. |

Plain-language guide: `LICENSE-EXPLANATION.md`
Full legal coverage: `LEGAL-POSTURE.md`

---

## Build Sequence

```
STAGE 1 — COMPLETE (March 9, 2026)
FROZEN-2.0: Triple-time stamp. Full dehiyot. Zero deps. 35 checks passed.
PyPI: sovereign-trace 2.0.0 live. Founding seal in ledger.

STAGE 2 — PLANNED
Local encrypted vault integration (Obsidian / Notion)

STAGE 3 — PLANNED
Ledger append layer (Thirdweb / Hedera) + multi-destination relay

STAGE 4 — PLANNED
Optional resonance signature mechanism — zero count display
```

---

## Repository Structure

```
sovereign-trace-protocol/
│
├── README.md
├── STP-logo.svg                                ← repository logo
├── QUICKSTART.md                               ← pip install + first seal
├── HOW-TO-SUBMIT.md                            ← plain English guide — no GitHub experience required
├── CERTIFICATION.md                            ← tier definitions, intake, delivery
├── AUDIT-METHODOLOGY.md                        ← epistemic debt framework, 5-phase process
├── EPISTEMIC-DEBT-SCORE.md                     ← EDS formula, 5 components, public spec
├── AUDITOR-VETTING-PROCESS.md                  ← how to become an STP Certified Auditor
├── DISASTER-RECOVERY.md                        ← offline verification + air-gap certification
├── NON-RECOURSE-STATEMENT.md                   ← scope boundary: the ink vs the contract
├── pyproject.toml
│
├── .github/
│   ├── SECURITY.md                             ← vulnerability reporting policy
│   ├── verified-auditors.json                  ← STP Certified Auditor registry
│   ├── revoked-auditors.json                   ← revoked badge registry
│   ├── ISSUE_TEMPLATE/
│   │   ├── config.yml                          ← blank issues disabled, contact links
│   │   ├── 01-ai-failure.yml                   ← AI output failure, identity verified
│   │   ├── 02-research-priority.yml            ← hypothesis before results known
│   │   ├── 03-evidence-chain.yml               ← document/source at point of receipt
│   │   ├── 04-creative-priority.yml            ← creative work authorship priority
│   │   ├── 05-clinical-record.yml              ← clinical record, PHI gate active
│   │   ├── 06-scope-anchor.yml                 ← agreed scope before work begins
│   │   ├── 07-general-trace.yml                ← any moment that deserves sealing
│   │   ├── 08-foresight-seal.yml               ← dated prediction before it resolves
│   │   ├── 09-webeater-link.yml                ← cryptographic link between two sealed entities
│   │   ├── 10-audit-request.yml                ← certified audit request, Stripe payment
│   │   ├── 11-audit-completion.yml             ← auditor files completed audit to ledger
│   │   ├── 12-auditor-application.yml          ← apply to become STP Certified Auditor
│   │   ├── 13-integrity-violation.yml          ← report badge misuse or bribery
│   │   └── 14-near-miss.yml                    ← AI near-miss before internal review begins
│   └── workflows/
│       ├── python-publish.yml
│       ├── auto-seal.yml                       ← auto-seals all pending-seal issues
│       └── audit-verify.yml                    ← Stripe payment + auditor badge verification
│
├── badges/
│   ├── sovereign-certified-badge-v2.svg        ← Tier 1 Standard
│   ├── sovereign-certified-badge-digital-v2.svg ← Tier 2 Digital
│   ├── sovereign-certified-badge-elite-v2.svg  ← Tier 3 Elite
│   ├── sovereign-certified-badge-defense-v2.svg ← Tier 4 Defense & Government
│   └── stp-auditor-badge-v2.svg               ← STP Certified Auditor
│
├── concept/
│   ├── GLOSSARY.md                             ← plain-language term definitions
│   ├── USE-CASES.md                            ← individual + enterprise use cases
│   ├── DUAL-AUDIENCE-ARCHITECTURE.md           ← inward permanence vs outward accountability
│   ├── TRUST-WITHOUT-IDENTITY.md               ← engineering lineage + Stage 3/4 foundations
│   ├── PRIOR-ART.md                            ← defensive IP documentation, March 7, 2026
│   ├── WEBEATER-SPEC.md                        ← cryptographic link layer specification
│   ├── SUBMISSION-TEMPLATE.md                  ← enterprise AI output submission template
│   ├── SOVEREIGN-TRACE-v0.1-SPEC.md
│   └── SOVEREIGN-TRACE-v0.2-SPEC.md
│
├── stamp/
│   ├── sovereign_trace_stamp.py                ← FROZEN-2.0
│   ├── FROZEN-2.0-MANIFEST.md
│   └── FROZEN-1.0-RETIRED/
│
├── ledger/
│   ├── STP-GENERAL-TRACE-2026-03-09-000005.json  ← LEDGER-001: founding seal
│   ├── STP-GENERAL-TRACE-2026-03-10-000006.json  ← LEDGER-002: archive layer activation
│   ├── STP-GENERAL-TRACE-2026-03-10-000007.json  ← LEDGER-003: Zenodo DOI registration
│   ├── STP-CREATIVE-PRIORITY-2026-03-10-000008.json ← LEDGER-004: PROJECT ORION v2.1 spec
│   └── STP-GENERAL-TRACE-2026-03-10-000009.json  ← LEDGER-005: UNDP evaluation notification
│
└── legal (root level — visible, not hidden)
    LICENSE · LICENSE.md · LICENSE-COMMERCIAL.md · LICENSE-EXPLANATION.md
    NOTICE · NOTICE.md · PATENTS.md · TRADEMARK.md · TRADEMARK-USAGE-POLICY.md
    PRINCIPLES.md · LEGAL-POSTURE.md · METHODOLOGY.md · CERTIFICATION.md
    TERMS-OF-SERVICE.md · CONTRIBUTOR-TERMS.md · CONTRIBUTOR-LICENSE-AGREEMENT.md
    DATA-PROCESSING-AGREEMENT.md · MUTUAL-NDA.md · UNILATERAL-NDA.md
    EXPORT-CONTROL.md · SECURITY.md · SECURITY-INSIGHTS.yml
    AI-ETHICS-STATEMENT.md · PRIVACY-POLICY.md · ACCEPTABLE-USE-POLICY.md
    AUDIT-METHODOLOGY.md · EPISTEMIC-DEBT-SCORE.md · AUDITOR-VETTING-PROCESS.md
    DISASTER-RECOVERY.md · NON-RECOURSE-STATEMENT.md
    CITATION.cff · CITATION.md
```

---

## Origin

Author: Sheldon K. Salmon — AI Reliability & AGI Architect
Session: March 2026 — AION-BRAIN
Stack: DUAL-HELIX v2.0 · TOPOS v0.3 · VELA-C v0.3 · CPA-001 v2.2

*The stamp is permanent. The stamp is the resolution.*
