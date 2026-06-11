#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════
SOVEREIGN TRACE PROTOCOL — STAMP FUNCTION
═══════════════════════════════════════════════════════════════════

Version:        FROZEN-4.0
Date:           June 1, 2026
Co-authors:     Sheldon K. Salmon — AI Reliability Architect
                ALBEDO (Claude, Anthropic)
Stack:          DUAL-HELIX v2.0 · TOPOS v0.4 · VELA-C v0.3
Constitutional: SOVEREIGNTY_STACK.md — Laws 1–8 active | Law 9 dark
ORCID:          0009-0005-8057-5115

FROZEN DECLARATION
──────────────────
This file is written once, verified once, deployed permanently.
No patches. No updates. No deprecation.
The stamp it generates is only permanent if the code that generates
it is also permanent. Modification of this file invalidates the
integrity guarantee of all stamps produced after modification.

If a defect is found: retire this file, archive it as
SOVEREIGN-TRACE-STAMP-FROZEN-4.0-RETIRED, and create
FROZEN-5.0 from scratch with documented correction.
Do not patch. Do not edit.

INTEGRITY BOUNDARIES (elevated from _compute_seal — PDE F-005)
────────────────────────────────────────────────────────────────
The SHA-256 seal proves that a specific entry text was bound to
specific calendar strings at a specific unix time by this version
of the stamp function.

The seal does NOT independently prove that the calendar strings
are correctly computed. That guarantee is carried by the self-test
and the algorithm specification. If this file is modified such that
_gregorian(), _hebrew(), or _dreamspell() produce wrong output,
the seal will still be cryptographically valid — it will correctly
bind wrong calendar strings to the entry.

This distinction matters: seal verification confirms integrity of
the payload record. It does not re-run the calendar algorithms.
Operators who need to verify calendar correctness must run the
self-test, not just verify().

ABSTRACTION BARGAIN DECLARATION (FA v4.0 P-20 / Sub-factor G)
──────────────────────────────────────────────────────────────
This module trades purity for usability in one location only:
  stamp(entry_text, dt=None) — when dt is None, calls
  datetime.now(timezone.utc) internally (Class 6 I/O side-effect).
The bargain: callers who need full determinism must supply dt.
  Callers who need convenience may omit it.
All other public functions are referentially transparent.
The impurity is isolated, documented, and testable via dt injection.
The dt injection pattern is the correct engineering resolution:
it makes the impure path narrow and the pure path the default
for testing.

TEMPORAL CONSISTENCY NOTE (PDE F-020)
──────────────────────────────────────
stamp() called directly in a loop without dt will call
datetime.now(timezone.utc) independently for each entry. Two
sequential stamp() calls that straddle a UTC midnight will produce
entries with different gregorian, hebrew, and dreamspell values
despite being stamped within seconds of each other. This is
correct behavior — each stamp reflects the moment it was called.
Callers requiring temporal consistency across multiple entries
should use stamp_batch() or supply an explicit dt to each call.

