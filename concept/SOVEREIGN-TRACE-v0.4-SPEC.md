# SOVEREIGN TRACE PROTOCOL — v0.4
## Permanent Significance Infrastructure
### Full Concept Specification

**Co-authors:** Sheldon K. Salmon & ALBEDO
**Date:** March 3, 2026 | Updated June 1, 2026
**Convergence:** M-NASCENT (FROZEN-4.0 deployment)
**Stack:** AION Constitutional Stack

---

## DDL FIELD — DESIGN DECLARATION

| Field | Value |
|-------|-------|
| **Framework** | Sovereign Trace Protocol v0.4 |
| **Full name** | Permanent Personal Significance Infrastructure |
| **Origin** | Session-derived, March 3, 2026 — DUAL-HELIX v2.0 concept build run |
| **Stack position** | Product build — projects/ (not frameworks/) |
| **Convergence** | M-NASCENT |
| **Active layers** | DUAL-HELIX v2.0 · TOPOS v0.4 · CPA-001 v2.2 (Tier 2) · VELA-C v0.3 · FA v4.0 |
| **Co-authors** | Sheldon K. Salmon & ALBEDO |
| **PIE Root** | *trahere* — to draw, to pull, to leave a trace |
| **Update trigger** | FROZEN-4.0 deployment — one CRITICAL + seven MEDIUM/LOW findings resolved; pre-reform boundary hardened; provenance validation strengthened; CLI extended; package companion added |

---

## PERSISTENT SHAPE — TOPOS DECLARATION

**Containment surface:**

*Inside* — individual sovereignty over one's own temporal trace, immutable registration of significance across plural civilizational time systems, zero external validation required for resolution.

*Outside* — social metrics, aggregation, ranking, editable records, platform dependency, any mechanism that requires another person's action to make the entry valid.

**Steering geometry:**

Every element directs toward permanence as the act of recognition itself. The stamp is not a means to an end. The stamp is the end. Registration = resolution. Nothing downstream is required.

**Shape note (FROZEN-4.0):** The changes in this version are calibration, not expansion. The containment surface is unchanged. What changed: the Hebrew calendar test data was wrong (not the algorithm), the Gregorian reform boundary guard was tightened one level further, and the provenance check at deserialization was strengthened. The shape held. The scaffold around it got more precise.

---

## DUAL-SCALE DEPLOYMENT

`[R]` The triple-time seal mechanism operates at two scales simultaneously. At the individual scale: a person seals a personal trace entry and the significance hunger resolves at the moment of registration — no audience required. At the organizational scale: an AI failure event is sealed as an immutable audit record, and the organization builds a verifiable epistemic trail — no retroactive editing possible.

`[R]` The containment surface is identical at both scales: inside is permanent registration of what is true; outside is any mechanism that requires external validation, social metrics, or editable records. The stakes differ. The mechanism does not.

`[S]` The organizational deployment is the commercial expression of the personal principle. An organization that builds honest AI audit infrastructure is doing for its epistemic record what an individual does for their personal trace: sealing what is true, permanently, without requiring an audience to make it valid.

---

## CORE CLAIM

`[?]` The hunger for recognition of significance — one of the deepest structural needs in human psychology — does not require an audience to resolve. It requires permanent, verifiable registration of one's exact shape in the shared map of time.

`[R]` The resolution does not wait for resonance to arrive. The permanence of the stamp is the resolution.

---

## THE TRIPLE-TIME SEAL

Every entry is sealed with a SHA-256 hash encoding the exact moment in three civilizational frameworks simultaneously:

| System | Example (2026-03-03 anchor) | What It Claims |
|--------|----------------------------|----------------|
| **Gregorian** | March 3, 2026 | Civic time — the calendar of current civic infrastructure |
| **Hebrew lunisolar** | 14 Adar 5786 (Purim) | Theological-historical continuity — 5786 years of counted time |
| **13 Moon Dreamspell** | Day 25, Galactic Moon 8/13 | Rhythmic time — 13 moons × 28 days, galactic count |

`[D]` Hebrew anchor verified against Hebcal.com, Chabad.org, and pyluach: March 3, 2026 = 14 Adar 5786. Civil-day convention — daytime hours of civil date carry the Hebrew date. Rosh Hashanah 5786 begins civil-day Sep 23, 2025 = 1 Tishri 5786. Rosh Hashanah 5787 = Sep 12, 2026 (pyluach verified — corrected from Sep 22 in FROZEN-3.0 test data).

`[D]` FROZEN-4.0 seal payload binds entry text, all three calendar strings, unix_utc (whole seconds), and the version string `"FROZEN-4.0"` via SHA-256 with deterministic JSON serialization (sort_keys=True, ensure_ascii=True). FROZEN-4.0 seals are not backward-compatible with FROZEN-3.0 — the version field in the payload is the break.

