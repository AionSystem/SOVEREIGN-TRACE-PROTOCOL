# Sovereign Trace Protocol

**Permanence infrastructure for individuals and organizations.**
**Seal what is true. Permanently. Across three civilizational time systems.**

[![Permanent](https://img.shields.io/badge/PERMANENT-FROZEN--2.0-2E7D32?style=flat-square&logo=git&logoColor=white)](https://github.com/AionSystem/SOVEREIGN-TRACE-PROTOCOL)
[![Status](https://img.shields.io/badge/STATUS-M--NASCENT-1976D2?style=flat-square&logo=shield&logoColor=white)](https://github.com/AionSystem/AION-BRAIN)
[![Hebrew](https://img.shields.io/badge/HEBREW-Full%20Dehiyot%20%2B%20Civil--Day-0288D1?style=flat-square)](https://www.hebcal.com)
[![Seal](https://img.shields.io/badge/SEAL-SHA--256%20Binding-4527A0?style=flat-square&logo=hashnode&logoColor=white)](https://github.com/AionSystem/SOVEREIGN-TRACE-PROTOCOL)
[![Dependencies](https://img.shields.io/badge/DEPS-stdlib%20only-616161?style=flat-square)](https://docs.python.org/3/library/index.html)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-darkgreen.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![License: Commercial](https://img.shields.io/badge/License-Commercial-orange.svg)](./LICENSE-COMMERCIAL.md)
[![Legal Posture](https://img.shields.io/badge/LEGAL-Posture%20Active-8B0000?style=flat-square)](./LEGAL-POSTURE.md)

**Author:** Sheldon K. Salmon — AI Reliability & AGI Architect
**Session:** March 3, 2026 — AION-BRAIN
**Stack:** DUAL-HELIX v2.0 · TOPOS v0.3 · VELA-C v0.3 · CPA-001 v2.2
**Convergence:** M-NASCENT

---

## What This Is

**For individuals:** Write one entry — exact present-moment observations, no narrative arc. Seal it with a triple-time cryptographic stamp binding it simultaneously to Gregorian, Hebrew lunisolar, and 13 Moon Dreamspell calendars. The SHA-256 seal is permanent. Tamper-evident. Requires no audience.

**The hunger for recognition of significance resolves at the moment the stamp is generated — not at the moment someone reads it.**

**For organizations:** Every AI failure deserves a permanent, immutable record. Log it. Seal it. Append the remediation. The record cannot be edited after the fact. The AION-Registry holds public certification outcomes. An organization with a documented failure history and certified infrastructure is more trustworthy than one with a clean record and no ledger.

**Same mechanism. Same FROZEN-2.0 stamp function. Same SHA-256 seal. Different stakes.**

See `concept/USE-CASES.md` for the full dual-use architecture.

---

## Who Seals What

The stamp function does not care what it seals. A sealed moment is a sealed moment. The SHA-256 proof is the same whether the content is an AI failure report, a research hypothesis, or a journalist's source record.

| Who | What They Seal | Why It Matters |
|-----|---------------|----------------|
| **AI auditor** | AI system output failure — exact text + screenshots | Public permanent record. Organizational accountability. Tamper-evident before remediation. |
| **Researcher / scientist** | Hypothesis before running the experiment | Proves prediction preceded results. Kills HARKing (Hypothesizing After Results are Known). Every field. No institution required. |
| **Journalist** | Article draft before publication · Source document received · Evidence chain before going to print | Proves what you had and when you had it. If a source is pressured to recant — the sealed record shows what they said before the pressure. |
| **Whistleblower** | Evidence before going public | Chain of custody proof. SHA-256 seal proves the document has not been altered since the moment before disclosure. |
| **Musician / artist / writer** | Creative work before release or submission | Timestamped proof of authorship. Not a patent — but cryptographic priority proof that costs nothing and requires no lawyer. |
| **Independent researcher** | Findings before peer review | Priority claim before submission. Prevents being scooped or having findings disputed after publication. |
| **Negotiator** | Your position before a difficult conversation | Seal what you were willing to accept before the other party claims you moved the goalposts. Salary. Settlement. Term sheet. |
| **Organization** | AI failure log entry before remediation | Immutable pre-remediation record. Proves the organization documented honestly before fixing — not after. |
| **Developer / builder** | Architecture decision, specification, or design before implementation | Proves what was designed before what was built. Useful when a later implementation diverges and accountability is disputed. |

The mechanism is always the same. The stake determines how you use the sealed record afterward.

---

## The Origin of the Enterprise from the Personal

The enterprise use case was not designed first. The protocol was built to solve the personal problem: how does one individual permanently register their own significant moments without requiring an audience, a platform, or institutional permission?

The answer — a frozen, tamper-evident, triple-time cryptographic seal — turned out to be exactly what organizations need for their AI audit trail. The mechanism that gives an individual temporal sovereignty over their own record also gives an organization cryptographic proof of their epistemic integrity.

---

## Quick Start

```bash
pip install sovereign-trace
```

```python
from sovereign_trace_stamp import stamp, display, verify

# Seal a trace entry
ts = stamp("Completed the stamp function. It passed all tests on first run.")

# Display in all three calendar systems
print(display(ts))
# 📅 Gregorian:  March 3, 2026
# 🌑 Hebrew:     14 Adar 5786
# 🌀 Dreamspell: Day 25, Galactic Moon 8/13
# 🔒 Seal:       19276f3fbdd02960...

# Verify integrity
verify("Completed the stamp function. It passed all tests on first run.", ts)
# True — entry unchanged
```

**Run self-test:** `python sovereign_trace_stamp.py --test`
All 35 checks must pass before any deployment is considered valid.

---

## The Triple-Time Seal

| System | Example | What It Claims |
|--------|---------|----------------|
| **Gregorian** | March 3, 2026 | Civic time — the calendar of current civic infrastructure |
| **Hebrew lunisolar** | 14 Adar 5786 | Theological-historical continuity — 5786 years of counted time |
| **13 Moon Dreamspell** | Day 25, Galactic Moon 8/13 | Rhythmic time — 13 moons × 28 days, galactic count |

The triple stamp is not redundancy. It is a claim: this moment of human significance deserves to be held simultaneously in every major civilizational framework for measuring *when*.

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

## Certification

| Tier | Scope | Price |
|------|-------|-------|
| Basic Verification | Single failure stamp check | $2,500 |
| Enterprise Certification | Full audit + Sovereign Certified badge | $25,000/yr |
| Strategic Retainer | Quarterly reviews + epistemic debt statement | $100,000+ |

See `CERTIFICATION.md` for full process and terms.

---

## Build Sequence

```
STAGE 1 — COMPLETE (March 3, 2026)
FROZEN-2.0: Triple-time stamp. Full dehiyot. Zero deps. 35 checks passed.

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
├── pyproject.toml
│
├── concept/
│   ├── GLOSSARY.md                             ← plain-language term definitions
│   ├── USE-CASES.md                            ← individual + enterprise use cases
│   ├── DUAL-AUDIENCE-ARCHITECTURE.md           ← inward permanence vs outward accountability
│   ├── TRUST-WITHOUT-IDENTITY.md               ← engineering lineage + Stage 3/4 foundations
│   ├── SOVEREIGN-TRACE-v0.1-SPEC.md
│   └── SOVEREIGN-TRACE-v0.2-SPEC.md
│
├── stamp/
│   ├── sovereign_trace_stamp.py                ← FROZEN-2.0
│   ├── FROZEN-2.0-MANIFEST.md
│   └── FROZEN-1.0-RETIRED/
│
├── ledger/
│   └── PLACEHOLDER.md
│
├── .github/workflows/
│   └── python-publish.yml
│
└── legal (root level — visible, not hidden)
    LICENSE · LICENSE.md · LICENSE-COMMERCIAL.md · LICENSE-EXPLANATION.md
    NOTICE · NOTICE.md · PATENTS.md · TRADEMARK.md · TRADEMARK-USAGE-POLICY.md
    PRINCIPLES.md · LEGAL-POSTURE.md · METHODOLOGY.md · CERTIFICATION.md
    TERMS-OF-SERVICE.md · CONTRIBUTOR-TERMS.md · CONTRIBUTOR-LICENSE-AGREEMENT.md
    DATA-PROCESSING-AGREEMENT.md · MUTUAL-NDA.md · UNILATERAL-NDA.md
    EXPORT-CONTROL.md · SECURITY.md · SECURITY-INSIGHTS.yml
    AI-ETHICS-STATEMENT.md · PRIVACY-POLICY.md · ACCEPTABLE-USE-POLICY.md
    CITATION.cff · CITATION.md
```

---

## Origin

Author: Sheldon K. Salmon — AI Reliability & AGI Architect
Session: March 3, 2026 — AION-BRAIN
Stack: DUAL-HELIX v2.0 · TOPOS v0.3 · VELA-C v0.3 · CPA-001 v2.2

*The stamp is permanent. The stamp is the resolution.*