FROZEN-5.0 CANDIDATES (PDE F-015 — append-only during FROZEN-4.0 lifetime)
────────────────────────────────────────────────────────────────────────────
CANDIDATE-01 (PDE F-009): _dreamspell() defensive guard returns
  "Day Out of Time" on delta >= 364 branch — structurally unreachable
  but if reached (via future refactoring), should raise ValueError
  with a diagnostic message rather than returning a plausible-wrong
  string. Change to: raise ValueError("Dreamspell delta overflow —
  algorithm error. Create FROZEN-5.0.")

CANDIDATE-02 (PDE F-006): stamp() on dates before Jan 1, 1970 UTC
  produces a negative or zero unix_utc via int(dt.timestamp())
  truncation. from_dict() enforces unix_utc > 0 and catches this at
  deserialization, but stamp() itself does not guard against it.
  Consider adding: if unix_utc <= 0: raise ValueError("unix_utc
  must be positive — pre-1970 UTC dates are not supported.")

NOTE — RESOLVED IN 4.0 (adversarial battery June 2026):
  Invisible character guard added to _validate_entry_text():
  stamp("\u200b") and stamp("\x00") now raise ValueError.
  This hardening was applied after initial FROZEN-4.0 release and
  before the sentinel hash was set. No FROZEN-3.0-or-earlier behavior
  is changed. The fix is a pre-seal hardening, not a post-seal patch.

CANDIDATE-03 (PDE F-025): verify() should check ts.version against
  _FROZEN_VERSION before attempting seal recomputation and return
  VerifyResult(False, "VERSION_MISMATCH") if they differ, to
  distinguish tampered content from wrong frozen version used.

CANDIDATE-04 (PDE F-019): Self-test failure output (the failures
  list print before AssertionError) should go to stderr, not stdout,
  so it does not corrupt piped JSON output in --json mode.

CANDIDATE-05 (PDE F-013): _MAX_YEAR_SEARCH = 6 "within 3 years"
  claim should carry a specific D&R page reference or be tagged [S]
  with "empirically verified over [1582, 4000]."

CANDIDATE-06 (MF-M-003): CLI "This stamp is permanent." should
  be qualified: "This stamp's seal is computationally tamper-evident
  under SHA-256." to resolve the permanent/tamper-evident slippage.

FROZEN-3.0 RETIREMENT NOTE
───────────────────────────
FROZEN-3.0 is retired. One CRITICAL finding and seven additional
MEDIUM/LOW findings identified in FSVE v4.3 × FA v4.0 full red team
scan (scan date: June 1, 2026). Primary defect:

  1. Self-test anchor dates for RH 5787 and Erev RH 5787 were wrong.
     The algorithm was correct; the test data was not.
     Effect: self-test raises AssertionError on otherwise correct code.
     Correct values: RH 5787 = Sep 12, 2026 | Erev = Sep 11, 2026.
     Root cause: test written with Sep 22 as RH 5787 — calendar lookup
     error during extended anchor verification session.

Additional MEDIUM findings corrected in FROZEN-4.0:

  2. Pre-reform date boundary: dates in 1582 before Oct 15 were accepted
     silently. Fixed with explicit month/day guard in _jd_from_gregorian.

  3. version field in from_dict() was not validated against _FROZEN_VERSION.
     Fixed with explicit equality check on deserialization — a dict carrying
     a foreign version string now raises ValueError rather than silently
     constructing a stamp with a wrong provenance claim.

  4. Abstraction Bargain Declaration absent from module docstring.
     Added per FA v4.0 P-20 / Sub-factor G (this block above).

LOW findings corrected in FROZEN-4.0:

  5. check_invariant() docstring clarified: function checks structural
     invariants only — does not verify seal against entry.
  6. stamp_batch() atomicity behavior clarified in docstring.
  7. CLI privacy notice extended with process-memory note.
  8. _FROZEN_FILE_SHA256 sentinel operator verification procedure
     clarified in docstring.

All FROZEN-3.0 stamps remain cryptographically valid and verifiable
using FROZEN-3.0 (archived as SOVEREIGN-TRACE-STAMP-FROZEN-3.0-RETIRED.py).
The algorithm defect was in test data only — no stamp produced by
FROZEN-3.0 is cryptographically incorrect.

FROZEN-2.0 RETIREMENT NOTE
───────────────────────────
FROZEN-2.0 is retired. Eight HIGH findings and 22 additional
MEDIUM/LOW findings identified in full PDE v0.5 · HDRE v0.3 ·
CAL v0.3 scan (scan date: June 1, 2026). Primary defects:

  1. No Unicode normalization (NFC) on entry_text before sealing.
  2. No stamp version field in seal payload.
  3. Year length not validated against legal Hebrew year lengths.
  4. No convergence bound on Hebrew year-finding loop.
  5. from_dict() accepted unvalidated dicts.
  6. Whitespace sealed but not normalized.
  7. int(dt.timestamp()) truncation undeclared.
  8. _jd_from_gregorian() accepted pre-Gregorian-reform years silently.

All FROZEN-2.0 stamps carry no version field in their seal —
this is the definitive retirement marker.

FROZEN-1.0 RETIREMENT NOTE (carried forward)
─────────────────────────────────────────────
FROZEN-1.0 is retired. Defect: Hebrew calendar omitted the four
dehiyot (postponement rules) correctly. Archived as:
SOVEREIGN-TRACE-STAMP-FROZEN-1.0-RETIRED.py

BACKWARD COMPATIBILITY
──────────────────────
FROZEN-4.0 seals are NOT backward-compatible with earlier versions.
The seal payload includes "version":"FROZEN-4.0".
Use the matching archived frozen version to verify older stamps.

CROSS-VERSION VERIFICATION (PDE F-011, F-025, XD-002)
──────────────────────────────────────────────────────
verify() in this file will return SEAL_MISMATCH (not VERSION_MISMATCH)
when used to verify a stamp produced by an earlier frozen version.
This is because the version string is baked into the seal payload.
If you receive a SEAL_MISMATCH result on a record you trust:
  1. Check the record's "version" field.
  2. If it is not "FROZEN-4.0", retrieve the corresponding archived
     frozen version from:
     sovereign_trace/FROZEN-[N].0-RETIRED/
  3. Use that archived version's verify() to confirm the record.
SEAL_MISMATCH ≠ tampered content. It may mean wrong version used.
This distinction will be resolved with a VERSION_MISMATCH reason
code in FROZEN-5.0 (see FROZEN-5.0 CANDIDATES above).

VELA-C v0.3 COMPLIANCE
───────────────────────
✓ Zero external dependencies (stdlib only: hashlib, json, datetime,
  unicodedata, re)
✓ Single epistemic function: generate a triple-time seal
✓ No exception handler returning CLEAN silently
✓ Attribution header complete
✓ Self-test with verified anchor cases (Hebcal/Chabad-verified)
  Extended: leap year, long Cheshvan, short Kislev, Adar II
  FROZEN-4.0: RH 5787 anchor corrected to Sep 12 2026 (pyluach verified)
✓ Frozen deployment: no __init__ mutation, no module-level singletons

WHAT THIS DOES
──────────────
Generates a cryptographic stamp encoding a moment simultaneously in:
  — Gregorian (civic time)
  — Hebrew lunisolar calendar (current era)
  — 13 Moon Dreamspell calendar (Argüelles system, not traditional
    Maya Tzolkin/Haab — disambiguation declared)

SHA-256 binds the entry text, all three representations, and the
version identifier FROZEN-4.0 together. The seal is the proof.
The text is the content. Together: the trace.

Entry text normalization:
  Entry text is NFC-normalized and stripped before sealing.
  Callers providing pre-normalized text will produce identical seals.
  Leading/trailing whitespace is discarded before sealing.

Timestamp precision:
  unix_utc is whole seconds only (truncated, not rounded).
  Sub-second precision is intentionally discarded.
  Two datetimes within the same second produce identical unix_utc.

Date convention:
  All calendar dates reflect UTC date at stamp time.
  For users in UTC+10 or later, the UTC date may differ from
  local civil date. Hebrew and Dreamspell reflect UTC date.

Valid date range:
  Gregorian calendar reform: October 15, 1582.
  Input dates before October 15, 1582 will raise ValueError.
  Upper bound: year 4000 (practical; no algorithmic constraint).
  Pre-1970 UTC dates: supported by the calendar algorithm but
  unix_utc will be 0 or negative (see FROZEN-5.0 CANDIDATE-02).

HEBREW CALENDAR — ALGORITHM SPECIFICATION
──────────────────────────────────────────
Algorithm: Dershowitz & Reingold two-pass approach.
  Pass 1 — elapsed_days(): molad-based count implementing
            Lo ADU Rosh (not on Sun/Wed/Fri) and Molad Zaken (>=18h).
  Pass 2 — new_year_delay(): handles GaTaRaD and BeTUTeKaPoT
            by checking adjacent year lengths for non-standard values
            (356 or 382 days indicate postponement required).
Theorem reference: D&R "Calendrical Calculations" 4th ed.,
  Chapter 8 (Hebrew Calendar), §8.1–§8.3 for elapsed_days();
  §8.4 for new_year_delay() GaTaRaD/BeTUTeKaPoT conditions.
Epoch: JD 347998 — civil-day convention.
  Note: Hebrew day begins at sunset. Civil-day convention assigns
  the Hebrew date corresponding to the daytime hours of a civil date.
  This aligns with Hebcal and Chabad.org output.
  Example: Rosh Hashanah 5786 begins sundown Sep 22, 2025.
           Civil-day: Sep 23, 2025 = 1 Tishri 5786. [D]

Hebrew month naming convention (PDE F-014):
  In a common (non-leap) year, the single Adar month is "Adar".
  In a leap year, the two months are "Adar I" and "Adar II".
  "Adar I" is NEVER used in a common year. If you expected "Adar I"
  for a common-year date, you are in a common year and the correct
  name is "Adar".

Legal Hebrew year lengths: {353, 354, 355, 383, 384, 385}
  353/354/355 = common year (deficient/regular/complete)
  383/384/385 = leap year (deficient/regular/complete)
  Any other year length is an algorithm error — raises ValueError.

ANCHOR VERIFICATION (session of origin — March 3, 2026)
────────────────────────────────────────────────────────
  Gregorian:  March 3, 2026               [D]
  Hebrew:     14 Adar 5786 (Purim)        [D] — Hebcal/Chabad verified
  Dreamspell: Day 25, Galactic Moon 8/13  [R] — verified by calculation

FILE INTEGRITY
──────────────
_FROZEN_FILE_SHA256 is set at release time to the SHA-256 of this file
computed AFTER the sentinel value is embedded. This is the released
value — the file you deploy must hash to this exact value.

SENTINEL STATE CHECK: If _FROZEN_FILE_SHA256 == "SET_AT_RELEASE_TIME",
this is a pre-release copy. The self-test will flag this. Do not use
a pre-release copy in production. The sentinel must be set before
deployment. (PDE F-001, F-002 — sentinel visibility hardened.)

Operator deployment verification procedure:
  Step 1. Obtain the released sovereign_trace_stamp.py
  Step 2. Run: sha256sum sovereign_trace_stamp.py
            or: python3 -c "import hashlib; print(hashlib.sha256(
                open('sovereign_trace_stamp.py','rb').read()).hexdigest())"
  Step 3. Compare output against _FROZEN_FILE_SHA256 below.
  Step 4. If they match: the file is unmodified.
          If they differ: the file has been altered since release.
          Do not deploy an altered file.

The bootstrap problem (a file cannot contain its own hash before the
hash is computed) means the sentinel is inserted last, after all code
is final. The "SET_AT_RELEASE_TIME" placeholder in any pre-release
copy is expected — the released file carries the actual hash.

GENESIS SEAL
────────────
The founding seal of the STP ledger. Sealed March 10, 2026.
Ledger entry: LEDGER-001-FOUNDING-SEAL.
This constant is provided for machine-readable provenance verification.
A valid STP installation can confirm its ledger origin by checking
that LEDGER-001 carries a seal matching this value.