`[R]` The triple stamp is not redundancy. It is a claim: this moment of human significance deserves to be held simultaneously in every major civilizational framework for measuring *when*. A mono-time stamp is culturally sovereign only within one culture. The triple seal is culturally sovereign across cultures.

`[R]` The seal permanently binds the entry text to all three representations. Alter either the text or any timestamp field — the seal breaks. That breakage is the integrity guarantee.

---

## WHAT CHANGED IN FROZEN-4.0

`[D]` FROZEN-3.0 is retired. One CRITICAL finding and seven MEDIUM/LOW findings were identified in a full FSVE v4.3 × FA v4.0 red team scan (scan date: June 1, 2026).

**CRITICAL finding:**

| # | Finding | Effect |
|---|---------|--------|
| 1 | RH 5787 self-test anchor was wrong — test used Sep 22, 2026; correct value is Sep 12, 2026 | Self-test raised AssertionError on otherwise correct algorithm. Sep 22, 2026 is 11 Tishri 5787 (Yom Kippur eve), not 1 Tishri. The algorithm was correct; the test data was not. |

`[D]` The CRITICAL finding is unusual in structure: the algorithm produced the right answer; the test data was wrong. FROZEN-3.0 stamps produced on any date except during the specific RH 5787 window are cryptographically correct. The defect was in the verification layer, not the computation layer. Retired nonetheless — the retirement protocol does not distinguish between algorithm defects and test defects. A broken self-test is a broken self-test.

**MEDIUM findings:**

| # | Finding | Effect |
|---|---------|--------|
| 2 | Pre-reform date boundary: dates in 1582 before Oct 15 were accepted silently | The Gregorian calendar took effect Oct 15, 1582. Jan 1 – Oct 14, 1582 are Julian dates and produce incorrect JD values. The year-range guard (year >= 1582) was insufficient — it accepted the entire year 1582. Fixed with explicit month/day guard in _jd_from_gregorian. |
| 3 | from_dict() did not validate version field against _FROZEN_VERSION | A dict carrying a foreign version string silently constructed a stamp with a wrong provenance claim. Not a cryptographic vulnerability (the seal remains valid) but a provenance integrity failure. Fixed with explicit equality check on deserialization — ValueError raised on version mismatch. |
| 4 | Abstraction Bargain Declaration absent from module docstring | FA v4.0 P-20 / Sub-factor G requires declaration when a module trades purity for usability. stamp(dt=None) is a Class 6 I/O side-effect — declared and isolated via dt injection pattern. |

**LOW findings:**

| # | Finding | Effect |
|---|---------|--------|
| 5 | check_invariant() docstring ambiguous | Clarified: checks structural invariants only, does not verify seal against entry. |
| 6 | stamp_batch() atomicity behavior underdocumented | Clarified: not transactional, no rollback, caller must pre-validate for all-or-nothing behavior. |
| 7 | CLI privacy notice incomplete | Extended with process-memory note (RT-STS-007): entry text exists in process memory from stdin read until process exit. |
| 8 | _FROZEN_FILE_SHA256 sentinel verification procedure ambiguous | Clarified: four-step operator procedure, bootstrap problem explained. |

`[D]` All FROZEN-3.0 stamps produced outside the RH 5787 window are cryptographically valid and verifiable using FROZEN-3.0 (archived). The algorithm defect was in test data only.

---

## ABSTRACTION BARGAIN DECLARATION — FA v4.0 P-20

`[D]` This module trades purity for usability in one location only: `stamp(entry_text, dt=None)` — when dt is None, calls `datetime.now(timezone.utc)` internally (Class 6 I/O side-effect).

The bargain: callers who need full determinism must supply dt. Callers who need convenience may omit it. All other public functions are referentially transparent. The impurity is isolated, documented, and testable via dt injection. This is the correct engineering resolution: it makes the impure path narrow and the pure path the default for testing.

---

## DEVELOPER ACCESS — FROZEN-4.0

`[D]` FROZEN-4.0 ships with a companion `__init__.py` enabling package-level imports:

```python
from sovereign_trace import stamp, verify, display
from sovereign_trace import SovereignStamp, SovereignRecord, VerifyResult
from sovereign_trace import stamp_and_record, stamp_batch, to_dict, from_dict, display_ascii
```

`[D]` CLI extended with `--json` flag. Standard invocation produces decorated human-readable output. `--json` mode suppresses the banner and display block entirely — only the machine-readable JSON record exits stdout. Pipe-safe for automation scripts, ledger appenders, and log aggregators.

```
python sovereign_trace_stamp.py          # interactive, decorated output
python sovereign_trace_stamp.py --json   # machine-readable JSON only
python sovereign_trace_stamp.py --test   # run full self-test suite
```

