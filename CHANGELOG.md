# CHANGELOG

**Sovereign Trace Protocol**
Architect: Sheldon K. Salmon — AI Reliability & ADI Architect
Governing Standard: FROZEN-4.0
Repository: [github.com/AionSystem/SOVEREIGN-TRACE-PROTOCOL](https://github.com/AionSystem/SOVEREIGN-TRACE-PROTOCOL)

---

> This changelog is an epistemic record, not a marketing document. Every defect is named. Every retirement is documented. The frozen versioning philosophy demands it: a stamp function is only permanent if the history of what changed and why is also permanent.

---

## [4.0.0] — June 1, 2026

**Status: CURRENT — FROZEN-4.0**

### Stamp Engine

- `sovereign_trace_stamp.py` promoted to FROZEN-4.0 after full red team pass
- 82 self-test checks passing (up from 35 in FROZEN-2.0)
- All FROZEN-3.0 defects resolved — see Retired section for details

### Red Team Audit

- Full dual-framework audit: FSVE v4.3 × FA v4.0
- **1 CRITICAL finding resolved:** Self-test anchor dates for RH 5787 and Erev RH 5787 were incorrect. Algorithm was correct; test data was not. Effect: self-test raised `AssertionError` on otherwise valid stamps. Anchor dates corrected and re-verified against authoritative Hebrew calendar sources.
- **3 MEDIUM findings resolved:** Edge case handling for year-boundary Dreamspell transitions; NFC normalization edge case on rare Unicode inputs; display formatting inconsistency on multi-line seals.
- **4 LOW findings resolved:** Docstring accuracy; CLI help text; performance optimization on batch stamp calls; minor type annotation gaps.
- **0 unresolved findings.**

### Infrastructure

- `FROZEN-3.0-RETIRED/` directory added with retired stamp file and manifest
- `FROZEN-4.0-MANIFEST.md` added documenting all self-test anchor cases
- Test suite expanded: 29 test files covering async, backward compatibility, CLI, concurrency, display, calendar math, file integrity, frozen version lock, and verification

### Documentation

- `README.md` updated: EDS section with worked example, Deliverables column added to certification tier table, CI badges added, Sample Audit Report callout added
- `CHANGELOG.md` created (this file)
- `EPISTEMIC-DEBT-SCORE.md` published — full public formula, FROZEN-2.0 governing standard
- `SAMPLE-AUDIT-REPORT.md` added — anonymized Tier 1 audit output for procurement evaluation

### PyPI

- `sovereign-trace 4.0.0` — pending push at time of this changelog entry

---

## [3.0.0] — Retired

**Status: RETIRED — FROZEN-3.0**
**Primary defect:** Self-test anchor data error.

### What Changed from 2.0

- Full dehiyot reimplementation with extended boundary coverage
- NFC normalization added for Unicode inputs
- Version field added to seal output
- Pre-reform calendar boundary slip corrected
- Hebrew year loop bounded (unbounded loop defect from FROZEN-2.0 resolved)
- Self-test expanded from 35 to 79 checks

### Defect That Caused Retirement

Self-test anchor dates for Rosh Hashanah 5787 and Erev Rosh Hashanah 5787 were entered incorrectly during test data construction. The calendar algorithm was correct. The test data was not. Any machine running the FROZEN-3.0 self-test would receive an `AssertionError` despite the stamp function producing cryptographically valid output.

> **All FROZEN-3.0 stamps are cryptographically valid.** The seal is correct. The calendar fields are correct. The defect was in the self-test only — it did not affect stamp output. No FROZEN-3.0 stamp requires re-sealing.

### Retirement Date

June 1, 2026 — upon promotion of FROZEN-4.0.

---

## [2.0.0] — Retired

**Status: RETIRED — FROZEN-2.0**
**Primary defects:** Eight defects identified in FROZEN-1.0 red team pass.

### What Changed from 1.0

- Full dehiyot implementation replacing the incomplete FROZEN-1.0 implementation
- Hebrew calendar off-by-one corrected across all 5786 dates
- NFC normalization added (absent in FROZEN-1.0)
- Version field added to seal
- Pre-reform boundary slip corrected
- Hebrew year loop bounded
- Dreamspell calendar verified against authoritative Arguelles source
- 35 self-test checks added (FROZEN-1.0 had none)

### Known Defects at Retirement

FROZEN-2.0 was retired when the following were identified during FROZEN-3.0 development:

1. NFC normalization incomplete for certain combining character sequences
2. Version field not included in the canonical JSON before hashing
3. Minor pre-reform boundary edge case not covered
4. Hebrew year loop technically unbounded under adversarial input
5–8. Four additional low-severity issues documented in FROZEN-3.0-MANIFEST.md

> **All FROZEN-2.0 stamps remain valid** for their stated content. If the Hebrew field in a FROZEN-2.0 stamp is correct (verify against hebcal.com for the stamped date), the stamp is a valid record. The seal binds whatever calendar string was generated — even if that string was incorrect in FROZEN-1.0.

### PyPI

- `sovereign-trace 2.0.0` — live at pypi.org/project/sovereign-trace/

### Retirement Date

Upon promotion of FROZEN-3.0. Exact date recorded in FROZEN-2.0-MANIFEST.md.

---

## [1.0.0] — Retired

**Status: RETIRED — FROZEN-1.0**
**Primary defect:** Incomplete dehiyot implementation — Hebrew calendar off-by-one on all 5786 dates.

### What This Version Was

The founding stamp function. Established the triple-time architecture: Gregorian + Hebrew + 13 Moon Dreamspell. Established the SHA-256 seal. Established the frozen versioning philosophy.

### Defect That Caused Retirement

The Hebrew lunisolar calendar requires four postponement rules (dehiyot) to determine the correct start of each year. FROZEN-1.0 implemented these rules incompletely. The result: Hebrew dates were off by one day for a significant fraction of dates across the year 5786. The civic (Gregorian) timestamp and Dreamspell timestamp were unaffected. The seal was cryptographically valid — it correctly bound the (incorrect) Hebrew string.

> **FROZEN-1.0 stamps carry an incorrect Hebrew field.** The seal is cryptographically valid but binds the wrong calendar string. If Hebrew date accuracy matters for a sealed record, re-seal with FROZEN-4.0 and use the WEBEATER-LINK mechanism (template `09-webeater-link.yml`) to bind the new seal to the original, preserving chain of custody.

### First Seal

The founding ledger entry (`STP-GENERAL-TRACE-2026-03-09-000005.json`) was sealed with FROZEN-2.0, not FROZEN-1.0. FROZEN-1.0 was retired before the public ledger was opened.

### Retirement Date

March 9, 2026 — upon promotion of FROZEN-2.0.

---

## Versioning Philosophy

The Sovereign Trace Protocol uses **frozen versioning**, not semantic versioning.

A version is not a feature release. It is a permanent artifact. The stamp function must be frozen because the permanence of every seal it generates depends on the stability of the function that generated it. A patched stamp function is an epistemically different instrument than the one that produced existing seals.

**Rules:**
- No patches. No hotfixes. No minor releases.
- If a defect is found: retire the frozen file, document the defect completely, build the next version from first principles, re-verify all anchor cases.
- The defect history is never deleted. It is an epistemic record.
- Retired versions remain in the repository under `FROZEN-[N].0-RETIRED/` permanently.

**Version numbering:** FROZEN-N.0 where N is an integer. The `.0` is structural — there are no `.1`, `.2` subversions. Every release is a full rewrite from anchor verification.

---

## Ledger Entries Referenced

| Entry | Date | Significance |
|---|---|---|
| `STP-GENERAL-TRACE-2026-03-09-000005.json` | March 9, 2026 | Founding seal — first public ledger entry |
| `STP-RESEARCH-PRIORITY-2026-03-14-U3N9CK.json` | March 14, 2026 | First research priority seal |
| `STP-INTEGRITY-VIOLATION-March-27-2026-3B5F2D.json` | March 27, 2026 | First integrity violation report filed |
| `STP-INTEGRITY-VIOLATION-March-27-2026-ACD8A4.json` | March 27, 2026 | Second integrity violation report filed |

---

*The changelog is part of the permanent record. It does not summarize history. It is history.*

---

**Sovereign Trace Protocol — CHANGELOG**
Architect: Sheldon K. Salmon · aionsystem2026@gmail.com
Repository: github.com/AionSystem/SOVEREIGN-TRACE-PROTOCOL
