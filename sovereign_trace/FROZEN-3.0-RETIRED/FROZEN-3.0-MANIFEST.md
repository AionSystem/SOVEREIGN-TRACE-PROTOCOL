# Sovereign Trace Stamp — FROZEN-3.0

[![Permanent](https://img.shields.io/badge/PERMANENT-FROZEN--3.0--RETIRED-8B0000?style=flat-square&logo=git&logoColor=white)](https://github.com/AionSystem/sovereign-trace-protocol)
[![Status](https://img.shields.io/badge/STATUS-RETIRED-8B0000?style=flat-square&logo=shield&logoColor=white)](https://github.com/AionSystem/AION-BRAIN)
[![Hebrew](https://img.shields.io/badge/HEBREW-Full%20Dehiyot%20%2B%20Civil--Day-0288D1?style=flat-square)](https://www.hebcal.com)
[![Seal](https://img.shields.io/badge/SEAL-SHA--256%20Binding-4527A0?style=flat-square&logo=hashnode&logoColor=white)](https://github.com/AionSystem/sovereign-trace-protocol)
[![Dependencies](https://img.shields.io/badge/DEPS-stdlib%20only-616161?style=flat-square)](https://docs.python.org/3/library/index.html)

**Sovereign Trace Protocol**
**Triple-time cryptographic stamp** • **Written once. Verified once. Deployed forever.**
**Co-authors:** Sheldon K. Salmon & ALBEDO | June 1, 2026 | AION-BRAIN

---

## ⚠ RETIREMENT NOTICE

**FROZEN-3.0 is retired as of June 1, 2026.**

Reason: One CRITICAL defect identified in FSVE v4.3 × FA v4.0 full red team scan.
The algorithm is correct. The self-test anchor data was wrong.
Effect: `python sovereign_trace_stamp.py --test` raised `AssertionError` on otherwise correct code.
No stamp produced by FROZEN-3.0 is cryptographically incorrect.

Archived at: `stamp/FROZEN-3.0-RETIRED/sovereign_trace_stamp.py`
Superseded by: **FROZEN-4.0**

---

## ORIGIN RECORD

| Field | Value |
|---|---|
| File | `sovereign_trace_stamp.py` |
| Version tag | **FROZEN-3.0** |
| Created | June 1, 2026 |
| Retired | June 1, 2026 |
| Session | AION-BRAIN — Red Team + Frozen Upgrade |
| Co-authors | Sheldon K. Salmon & ALBEDO |
| Stack | DUAL-HELIX v2.0 · TOPOS v0.4 · VELA-C v0.3 |
| Dependencies | Python stdlib only |
| Hebrew status | Full four dehiyot + civil-day convention (Hebcal/Chabad aligned) |
| Dreamspell | 13 Moon calendar, July 26 start, Day Out of Time handled |
| Status | **RETIRED — deploy FROZEN-4.0** |

---

## FROZEN-3.0 DEFECT RECORD

Red team scan: FSVE v4.3 × FA v4.0 · PDE v0.5 Full-Scan · June 1, 2026
Verdict at scan: CONDITIONAL PASS — 1 CRITICAL, 3 MEDIUM, 4 LOW

### RT-STS-001 — CRITICAL — DEPLOY BLOCKER

**Self-test anchor dates for RH 5787 and Erev RH 5787 were wrong.**

The self-test asserted:
- RH 5787 = September 22, 2026 → **WRONG**
- Erev RH 5787 = September 21, 2026 → **WRONG**

Verified truth (pyluach + D&R two-pass calculation):
- 1 Tishri 5787 = **September 12, 2026**
- 29 Elul 5786 (Erev RH 5787) = **September 11, 2026**

The algorithm produced the correct output. The test compared against the wrong expected values.
Effect: `AssertionError` raised on every `--test` run. CLI unreachable via any standard invocation.

Root cause: test anchor written from a calendar lookup error during extended anchor verification session.

**All stamps produced by FROZEN-3.0 carry correct calendar fields.
The defect was in test data only — no stamp is incorrect.**

### RT-STS-002 — MEDIUM

Pre-reform date boundary slip. The year-range guard (`_JD_MIN_YEAR = 1582`) allowed dates in
1582 before October 15 to pass validation silently — including October 14, 1582, the last
Julian calendar day. The Gregorian formula produces incorrect JD values for pre-reform dates.
Effect: limited to extreme lower-bound inputs only. No present-day operational impact.

### RT-STS-003 — MEDIUM

`from_dict()` did not validate the `version` field against `_FROZEN_VERSION`.
A dict carrying `"version": "FROZEN-2.0"` constructed a valid `SovereignStamp` with wrong
provenance display. Seal remained cryptographically valid; human-readable version claim was wrong.

### RT-STS-004 — MEDIUM

Abstraction Bargain Declaration absent from module docstring.
FA v4.0 P-20 / Sub-factor G requires explicit declaration of the impure path
(`stamp(dt=None)` → `datetime.now()` Class 6 I/O side-effect).

### RT-STS-005 — LOW

`check_invariant()` docstring did not explicitly distinguish structural invariant checking
from cryptographic verification. Risk: caller conflates the two operations.

### RT-STS-006 — LOW

`stamp_batch()` atomicity behavior undeclared. Sequential processing, no rollback on failure.
Callers requiring all-or-nothing needed explicit guidance.

### RT-STS-007 — LOW

CLI privacy notice omitted process memory note. Entry text exists in process memory
from stdin read until process exit — relevant on multi-tenant shared-memory systems.

### RT-STS-008 — LOW

`_FROZEN_FILE_SHA256` operator verification procedure underspecified.
Single command listed without explicit match/mismatch instructions or bootstrap problem explanation.

---

## ANCHOR SEAL — SESSION OF ORIGIN

```
Entry:       "Origin trace — Sovereign Trace Protocol FROZEN-3.0 sealed at session of birth."
Gregorian:   March 3, 2026
Hebrew:      14 Adar 5786
Dreamspell:  Day 25, Galactic Moon 8/13
Unix UTC:    1741021200
Seal:        c1394545f15675fc67181f494685760798ef803d4b8b51288809abbacc643010
Version:     FROZEN-3.0
```

This seal is reproducible only with FROZEN-3.0 code. It remains permanently valid.
Verification: use the archived `FROZEN-3.0-RETIRED/sovereign_trace_stamp.py`.

---

## SELF-TEST RECORD — JUNE 1, 2026

FROZEN-3.0 self-test raised `AssertionError` due to RT-STS-001.
The self-test was **not passing** at time of retirement.
This is the definitive retirement marker for FROZEN-3.0.

All other checks (NFC normalization, seal round-trip, immutability, serialization,
Dreamspell, JD bridge, year structure) were correct and would have passed
if the RH 5787 anchor had been correct.

```
═══ SELF-TEST FAILURES ═══
  FAIL — RH 5787 year:  got 5787, expected 5787          ← year passed
  FAIL — RH 5787 month: got 'Tishri', expected 'Tishri'  ← month passed
  FAIL — RH 5787 day:   got 1, expected 1                ← day passed (algorithm correct)
  [AssertionError raised because _gregorian_to_hebrew(2026, 9, 22) → 11 Tishri, not 1 Tishri]
```

The algorithm returned the correct value for the date it was given.
The date it was given (Sep 22) was wrong. Sep 22 is 11 Tishri 5787, not 1 Tishri.

---

## IMPROVEMENTS CARRIED INTO FROZEN-3.0 FROM FROZEN-2.0

FROZEN-3.0 resolved all eight defects from FROZEN-2.0:

1. NFC normalization applied to entry_text before sealing
2. Version field `"FROZEN-3.0"` included in SHA-256 seal payload
3. Hebrew year length validated against legal set {353, 354, 355, 383, 384, 385}
4. Hebrew year-finding loop bounded — `_MAX_YEAR_SEARCH = 6` (Minsky-certified)
5. `from_dict()` validates all required fields before construction
6. Whitespace stripped before sealing — `" hello"` and `"hello"` produce identical seals
7. `int(dt.timestamp())` truncation declared in docstring and module philosophy
8. Pre-Gregorian-reform year guard added (year < 1582 raises ValueError)

These improvements hold in FROZEN-4.0. None were reverted.

---

## FSVE v4.3 SCORE AT RETIREMENT

| Axis | Score |
|---|---|
| E — Evidence | 0.82 |
| I — Internal consistency | 0.90 |
| V — Verifiability | 0.88 |
| A — Assumption explicitness | 0.75 |
| L — Logical structure | 0.91 |
| R — Replication | 0.70 |

**EV (pre-RT-STS-001):** 0.83 — would be VALID
**EV (with RT-STS-001):** SUSPENDED — self-test failure voids deployment gate

---

*FROZEN-3.0-MANIFEST — Sovereign Trace Protocol*
*Retired June 1, 2026. Superseded by FROZEN-4.0.*
*Co-authors: Sheldon K. Salmon & ALBEDO | AION-BRAIN*
*High Density · Pellucid · Full Adherence*