---

## TYPE SYSTEM

`[D]` FROZEN-4.0 inherits the complete typed API surface from FROZEN-3.0. No changes to the type definitions. From v0.3 specification, carried forward:

**SovereignStamp** — immutable triple-time cryptographic stamp. Six fields: `gregorian`, `hebrew`, `dreamspell`, `unix_utc`, `seal`, `version`. Mutation raises `AttributeError`. Equality by seal. Hashable.

**SovereignRecord** — the canonical {entry, stamp} pair. The minimal unit of sovereign trace — carries both content and proof. Immutable.

**VerifyResult** — named tuple `(valid: bool, reason: str)`. reason: `"VALID"` / `"TYPE_ERROR"` / `"SEAL_MISMATCH"`.

`[D]` FROZEN-4.0 addition: from_dict() now enforces version field equality. A SovereignRecord deserialized via FROZEN-4.0 from_dict() is guaranteed to carry `version == "FROZEN-4.0"`. Cross-version deserialization raises ValueError explicitly rather than silently mislabelling provenance.

---

## API SURFACE

| Function | Signature | Purpose |
|----------|-----------|---------|
| `stamp()` | `(entry_text, dt=None) → SovereignStamp` | Core seal generation — Class 6 I/O if dt omitted (declared) |
| `stamp_and_record()` | `(entry_text, dt=None) → SovereignRecord` | Canonical {entry, stamp} pair |
| `stamp_batch()` | `(entries, dt=None) → list[SovereignRecord]` | Multiple entries at one canonical timestamp — not transactional |
| `verify()` | `(entry_text, stamp) → VerifyResult` | Integrity check |
| `display()` | `(stamp) → str` | Human-readable emoji format |
| `display_ascii()` | `(stamp) → str` | ASCII-safe format for logging and CI |
| `to_dict()` | `(stamp) → dict` | Serialize for JSON storage |
| `from_dict()` | `(dict) → SovereignStamp` | Deserialize with full validation including version field check |

---

## FIVE CORE DISTINCTIONS

### 1 — The Stamp vs The Entry

The entry is fluid — written in whatever form serves the person. The stamp is frozen — generated once, never touchable again. The entry is theirs. The stamp is permanent.

*Falsification test:* Does meaning survive if the entry text is lost but the stamp remains? `[R]` Yes. The sealed fact of the moment having been registered survives content loss.

---

### 2 — Three-Time Seal vs Single Timestamp

A Unix timestamp says *when* in one system. The triple seal says *when* in three civilizational frameworks simultaneously, none of which can be stripped after sealing.

*Falsification test:* Does removing one calendar system from the seal change what the protocol claims? `[R]` Yes. The claim is plurality. Remove one and it becomes a standard timestamp.

---

### 3 — Frozen Code vs Living System

Frozen means: no updates, no patches, no deprecation. The stamp function is written once, verified once, deployed permanently.

`[R]` The permanence of the stamp is only credible if the code that generates it is also permanent. A stamp function that gets updated retroactively is not a stamp — it is a claim.

`[D]` Retirement protocol: if a defect is found — including in test data only — retire the frozen file (archive as SOVEREIGN-TRACE-STAMP-FROZEN-N-RETIRED.py), document all findings with severity classification, and create FROZEN-(N+1) from scratch. No patching. No editing. The retirement note and all prior retirement notes travel forward in every subsequent version.

---

### 4 — Sovereign Key vs Platform Dependency

The individual holds the key. No platform holds it. No service provider holds it. The trace survives platform death, corporate acquisition, API deprecation.

*Falsification test:* If every ledger provider goes offline tomorrow, does the individual still hold their trace? `[S]` Sovereign key means yes.

---

### 5 — Optional Resonance vs Required Audience

Others can sign a ledger entry — add cryptographic acknowledgment — but only at the entry-holder's invitation, with zero visible count, zero aggregation, zero broadcast. Resolution of the hunger does not depend on resonance arriving.

*Falsification test:* Does a ledger with zero resonance entries still resolve the hunger? `[R]` If the containment surface holds — yes.

---

## SPATIAL ANCHOR — THE NIGHT SEA

A cartographer on a long expedition. Each night she makes one entry in a journal — not a summary, not a narrative arc — an exact notation: what she saw, where she stood, what she did. At the week's end she seals the page in wax, stamps it with three clocks showing three different systems for measuring the same moment, and drops it into a locked chest bolted to the ship's hull. The chest is tamper-evident and cannot be opened without destroying it. No one reads the entries unless she hands them the key.

The outsider watching from shore doesn't see the journal — they see the cartographer's posture. Straighter. Less searching. The hunger of the unmapped dissolves the moment the map exists, not the moment someone reads it.