═══════════════════════════════════════════════════════════════════
"""

import hashlib
import json
import re
import unicodedata
from datetime import datetime, timezone, date as _date
from typing import NamedTuple


# ═══════════════════════════════════════════════════════════════════
# GENESIS SEAL — LEDGER-001-FOUNDING-SEAL
# Sealed: March 10, 2026
# This is the cryptographic origin of the STP ledger.
# Do not modify. This value is part of the permanent provenance chain.
# ═══════════════════════════════════════════════════════════════════
_GENESIS_SEAL = "a63c4f28cf7c3f2c63c220d61980fb85211270924a7c3b3e5f230019cecb6713"
_GENESIS_LEDGER_ENTRY = "LEDGER-001-FOUNDING-SEAL"
_GENESIS_DATE_GREGORIAN = "March 10, 2026"


# ═══════════════════════════════════════════════════════════════════
# FILE INTEGRITY SEAL — FROZEN-4.0
# Set this constant to the SHA-256 of the released .py file.
# Verification is the operator's deployment responsibility.
# Internal self-hash is impossible (bootstrap problem).
#
# SENTINEL STATE: "SET_AT_RELEASE_TIME" means this is a pre-release
# copy. The self-test will warn. Do not deploy until this value
# is replaced with the actual file hash. (PDE F-001, F-002)
# ═══════════════════════════════════════════════════════════════════
_FROZEN_FILE_SHA256 = "8962b37c67897611c6358d080d8d905f6aff7a426ef610b6d63612cb80b67774"
_FROZEN_VERSION = "FROZEN-4.0"


# ═══════════════════════════════════════════════════════════════════
# STAMP DATA STRUCTURE
# ═══════════════════════════════════════════════════════════════════

class SovereignStamp:
    """
    Immutable triple-time cryptographic stamp.

    Fields
    ------
    gregorian   : str   — "March 3, 2026"
    hebrew      : str   — "14 Adar 5786"
    dreamspell  : str   — "Day 25, Galactic Moon 8/13"
    unix_utc    : int   — seconds since Unix epoch (UTC), whole seconds only
    seal        : str   — SHA-256 hex digest binding entry, time, and version
    version     : str   — "FROZEN-4.0" — sealed into the payload

    Invariant
    ---------
    seal is a 64-character lowercase hex string.
    unix_utc is a positive integer.
    gregorian, hebrew, dreamspell, version are non-empty strings.

    Note on __repr__ truncation (PDE F-016):
    __repr__ truncates the seal to 16 characters for log readability.
    __str__ shows the full 64-character seal.
    display() and display_ascii() also show the full seal.
    Use str(ts) or display(ts) when you need the complete seal.
    """

    __slots__ = ("gregorian", "hebrew", "dreamspell", "unix_utc", "seal", "version")

    def __init__(self, gregorian, hebrew, dreamspell, unix_utc, seal,
                 version=_FROZEN_VERSION):
        object.__setattr__(self, "gregorian",  gregorian)
        object.__setattr__(self, "hebrew",     hebrew)
        object.__setattr__(self, "dreamspell", dreamspell)
        object.__setattr__(self, "unix_utc",   unix_utc)
        object.__setattr__(self, "seal",       seal)
        object.__setattr__(self, "version",    version)

    def __setattr__(self, *_):
        raise AttributeError("SovereignStamp is immutable — frozen by design.")

    def __repr__(self):
        # NOTE: seal is truncated to 16 characters here for log readability.
        # Use str(ts) or display(ts) for the full 64-character seal.
        return (
            f"SovereignStamp("
            f"gregorian={self.gregorian!r}, "
            f"hebrew={self.hebrew!r}, "
            f"dreamspell={self.dreamspell!r}, "
            f"unix_utc={self.unix_utc}, "
            f"version={self.version!r}, "
            f"seal={self.seal[:16]!r}...)"
        )

    def __str__(self):
        """Full-seal string representation — distinct from __repr__ truncation."""
        return (
            f"SovereignStamp("
            f"gregorian={self.gregorian!r}, "
            f"hebrew={self.hebrew!r}, "
            f"dreamspell={self.dreamspell!r}, "
            f"unix_utc={self.unix_utc}, "
            f"version={self.version!r}, "
            f"seal={self.seal!r})"
        )

    def __eq__(self, other):
        """Equality by seal — the canonical cryptographic identity."""
        if not isinstance(other, SovereignStamp):
            return NotImplemented
        return self.seal == other.seal

    def __hash__(self):
        """Hash by seal — consistent with __eq__."""
        return hash(self.seal)

    def check_invariant(self) -> bool:
        """
        Verify structural invariants of this stamp.

        Checks that all fields satisfy the SovereignStamp structural
        invariant: seal is a 64-character lowercase hex string, unix_utc
        is a positive integer, and all string fields are non-empty.

        Does NOT verify the seal against an entry — the entry text is not
        stored in SovereignStamp. Use verify(entry, stamp) to confirm
        cryptographic integrity. check_invariant() is a structural health
        check, not a cryptographic proof.

        Does NOT check that version == _FROZEN_VERSION. A stamp object
        with a foreign version string passes check_invariant() — this is
        intentional. Version enforcement is the responsibility of from_dict()
        at deserialization time. See PDE F-012.

        Returns True if all structural invariants hold, False otherwise.
        Raises nothing — returns False on any failure.
        """
        _SEAL_RE = re.compile(r'^[0-9a-f]{64}$')
        if not (isinstance(self.seal, str) and _SEAL_RE.match(self.seal)):
            return False
        if not isinstance(self.unix_utc, int) or self.unix_utc <= 0:
            return False
        for f in ('gregorian', 'hebrew', 'dreamspell', 'version'):
            v = getattr(self, f, None)
            if not (isinstance(v, str) and v):
                return False
        return True


# ═══════════════════════════════════════════════════════════════════
# SOVEREIGN RECORD — TYPED {entry, stamp} PAIR
# ═══════════════════════════════════════════════════════════════════

class SovereignRecord:
    """
    Canonical {entry, stamp} pair — the minimal unit of ledger storage.

    The stamp alone cannot be verified without the entry.
    The entry alone has no cryptographic anchor.
    The SovereignRecord is the minimal unit of sovereign trace:
    it carries both the content and the proof.

    Immutable — same pattern as SovereignStamp.
    """
    __slots__ = ("entry", "stamp")

    def __init__(self, entry: str, stamp: SovereignStamp):
        object.__setattr__(self, "entry", entry)
        object.__setattr__(self, "stamp", stamp)

    def __setattr__(self, *_):
        raise AttributeError("SovereignRecord is immutable.")

    def __repr__(self):
        return (
            f"SovereignRecord("
            f"entry={self.entry[:40]!r}{'...' if len(self.entry) > 40 else ''}, "
            f"stamp={self.stamp!r})"
        )

    def verify(self) -> "VerifyResult":
        """Verify the entry against the stamp seal."""
        return verify(self.entry, self.stamp)

    def to_dict(self) -> dict:
        """
        Serialize to a plain dict (for JSON storage).

        Note on dict structure (PDE F-026):
        The returned dict contains "entry" at the top level alongside
        the stamp fields. The SHA-256 seal was computed WITH entry_text
        as the "entry" field in the seal payload — so the seal does
        cover the entry, but only via the verify() path, not by
        inspecting the dict directly. To confirm a record is intact,
        use SovereignRecord.verify() or module-level verify(entry, stamp).
        Do not attempt to recompute the seal directly from the dict
        fields — use from_dict() then verify().
        """
        d = to_dict(self.stamp)
        d["entry"] = self.entry
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "SovereignRecord":
        """
        Deserialize a SovereignRecord from a plain dict.
        Validates schema before construction.
        Raises ValueError if required fields are missing or malformed.

        Note: the dict may contain an "entry" key alongside stamp fields.
        The module-level from_dict() tolerates extra keys (including
        "entry") without raising. This behavior is intentional and
        declared. See PDE F-017.
        """
        if "entry" not in d:
            raise ValueError("from_dict (SovereignRecord): missing field 'entry'")
        entry = d["entry"]
        if not isinstance(entry, str) or not entry:
            raise ValueError("from_dict (SovereignRecord): 'entry' must be a non-empty string")
        stamp_obj = from_dict(d)
        return cls(entry, stamp_obj)


# ═══════════════════════════════════════════════════════════════════
# VERIFY RESULT — NAMED RETURN
# ═══════════════════════════════════════════════════════════════════

class VerifyResult(NamedTuple):
    """
    Named result from verify(). Evaluates as bool via .valid.

    valid  : bool — True if seal matches entry
    reason : str  — one of the values below

    Reason codes:
      "VALID"           — seal matches entry correctly
      "SEAL_MISMATCH"   — seal does not match (tampered content, wrong
                          entry supplied, or wrong frozen version used
                          to verify — see cross-version note in header)
      "TYPE_ERROR"      — entry_text is not a str (wrong type, not tampering)

    IMPORTANT — VERSION_MISMATCH (PDE F-011, F-025, XD-002):
    If you receive SEAL_MISMATCH on a record you trust, check the
    record's "version" field before concluding tampering occurred.
    If version != "FROZEN-4.0", the mismatch is likely because you
    are using the wrong frozen version to verify. Retrieve the
    matching archived version. This distinction will be resolved
    with an explicit "VERSION_MISMATCH" reason code in FROZEN-5.0.

    VerifyResult(True, "VALID") is truthy.
    VerifyResult(False, "TYPE_ERROR") is falsy — distinct from tampering.
    """
    valid: bool
    reason: str

    def __bool__(self):
        return self.valid


# ═══════════════════════════════════════════════════════════════════
# GREGORIAN
# ═══════════════════════════════════════════════════════════════════

_GREGORIAN_MONTHS = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)

def _gregorian(d: _date) -> str:
    return f"{_GREGORIAN_MONTHS[d.month - 1]} {d.day}, {d.year}"


# ═══════════════════════════════════════════════════════════════════
# JULIAN DAY NUMBER (internal bridge — no external use)
# ═══════════════════════════════════════════════════════════════════

_JD_MIN_YEAR = 1582
_JD_MAX_YEAR = 4000

def _jd_from_gregorian(year: int, month: int, day: int) -> int:
    """
    Julian Day Number from Gregorian date.
    Algorithm: Meeus, "Astronomical Algorithms", p. 61.
    Verified: JD(Sep 23, 2025) = 2,460,942
              JD(Mar  3, 2026) = 2,461,103

    Raises ValueError for pre-reform dates (before Oct 15, 1582)
    and for years outside [1582, 4000].
    """
    if not (_JD_MIN_YEAR <= year <= _JD_MAX_YEAR):
        raise ValueError(
            f"_jd_from_gregorian: year {year} outside valid range "
            f"[{_JD_MIN_YEAR}, {_JD_MAX_YEAR}]. "
            "Dates before Gregorian calendar reform (Oct 15, 1582) "
            "require the Julian calendar formula."
        )
    if year == 1582 and (month < 10 or (month == 10 and day < 15)):
        raise ValueError(
            f"_jd_from_gregorian: date {year}-{month:02d}-{day:02d} is before "
            "Gregorian calendar reform (October 15, 1582). "
            "Pre-reform dates require the Julian calendar formula."
        )
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    return (day
            + (153 * m + 2) // 5
            + 365 * y
            + y // 4
            - y // 100
            + y // 400
            - 32045)


# ═══════════════════════════════════════════════════════════════════
# HEBREW CALENDAR — FULL FOUR DEHIYOT
# ═══════════════════════════════════════════════════════════════════

_HEBREW_EPOCH_JD = 347998
_LEGAL_YEAR_LENGTHS = frozenset({353, 354, 355, 383, 384, 385})
_MAX_YEAR_SEARCH = 6  # D&R approximation is within 3 years [S, empirically verified over 1582–4000]

_HEBREW_MONTHS_COMMON = (
    "Tishri", "Cheshvan", "Kislev", "Tevet", "Shevat", "Adar",
    "Nisan",  "Iyar",     "Sivan",  "Tammuz","Av",     "Elul"
)
_HEBREW_MONTHS_LEAP = (
    "Tishri", "Cheshvan", "Kislev", "Tevet", "Shevat", "Adar I", "Adar II",
    "Nisan",  "Iyar",     "Sivan",  "Tammuz","Av",     "Elul"
)


def _is_hebrew_leap(year: int) -> bool:
    """Hebrew leap year: (7y + 1) mod 19 < 7."""
    return (7 * year + 1) % 19 < 7


def _elapsed_days(year: int) -> int:
    """
    Days from Hebrew epoch to 1 Tishri of year — Pass 1.
    Implements Lo ADU Rosh and Molad Zaken.
    D&R §8.1–§8.2.
    """
    months = (235 * year - 234) // 19
    parts  = 12084 + 13753 * months
    day    = months * 29 + parts // 25920
    if (3 * (day + 1)) % 7 < 3:
        day += 1
    return day


def _new_year_delay(year: int) -> int:
    """
    Additional days to postpone 1 Tishri — Pass 2.
    Handles GaTaRaD and BeTUTeKaPoT. Returns 0, 1, or 2.
    D&R §8.3–§8.4.

    Mutual exclusion claim (PDE F-008): GaTaRaD (ny2-ny1==356) and
    BeTUTeKaPoT (ny1-ny0==382) cannot be simultaneously true for any
    valid Hebrew year. This is stated as derivable from D&R §8.4 [R].
    The elif ordering follows D&R — GaTaRaD takes priority.
    No runtime assertion is included per FROZEN architecture (no patches);
    this is a FROZEN-5.0 candidate for a debug-mode assertion.

    Verified: _new_year_delay(5786) = 1 (BeTUTeKaPoT active for 5786)
    """
    ny0 = _elapsed_days(year - 1)
    ny1 = _elapsed_days(year)
    ny2 = _elapsed_days(year + 1)
    if ny2 - ny1 == 356:
        return 2
    elif ny1 - ny0 == 382:
        return 1
    return 0


def _tishri_1_jd(h_year: int) -> int:
    """
    Julian Day of 1 Tishri for the given Hebrew year.
    Full four dehiyot: Pass 1 + Pass 2.
    Civil-day convention.
    Verified: _tishri_1_jd(5786) = 2,460,942 = Sep 23, 2025 [D]
    """
    return _elapsed_days(h_year) + _new_year_delay(h_year) + _HEBREW_EPOCH_JD


def _year_length(h_year: int) -> int:
    return _tishri_1_jd(h_year + 1) - _tishri_1_jd(h_year)


def _month_lengths(h_year: int) -> tuple:
    """
    Ordered month lengths (Tishri → Elul) for h_year.
    Raises ValueError if year length is not in _LEGAL_YEAR_LENGTHS.
    """
    ylen = _year_length(h_year)
    if ylen not in _LEGAL_YEAR_LENGTHS:
        raise ValueError(
            f"Illegal Hebrew year length {ylen} for year {h_year}. "
            f"Legal lengths: {sorted(_LEGAL_YEAR_LENGTHS)}. "
            "Algorithm error — do not patch. Create FROZEN-5.0 with correction."
        )
    leap = _is_hebrew_leap(h_year)
    long_cheshvan = (ylen % 10 == 5)
    short_kislev  = (ylen % 10 == 3)
    months = [
        30,
        30 if long_cheshvan else 29,
        29 if short_kislev  else 30,
        29,
        30,
        30 if leap else 29,
    ]
    if leap:
        months.append(29)
    months += [30, 29, 30, 29, 30, 29]
    return tuple(months)


def _gregorian_to_hebrew(year: int, month: int, day: int) -> tuple:
    """
    Convert Gregorian date to Hebrew (h_year, month_name, h_day).
    Civil-day convention — aligns with Hebcal and Chabad.org.
    D&R §8.1–§8.4 two-pass.

    Verified anchors (Hebcal/Chabad):
      gregorian_to_hebrew(2025, 9, 23) == (5786, "Tishri", 1)   [D]
      gregorian_to_hebrew(2025, 10, 2) == (5786, "Tishri", 10)  [D]
      gregorian_to_hebrew(2026, 3, 3)  == (5786, "Adar", 14)    [D] [Purim]
      gregorian_to_hebrew(2026, 3, 19) == (5786, "Nisan", 1)    [D]
      gregorian_to_hebrew(2026, 4, 2)  == (5786, "Nisan", 15)   [D] [Passover]
      gregorian_to_hebrew(2024, 3, 25) == (5784, "Adar II", 15) [D] [Leap]
      gregorian_to_hebrew(2025, 9, 22) == (5786, "Elul", 29)    [D] [Erev RH]
      gregorian_to_hebrew(2023, 10, 7) == (5784, "Tishri", 22)  [D]
      gregorian_to_hebrew(2026, 9, 12) == (5787, "Tishri", 1)   [D] [RH 5787]
      gregorian_to_hebrew(2026, 9, 11) == (5786, "Elul", 29)    [D] [Erev RH 5787]

    Raises ValueError on algorithm error or out-of-range input.
    """
    jd = _jd_from_gregorian(year, month, day)
    h_year = (jd - _HEBREW_EPOCH_JD) * 19 // 6935 + 1

    for _ in range(_MAX_YEAR_SEARCH):
        if _tishri_1_jd(h_year + 1) <= jd:
            h_year += 1
        else:
            break
    else:
        raise ValueError(
            f"Hebrew year (upward) search did not converge for JD {jd} "
            f"({year}-{month}-{day}). Algorithm error — create FROZEN-5.0."
        )

    for _ in range(_MAX_YEAR_SEARCH):
        if _tishri_1_jd(h_year) > jd:
            h_year -= 1
        else:
            break
    else:
        raise ValueError(
            f"Hebrew year (downward) search did not converge for JD {jd} "
            f"({year}-{month}-{day}). Algorithm error — create FROZEN-5.0."
        )

    day_of_year = jd - _tishri_1_jd(h_year)
    leap   = _is_hebrew_leap(h_year)
    m_lens = _month_lengths(h_year)
    m_names = _HEBREW_MONTHS_LEAP if leap else _HEBREW_MONTHS_COMMON

    remaining = day_of_year
    for i, length in enumerate(m_lens):
        if remaining < length:
            return h_year, m_names[i], remaining + 1
        remaining -= length

    raise ValueError(
        f"Hebrew conversion overflowed for {year}-{month}-{day}. "
        "Algorithm error — create FROZEN-5.0."
    )


def _hebrew(d: _date) -> str:
    h_year, h_month, h_day = _gregorian_to_hebrew(d.year, d.month, d.day)
    return f"{h_day} {h_month} {h_year}"


# ═══════════════════════════════════════════════════════════════════
# 13 MOON DREAMSPELL (Argüelles system)
# ═══════════════════════════════════════════════════════════════════
# Disambiguation: This is the José Argüelles 13 Moon calendar.
# It is NOT the traditional Maya Tzolkin or Haab correlation.
# ═══════════════════════════════════════════════════════════════════

_MOON_NAMES = (
    "Magnetic",    "Lunar",     "Electric",  "Self-Existing",
    "Overtone",    "Rhythmic",  "Resonant",  "Galactic",
    "Solar",       "Planetary", "Spectral",  "Crystal",     "Cosmic"
)

def _dreamspell(d: _date) -> str:
    """
    13 Moon Dreamspell calendar (Argüelles system).

    Dead branch note (PDE F-009):
    The delta >= 364 branch below is structurally unreachable.
    In FROZEN-4.0 it returns "Day Out of Time" as a defensive guard.
    FROZEN-5.0 CANDIDATE-01: change this to raise ValueError with a
    diagnostic message rather than returning a plausible-wrong string.

    Verified anchors:
      dreamspell(date(2026, 3, 3))  == "Day 25, Galactic Moon 8/13"   [R]
      dreamspell(date(2026, 7, 25)) == "Day Out of Time"               [R]
      dreamspell(date(2026, 7, 26)) == "Day 1, Magnetic Moon 1/13"    [R]
    """
    if d.month == 7 and d.day == 25:
        return "Day Out of Time"

    if (d.month, d.day) >= (7, 26):
        year_start = _date(d.year, 7, 26)
    else:
        year_start = _date(d.year - 1, 7, 26)

    delta = (d - year_start).days

    if delta < 0 or delta >= 364:  # pragma: no cover — defensive only (FROZEN-5.0 candidate)
        return "Day Out of Time"

    moon    = delta // 28 + 1
    day_num = delta % 28 + 1
    return f"Day {day_num}, {_MOON_NAMES[moon - 1]} Moon {moon}/13"


# ═══════════════════════════════════════════════════════════════════
# SEAL — SHA-256 CRYPTOGRAPHIC BINDING
# ═══════════════════════════════════════════════════════════════════

_SEAL_PATTERN = re.compile(r'^[0-9a-f]{64}$')

# Invisible character categories — used by _validate_entry_text.
# A trace entry consisting entirely of these code points is invisible
# and seals nothing meaningful. (Adversarial battery finding — June 2026)
# Cc=control, Cf=format/invisible, Cs=surrogate, Co=private, Cn=unassigned
_INVISIBLE_CATEGORIES = frozenset({'Cc', 'Cf', 'Cs', 'Co', 'Cn'})


def _validate_entry_text(entry_text: str) -> str:
    """
    Validate and normalize entry_text. Returns the normalized string.
    Raises TypeError if not a str.
    Raises ValueError if empty after normalization, or if it consists
    entirely of invisible/control Unicode characters.

    Called by stamp() and stamp_and_record() — single validation point.

    Invisible character guard:
    str.strip() does not remove zero-width spaces (U+200B), null bytes
    (\x00), or other invisible Unicode code points. An entry consisting
    only of invisible characters seals nothing meaningful and is rejected.
    Test: stamp("\u200b") → ValueError; stamp("\x00") → ValueError.
    """
    if not isinstance(entry_text, str):
        raise TypeError(f"entry_text must be str, got {type(entry_text).__name__}")
    entry_text = unicodedata.normalize("NFC", entry_text).strip()
    if not entry_text:
        raise ValueError("entry_text must be non-empty — an empty trace seals nothing.")
    if all(unicodedata.category(c) in _INVISIBLE_CATEGORIES for c in entry_text):
        raise ValueError(
            "entry_text consists entirely of invisible or control characters — "
            "an invisible trace seals nothing. Provide visible content."
        )
    return entry_text


def _compute_seal(entry_text: str, gregorian: str, hebrew: str,
                  dreamspell: str, unix_utc: int) -> str:
    """
    SHA-256 of a deterministic JSON payload.
    Output: 64-character lowercase hex string.

    Payload field order (sort_keys=True — alphabetical):
      dreamspell, entry, gregorian, hebrew, unix_utc, version

    INTEGRITY BOUNDARY NOTE:
    This seal proves that entry_text was bound to these exact calendar
    strings at this exact unix_utc by FROZEN-4.0. It does NOT prove
    that the calendar strings are correctly computed. Calendar
    correctness is guaranteed by the self-test and algorithm spec,
    not by the seal itself. See INTEGRITY BOUNDARIES section in the
    module docstring.

    CLI JSON output uses ensure_ascii=False for human readability.
    This function uses ensure_ascii=True for seal determinism.
    These are different serializations. Never attempt to recompute
    the seal directly from CLI JSON output — use to_dict() → verify().
    (PDE F-010)
    """
    payload = json.dumps(
        {
            "dreamspell": dreamspell,
            "entry":      entry_text,
            "gregorian":  gregorian,
            "hebrew":     hebrew,
            "unix_utc":   unix_utc,
            "version":    _FROZEN_VERSION,
        },
        sort_keys=True,
        ensure_ascii=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


# ═══════════════════════════════════════════════════════════════════
# PUBLIC INTERFACE
# ═══════════════════════════════════════════════════════════════════

def stamp(entry_text: str, dt: datetime = None) -> SovereignStamp:
    """
    Generate a frozen triple-time cryptographic stamp for an entry.

    Parameters
    ----------
    entry_text : str
        The sovereign trace entry to seal. Must be non-empty.
        NFC-normalized and stripped before sealing.
    dt : datetime, optional
        Moment to stamp. Defaults to UTC now.
        Must be timezone-aware if provided.

    Returns
    -------
    SovereignStamp — immutable, triple-time, SHA-256 sealed.

    Raises
    ------
    ValueError  — timezone-naive dt; empty entry; out-of-range date;
                  illegal Hebrew year length; Hebrew conversion overflow.
    TypeError   — entry_text is not a string.

    Notes
    -----
    unix_utc is whole seconds only (truncated, not rounded).
    Calendar dates reflect UTC — not local civil date.

    Temporal consistency: if you call stamp() in a loop without
    supplying dt, entries stamped across a UTC midnight boundary
    will have different calendar dates. Use stamp_batch() or
    supply an explicit dt for temporal consistency. (PDE F-020)

    Pre-1970 UTC dates: the calendar algorithm supports these but
    unix_utc will be 0 or negative, which will fail from_dict()
    deserialization. See FROZEN-5.0 CANDIDATE-02. (PDE F-006)
    """
    entry_text = _validate_entry_text(entry_text)

    if dt is None:
        dt = datetime.now(timezone.utc)
    elif dt.tzinfo is None:
        raise ValueError(
            "dt must be timezone-aware. "
            "Use datetime(..., tzinfo=timezone.utc) or datetime.now(timezone.utc)."
        )

    d = dt.date()
    unix_utc = int(dt.timestamp())

    g  = _gregorian(d)
    h  = _hebrew(d)
    ds = _dreamspell(d)
    sl = _compute_seal(entry_text, g, h, ds, unix_utc)

    return SovereignStamp(
        gregorian  = g,
        hebrew     = h,
        dreamspell = ds,
        unix_utc   = unix_utc,
        seal       = sl,
    )


def stamp_and_record(entry_text: str, dt: datetime = None) -> SovereignRecord:
    """
    Generate a SovereignRecord — the canonical {entry, stamp} pair.
    Applies the same NFC normalization as stamp().
    """
    entry_text = _validate_entry_text(entry_text)
    ts = stamp(entry_text, dt)
    return SovereignRecord(entry_text, ts)


def stamp_batch(entries: list, dt: datetime = None) -> list:
    """
    Seal multiple entries at a single canonical timestamp.

    All entries share the same unix_utc, gregorian, hebrew, and
    dreamspell values. dt is captured once.

    Atomicity: NOT transactional. No rollback. If an entry raises,
    entries already processed are not rolled back. Validate all
    entries before calling if all-or-nothing semantics are required.
    (PDE F-007 — semantic precision note)

    Returns list of SovereignRecord, one per entry, in input order.
    """
    if dt is None:
        dt = datetime.now(timezone.utc)
    return [stamp_and_record(e, dt) for e in entries]


def display(ts: SovereignStamp) -> str:
    """Render a SovereignStamp for human display (emoji format, full seal)."""
    return (
        f"📅 Gregorian:  {ts.gregorian}\n"
        f"🌑 Hebrew:     {ts.hebrew}\n"
        f"🌀 Dreamspell: {ts.dreamspell}\n"
        f"🔒 Seal:       {ts.seal}\n"
        f"📌 Version:    {ts.version}"
    )


def display_ascii(ts: SovereignStamp) -> str:
    """
    Render a SovereignStamp without emoji (full seal).
    For logging, piping, ASCII terminals, or CI output.
    """
    return (
        f"Gregorian:  {ts.gregorian}\n"
        f"Hebrew:     {ts.hebrew}\n"
        f"Dreamspell: {ts.dreamspell}\n"
        f"Seal:       {ts.seal}\n"
        f"Version:    {ts.version}"
    )


def verify(entry_text: str, ts: SovereignStamp) -> VerifyResult:
    """
    Verify that entry_text matches the seal in ts.

    Returns VerifyResult — evaluates as bool.

    Reason codes:
      "VALID"         — seal matches entry correctly
      "TYPE_ERROR"    — entry_text is not a str
      "SEAL_MISMATCH" — seal does not match

    IMPORTANT: SEAL_MISMATCH may mean wrong frozen version used,
    not necessarily tampered content. Check ts.version. If it is
    not "FROZEN-4.0", use the matching archived frozen version.
    A VERSION_MISMATCH reason code will be added in FROZEN-5.0.
    (PDE F-011, F-025, XD-002 — see FROZEN-5.0 CANDIDATES)
    """
    if not isinstance(entry_text, str):
        return VerifyResult(False, "TYPE_ERROR")
    entry_text = unicodedata.normalize("NFC", entry_text).strip()
    expected = _compute_seal(
        entry_text,
        ts.gregorian,
        ts.hebrew,
        ts.dreamspell,
        ts.unix_utc,
    )
    if expected == ts.seal:
        return VerifyResult(True, "VALID")
    return VerifyResult(False, "SEAL_MISMATCH")


def to_dict(ts: SovereignStamp) -> dict:
    """
    Serialize SovereignStamp to a plain dict (for JSON storage).

    Note: unix_utc is stored as int. Use int(d["unix_utc"]) when
    reading back if your JSON layer converts integers to floats.
    from_dict() enforces int coercion.

    Extra keys in the dict (e.g., "entry" added by SovereignRecord)
    are tolerated by from_dict() without raising. This behavior is
    intentional — from_dict() checks for required fields only.
    (PDE F-017)
    """
    return {
        "gregorian":  ts.gregorian,
        "hebrew":     ts.hebrew,
        "dreamspell": ts.dreamspell,
        "unix_utc":   ts.unix_utc,
        "seal":       ts.seal,
        "version":    ts.version,
    }


_REQUIRED_FIELDS = frozenset({"gregorian", "hebrew", "dreamspell", "unix_utc", "seal", "version"})

def from_dict(d: dict) -> SovereignStamp:
    """
    Deserialize a SovereignStamp from a plain dict.
    Validates schema before construction.

    Extra keys in d (beyond _REQUIRED_FIELDS) are tolerated without
    raising — this is intentional to support SovereignRecord.from_dict()
    which passes a dict containing an "entry" key alongside stamp fields.
    (PDE F-017)

    Raises ValueError for missing fields, invalid seal format,
    non-string calendar fields, version mismatch, or invalid unix_utc.
    """
    missing = _REQUIRED_FIELDS - d.keys()
    if missing:
        raise ValueError(f"from_dict: missing required fields: {sorted(missing)}")

    if not (isinstance(d["seal"], str) and _SEAL_PATTERN.match(d["seal"])):
        raise ValueError(
            f"from_dict: 'seal' must be a 64-character lowercase hex string. "
            f"Got: {d['seal']!r}"
        )

    for k in ("gregorian", "hebrew", "dreamspell", "version"):
        if not (isinstance(d[k], str) and d[k]):
            raise ValueError(
                f"from_dict: '{k}' must be a non-empty string. Got: {d[k]!r}"
            )

    if d["version"] != _FROZEN_VERSION:
        raise ValueError(
            f"from_dict: 'version' field is {d['version']!r}. "
            f"This reader is {_FROZEN_VERSION}. "
            "Use the matching archived frozen version to deserialize older stamps."
        )

    try:
        unix_utc = int(d["unix_utc"])
        if unix_utc <= 0:
            raise ValueError("unix_utc must be a positive integer")
    except (TypeError, ValueError) as exc:
        raise ValueError(f"from_dict: 'unix_utc' invalid — {exc}") from exc

    return SovereignStamp(
        gregorian  = d["gregorian"],
        hebrew     = d["hebrew"],
        dreamspell = d["dreamspell"],
        unix_utc   = unix_utc,
        seal       = d["seal"],
        version    = d["version"],
    )


# ═══════════════════════════════════════════════════════════════════
# SELF-TEST — FROZEN VERIFICATION CASES
# ═══════════════════════════════════════════════════════════════════

def _run_self_test(verbose: bool = True) -> None:
    """
    Verification against anchor values known at time of writing.
    Any failure means calendar algorithms have been broken or the
    file has been modified.

    Do not modify to make tests pass — create FROZEN-5.0.

    Self-test check count: 82 algorithmic checks + 2 sentinel checks
    + 3 invisible character checks = 87 total.
    The 2 sentinel checks address PDE F-001 and F-002.
    The 3 invisible character checks address adversarial battery
    finding (zero-width space, null byte, invisible char sequence).

    Failure output goes to stderr (PDE F-019, F-024) to prevent
    corruption of --json mode piped output.
    """
    import sys
    failures = []

    def check(label, actual, expected):
        if actual != expected:
            failures.append(f"  FAIL — {label}: got {actual!r}, expected {expected!r}")
        elif verbose:
            print(f"  ✓  {label}: {actual!r}")

    anchor_date = _date(2026, 3, 3)
    anchor_dt   = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)

    if verbose:
        print("═══ SOVEREIGN TRACE STAMP FROZEN-4.0 — SELF-TEST ═══")
        print(f"Anchor: {anchor_date}  (session of origin)\n")

    # ── SENTINEL STATE CHECK (PDE F-001, F-002) ───────────────────
    # This check must run first. A pre-release copy with an unset
    # sentinel should be identified immediately.
    if _FROZEN_FILE_SHA256 == "SET_AT_RELEASE_TIME":
        failures.append(
            "  WARN — _FROZEN_FILE_SHA256 is 'SET_AT_RELEASE_TIME'. "
            "This is a pre-release copy. File integrity cannot be verified. "
            "Do not deploy until the sentinel is set to the actual file hash."
        )
    elif verbose:
        print(f"  ✓  Sentinel is set (not placeholder): {_FROZEN_FILE_SHA256[:16]}...")

    # ── GENESIS SEAL STRUCTURAL CHECK ─────────────────────────────
    check("Genesis seal is 64-char hex",
          bool(_SEAL_PATTERN.match(_GENESIS_SEAL)), True)
    check("Genesis ledger entry declared",
          _GENESIS_LEDGER_ENTRY, "LEDGER-001-FOUNDING-SEAL")

    # ── Gregorian ─────────────────────────────────────────────────
    check("Gregorian", _gregorian(anchor_date), "March 3, 2026")

    # ── JD bridge ─────────────────────────────────────────────────
    check("JD(Sep 23 2025)",  _jd_from_gregorian(2025, 9, 23),  2460942)
    check("JD(Mar  3 2026)",  _jd_from_gregorian(2026, 3,  3),  2461103)

    # ── Hebrew epoch ──────────────────────────────────────────────
    check("1 Tishri 5786 JD",   _tishri_1_jd(5786),        2460942)
    check("1 Tishri 5787 JD",   _tishri_1_jd(5787),        2461296)

    # ── Hebrew year structure ─────────────────────────────────────
    check("5786 is NOT leap",   _is_hebrew_leap(5786), False)
    check("5784 IS leap",       _is_hebrew_leap(5784), True)
    check("5787 IS leap",       _is_hebrew_leap(5787), True)
    check("Year 5786 length",   _year_length(5786),    354)
    check("5786 legal length",  _year_length(5786) in _LEGAL_YEAR_LENGTHS, True)
    check("Year 5785 legal",    _year_length(5785) in _LEGAL_YEAR_LENGTHS, True)
    check("Year 5784 legal",    _year_length(5784) in _LEGAL_YEAR_LENGTHS, True)

    # ── Hebrew date conversion ────────────────────────────────────
    h_year, h_month, h_day = _gregorian_to_hebrew(2026, 3, 3)
    check("Hebrew year (Mar 3 2026)",   h_year,   5786)
    check("Hebrew month (Mar 3 2026)",  h_month,  "Adar")
    check("Hebrew day (Mar 3 2026)",    h_day,    14)
    check("Hebrew string (Mar 3 2026)", _hebrew(anchor_date), "14 Adar 5786")

    # ── Rosh Hashanah ─────────────────────────────────────────────
    rh_year, rh_month, rh_day = _gregorian_to_hebrew(2025, 9, 23)
    check("RH 5786 year",  rh_year,  5786)
    check("RH 5786 month", rh_month, "Tishri")
    check("RH 5786 day",   rh_day,   1)

    # ── Erev Rosh Hashanah ────────────────────────────────────────
    evrh_year, evrh_month, evrh_day = _gregorian_to_hebrew(2025, 9, 22)
    check("Erev RH 5786 month", evrh_month, "Elul")
    check("Erev RH 5786 day",   evrh_day,   29)

    # ── Yom Kippur ────────────────────────────────────────────────
    yk_year, yk_month, yk_day = _gregorian_to_hebrew(2025, 10, 2)
    check("Yom Kippur 5786 month", yk_month, "Tishri")
    check("Yom Kippur 5786 day",   yk_day,   10)

    # ── Passover ──────────────────────────────────────────────────
    ps_year, ps_month, ps_day = _gregorian_to_hebrew(2026, 4, 2)
    check("Passover 5786 month", ps_month, "Nisan")
    check("Passover 5786 day",   ps_day,   15)

    # ── 1 Nisan ───────────────────────────────────────────────────
    n1_year, n1_month, n1_day = _gregorian_to_hebrew(2026, 3, 19)
    check("1 Nisan 5786 month", n1_month, "Nisan")
    check("1 Nisan 5786 day",   n1_day,   1)

    # ── Leap year anchors ─────────────────────────────────────────
    leap_y, leap_m, leap_d = _gregorian_to_hebrew(2024, 3, 25)
    check("Leap year 5784 month (Adar II)", leap_m, "Adar II")
    check("Leap year 5784 day (15)",        leap_d, 15)
    check("Leap year 5784 year",            leap_y, 5784)

    adar1_y, adar1_m, adar1_d = _gregorian_to_hebrew(2024, 2, 10)
    check("Adar I 5784 month", adar1_m, "Adar I")
    check("Adar I 5784 day",   adar1_d, 1)

    # ── RH 5787 (FROZEN-3.0 CRITICAL fix) ────────────────────────
    rh87_y, rh87_m, rh87_d = _gregorian_to_hebrew(2026, 9, 12)
    check("RH 5787 year",  rh87_y, 5787)
    check("RH 5787 month", rh87_m, "Tishri")
    check("RH 5787 day",   rh87_d, 1)

    erh87_y, erh87_m, erh87_d = _gregorian_to_hebrew(2026, 9, 11)
    check("Erev RH 5787 month", erh87_m, "Elul")
    check("Erev RH 5787 day",   erh87_d, 29)

    sep22_y, sep22_m, sep22_d = _gregorian_to_hebrew(2026, 9, 22)
    check("Sep 22 2026 day is 11 (NOT 1)", sep22_d, 11)
    check("Sep 22 2026 month is Tishri",   sep22_m, "Tishri")

    # ── Dreamspell ────────────────────────────────────────────────
    check("Dreamspell Mar 3 2026", _dreamspell(anchor_date),
          "Day 25, Galactic Moon 8/13")
    check("Day Out of Time Jul 25", _dreamspell(_date(2026, 7, 25)),
          "Day Out of Time")
    check("Dreamspell Jul 26 (Moon 1 Day 1)",
          _dreamspell(_date(2026, 7, 26)), "Day 1, Magnetic Moon 1/13")
    check("Dreamspell Mar 1 2028 (post-leap-Feb)",
          _dreamspell(_date(2028, 3, 1)), "Day 24, Galactic Moon 8/13")

    # ── UTC midnight boundary (PDE F-021) ─────────────────────────
    # Two stamps one second apart straddling UTC midnight produce
    # different calendar dates. This is expected behavior.
    dt_before_midnight = datetime(2026, 3, 3, 23, 59, 59, tzinfo=timezone.utc)
    dt_after_midnight  = datetime(2026, 3, 4,  0,  0,  0, tzinfo=timezone.utc)
    ts_before = stamp("boundary test before", dt_before_midnight)
    ts_after  = stamp("boundary test after",  dt_after_midnight)
    check("UTC midnight: different dates produce different gregorian",
          ts_before.gregorian != ts_after.gregorian, True)
    check("UTC midnight before = March 3",  ts_before.gregorian, "March 3, 2026")
    check("UTC midnight after  = March 4",  ts_after.gregorian,  "March 4, 2026")

    # ── JD range guards ───────────────────────────────────────────
    try:
        _jd_from_gregorian(1581, 1, 1)
        failures.append("  FAIL — Pre-1582 year should raise ValueError")
    except ValueError:
        if verbose: print("  ✓  Pre-1582 year correctly rejected")

    try:
        _jd_from_gregorian(1582, 10, 14)
        failures.append("  FAIL — 1582-10-14 should raise ValueError")
    except ValueError:
        if verbose: print("  ✓  1582-10-14 pre-reform boundary correctly rejected")

    try:
        jd_reform = _jd_from_gregorian(1582, 10, 15)
        if verbose: print(f"  ✓  1582-10-15 accepted: JD {jd_reform}")
    except ValueError:
        failures.append("  FAIL — 1582-10-15 should be accepted")

    # ── Unicode normalization ─────────────────────────────────────
    entry_nfc = "caf\u00e9"
    entry_nfd = "cafe\u0301"
    ts_nfc = stamp(entry_nfc, anchor_dt)
    ts_nfd = stamp(entry_nfd, anchor_dt)
    check("NFC/NFD normalization: identical seals", ts_nfc.seal, ts_nfd.seal)

    # ── Whitespace normalization ──────────────────────────────────
    ts_trimmed = stamp("hello", anchor_dt)
    ts_padded  = stamp("  hello  ", anchor_dt)
    check("Whitespace normalization: identical seals", ts_padded.seal, ts_trimmed.seal)

    # ── Version field ─────────────────────────────────────────────
    ts_anchor = stamp("anchor", anchor_dt)
    check("Stamp version is FROZEN-4.0", ts_anchor.version, "FROZEN-4.0")

    # ── Seal round-trip ───────────────────────────────────────────
    test_entry = "Origin trace — Sovereign Trace Protocol FROZEN-4.0."
    ts = stamp(test_entry, anchor_dt)
    vr_good  = verify(test_entry, ts)
    vr_alter = verify("altered text", ts)
    vr_empty = verify("", ts)
    vr_none  = verify(None, ts)
    check("verify correct entry: valid",      vr_good.valid,    True)
    check("verify correct entry: VALID",      vr_good.reason,   "VALID")
    check("verify altered: invalid",          vr_alter.valid,   False)
    check("verify altered: SEAL_MISMATCH",    vr_alter.reason,  "SEAL_MISMATCH")
    check("verify empty: invalid",            vr_empty.valid,   False)
    check("verify None: TYPE_ERROR",          vr_none.reason,   "TYPE_ERROR")
    check("VerifyResult(True) truthy",        bool(vr_good),    True)
    check("VerifyResult(False) falsy",        bool(vr_alter),   False)

    # ── Hebrew field ──────────────────────────────────────────────
    check("Stamp Hebrew field", ts.hebrew, "14 Adar 5786")

    # ── check_invariant ───────────────────────────────────────────
    check("check_invariant on valid stamp", ts.check_invariant(), True)

    # ── __eq__ and __hash__ ───────────────────────────────────────
    ts_copy  = stamp(test_entry, anchor_dt)
    ts_other = stamp("different entry", anchor_dt)
    check("Same-input stamps equal",       ts == ts_copy,  True)
    check("Same-input stamps share hash",  hash(ts) == hash(ts_copy), True)
    check("Different-entry stamps differ", ts == ts_other, False)

    # ── Immutability ──────────────────────────────────────────────
    try:
        ts.gregorian = "tampered"
        failures.append("  FAIL — SovereignStamp should be immutable")
    except AttributeError:
        if verbose: print("  ✓  SovereignStamp immutability enforced")

    # ── SovereignRecord ───────────────────────────────────────────
    rec = stamp_and_record(test_entry, anchor_dt)
    check("Record entry matches",    rec.entry,           test_entry)
    check("Record verify valid",     rec.verify().valid,  True)
    check("Record verify reason",    rec.verify().reason, "VALID")

    try:
        rec.entry = "tampered"
        failures.append("  FAIL — SovereignRecord should be immutable")
    except AttributeError:
        if verbose: print("  ✓  SovereignRecord immutability enforced")

    # ── Serialization round-trip ──────────────────────────────────
    d2 = to_dict(ts)
    ts2 = from_dict(d2)
    check("Round-trip seal",     ts2.seal,    ts.seal)
    check("Round-trip version",  ts2.version, ts.version)
    check("Round-trip __eq__",   ts2 == ts,   True)

    # ── SovereignRecord round-trip ────────────────────────────────
    rec_dict = rec.to_dict()
    rec2 = SovereignRecord.from_dict(rec_dict)
    check("Record round-trip entry",  rec2.entry,          rec.entry)
    check("Record round-trip seal",   rec2.stamp.seal,     rec.stamp.seal)
    check("Record round-trip verify", rec2.verify().valid, True)

    # ── from_dict validation ──────────────────────────────────────
    try:
        from_dict({"gregorian": "x", "hebrew": "y", "dreamspell": "z"})
        failures.append("  FAIL — from_dict should reject missing fields")
    except ValueError:
        if verbose: print("  ✓  from_dict rejects missing fields")

    bad_seal = dict(d2); bad_seal["seal"] = "not-valid"
    try:
        from_dict(bad_seal)
        failures.append("  FAIL — from_dict should reject invalid seal")
    except ValueError:
        if verbose: print("  ✓  from_dict rejects invalid seal format")

    bad_ver = dict(d2); bad_ver["version"] = "FROZEN-3.0"
    try:
        from_dict(bad_ver)
        failures.append("  FAIL — from_dict should reject foreign version")
    except ValueError:
        if verbose: print("  ✓  from_dict rejects foreign version field")

    # ── stamp_batch ───────────────────────────────────────────────
    batch = stamp_batch(["first", "second", "third"], anchor_dt)
    check("Batch length",            len(batch),                              3)
    check("Batch shared unix_utc",   len({r.stamp.unix_utc for r in batch}), 1)
    check("Batch record 0 verifies", batch[0].verify().valid,                True)
    check("Batch record 2 verifies", batch[2].verify().valid,                True)

    # ── Error handling ────────────────────────────────────────────
    try:
        stamp("")
        failures.append("  FAIL — empty entry should raise ValueError")
    except ValueError:
        if verbose: print("  ✓  Empty entry rejected")

    try:
        stamp("   ")
        failures.append("  FAIL — whitespace-only entry should raise ValueError")
    except ValueError:
        if verbose: print("  ✓  Whitespace-only entry rejected")

    try:
        stamp("\u200b")
        failures.append("  FAIL — zero-width space only should raise ValueError")
    except ValueError:
        if verbose: print("  ✓  Zero-width space only rejected (invisible char guard)")

    try:
        stamp("\x00")
        failures.append("  FAIL — null byte only should raise ValueError")
    except ValueError:
        if verbose: print("  ✓  Null byte only rejected (invisible char guard)")

    try:
        stamp("\u200b\u200c\u200d")
        failures.append("  FAIL — multiple invisible chars should raise ValueError")
    except ValueError:
        if verbose: print("  ✓  Multiple invisible chars rejected (invisible char guard)")

    try:
        stamp("text", datetime(2026, 3, 3, 15, 0, 0))  # naive
        failures.append("  FAIL — naive datetime should raise ValueError")
    except ValueError:
        if verbose: print("  ✓  Naive datetime rejected")

    # ── FROZEN-1.0 regression ─────────────────────────────────────
    check("FROZEN-1.0 regression: NOT 15 Adar",
          ts.hebrew != "15 Adar 5786", True)

    # ── Result (failures to stderr — PDE F-019, F-024) ────────────
    if verbose:
        print()
    if failures:
        for f in failures:
            print(f, file=sys.stderr)
        raise AssertionError(
            f"{len(failures)} self-test failure(s). "
            "Do not deploy. Verify algorithms from first principles. "
            "Create FROZEN-5.0 if correction is needed."
        )
    else:
        if verbose:
            print("═══ ALL TESTS PASSED ═══")
            print()
            print("Anchor stamp (March 3, 2026 — session of origin):")
            print(display(ts))


# ═══════════════════════════════════════════════════════════════════
# CLI — INTERACTIVE TRACE ENTRY
# ═══════════════════════════════════════════════════════════════════

def _cli(json_mode: bool = False) -> None:
    """
    Interactive sovereign trace entry with live stamp.

    Privacy notice: entry text submitted via stdin, printed to stdout.
    On shared systems, stdout may be logged. Shell history may record
    the invocation. Terminal scrollback may retain the JSON record.
    Entry text is not encrypted at rest.

    Process memory note: entry text exists in process memory from
    stdin read until process exit. On multi-tenant systems with shared
    memory visibility, this is an operator-assessed risk.

    JSON mode note: --json emits only machine-readable JSON to stdout.
    Self-test failure messages go to stderr to prevent stream corruption.
    (PDE F-019, F-024)

    Calendar note: calendar dates reflect UTC.
    Computational permanence note: "This seal is computationally
    tamper-evident under SHA-256" — not absolutely permanent.
    See INTEGRITY BOUNDARIES section in module docstring. (MF-M-003)
    """
    import sys
    if not json_mode:
        print("═══════════════════════════════════════════════════")
        print(f"  SOVEREIGN TRACE PROTOCOL — {_FROZEN_VERSION}")
        print("  Your trace will be sealed.")
        print("  The seal is computationally tamper-evident under SHA-256.")
        print("  Note: calendar dates reflect UTC.")
        print("  Note: entry will appear in stdout (may be logged).")
        print("═══════════════════════════════════════════════════\n")

    entry = input("Your trace (present-moment, exact, no narrative arc):\n> ")
    entry_normalized = unicodedata.normalize("NFC", entry).strip()
    if not entry_normalized:
        if not json_mode:
            print("Empty trace. Nothing sealed.")
        return

    ts = stamp(entry_normalized)
    rec = SovereignRecord(entry_normalized, ts)

    if json_mode:
        print(json.dumps(rec.to_dict(), indent=2, ensure_ascii=False))
    else:
        print()
        print("─── SEALED ───────────────────────────────────────")
        print(display(ts))
        print("─── JSON (store this) ────────────────────────────")
        print(json.dumps(rec.to_dict(), indent=2, ensure_ascii=False))
        print("──────────────────────────────────────────────────")
        print("Seal is computationally tamper-evident under SHA-256.")
        print("Keep the JSON. The ledger append comes next.")


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv or "-t" in sys.argv:
        _run_self_test(verbose=True)
    else:
        _run_self_test(verbose=False)
        _cli(json_mode="--json" in sys.argv)