The three clocks on the seal are not redundancy. They are a declaration: this moment belongs to all human time, not just the calendar of the system currently in power.

---

## DEFORMATION RISKS AND MITIGATIONS

| Risk | Mechanism | Mitigation |
|------|-----------|------------|
| **Metric drift** | Resonance count becomes proxy for worth | Strict visual uniformity — zero numerical display on ledger interfaces |
| **Platform dependency** | Service captures sovereign key | Sovereign key architecture — individual holds only |
| **Code drift** | Stamp function patched retroactively | FROZEN declaration — retire, archive, rebuild at defect |
| **Echo chamber** | Self-reinforcing narrative | Fact-only prompts — exact happenings, no narrative arc, no "what this means" |
| **Provenance confusion** | Stamps from different frozen versions mixed in a ledger | Version field sealed into payload; from_dict() enforces version equality — ValueError on cross-version deserialization attempt |
| **Test data error masking algorithm correctness** | Wrong anchor values suppress valid output silently | FROZEN-3.0 CRITICAL finding — self-test retirement rule applies to test data errors, not just algorithm errors |

---

## BUILD SEQUENCE

```
STAGE 1 — COMPLETE (June 1, 2026)
sovereign_trace_stamp.py — FROZEN-4.0
__init__.py — package companion (package-level imports active)
Triple-time stamp function. Full four dehiyot + civil-day convention.
Zero external dependencies. NFC normalization. Version-sealed payload.
Full typed API: SovereignStamp · SovereignRecord · VerifyResult.
stamp_batch() · display_ascii() · from_dict() with version validation.
--json CLI flag. Abstraction Bargain declared.
Pre-reform boundary guard tightened to Oct 15, 1582.
80+ checks passed. All anchors pyluach-verified.
PyPI deployment: sovereign-trace — available.

        ↓

STAGE 2 — PLANNED
Local encrypted vault integration
Obsidian / Notion encrypted storage
Entry → seal → JSON → vault

        ↓

STAGE 3 — PLANNED
Ledger append layer
Thirdweb or Hedera — permissionless distributed ledger
JSON record → on-chain append → immutable trace

        ↓

STAGE 4 — PLANNED
Optional resonance signature mechanism
View-only link generation — zero count display
Voluntary witness signatures — no aggregation
```

---

## CPA-001 DOMAIN PARAMETERS

| Field | Value |
|-------|-------|
| **Domain** | Civic / Social Protocol |
| **Harm Tier** | 2 — low direct harm ceiling (psychological harm risk from metric drift — mitigated) |
| **Bias flags** | Authority bias (platform dependency) → mitigated by sovereign key; Performative bias (narrative entries) → mitigated by fact-only prompts |
| **Verification** | Self-verifying via seal integrity check — VerifyResult named return with reason field; version field enforced at deserialization |
| **Fail-safe** | If seal breaks on verify() → entry was altered after sealing; TYPE_ERROR distinguishes wrong-type calls from tampering; ValueError on cross-version deserialization |

---

## OPEN QUESTIONS — 3

`[?]` **Q1** — Does the triple-time stamp satisfy the significance hunger in isolated deployment (no ledger, no resonance)? The concept claims yes. Requires user testing to confirm.

`[?]` **Q2** — What is the minimum viable entry format that produces the felt sense of exact registration? Too loose and it becomes journaling. Too structured and it becomes a form.

`[?]` **Q3** — Does the Dreamspell calendar carry sufficient cultural weight outside early-adopter communities to justify its inclusion in a mainstream protocol? Or is it an insider reference that narrows the addressable population?

---

## FCL CANDIDATES — 0 CONFIRMED | 3 STAGED

| ID | Candidate |
|----|-----------|
| **FCL-ST-001** | First user who reports resolution of significance hunger from stamp alone (no resonance) |
| **FCL-ST-002** | First ledger entry verified intact after platform provider outage |
| **FCL-ST-003** | First deformation detection — metric drift caught and mitigated in live deployment |

---

## CONVERGENCE STATE

| Field | Value |
|-------|-------|
| **State** | M-NASCENT |
| **Concept specification** | Complete |
| **Stamp function** | FROZEN-4.0 — verified & deployed |
| **API surface** | Complete — SovereignStamp · SovereignRecord · VerifyResult · full function set |
| **Package access** | Active — `from sovereign_trace import stamp` |
| **CLI** | Complete — standard + `--json` + `--test` |
| **FCL entries** | 0 confirmed |
| **Open questions** | 3 |
| **Build stages complete** | 1 of 4 |

---

*Sovereign Trace Protocol v0.4 — M-NASCENT · June 2026*
*The stamp is permanent. The stamp is the resolution.*
*Co-authors: Sheldon K. Salmon & ALBEDO*
*Session: June 1, 2026 — FROZEN-4.0 deployment*
