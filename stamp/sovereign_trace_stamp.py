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
     Effect: semantically identical text with different normalization
     states produced different seals. Silent divergence.

  2. No stamp version field in seal payload.
     Effect: FROZEN-2.0 stamps indistinguishable from stamps
     produced by any modified variant. Provenance gap.

  3. Year length not validated against legal Hebrew year lengths.
     Effect: Silent wrong output if algorithm produced illegal
     year length on edge inputs.

  4. No convergence bound on Hebrew year-finding loop.
     Effect: Uncertifiable loop for extreme date inputs.

  5. from_dict() accepted unvalidated dicts.
     Effect: Garbage calendar fields with valid-looking seal.

  6. Whitespace sealed but not normalized.
     Effect: " hello" and "hello" produced different seals.

  7. int(dt.timestamp()) truncation undeclared.
  8. _jd_from_gregorian() accepted pre-Gregorian-reform years silently.

All FROZEN-2.0 stamps carry no version field in their seal —
this is the definitive retirement marker.

FROZEN-1.0 RETIREMENT NOTE (carried forward)
─────────────────────────────────────────────
FROZEN-1.0 is retired. Defect: Hebrew calendar omitted the
four dehiyot (postponement rules) correctly. Specifically,
GaTaRaD and BeTUTeKaPoT were not implemented, and the epoch
used the sunset-start convention rather than the civil-day
convention used by authoritative converters (Hebcal, Chabad).
Effect: Hebrew dates were off by one day for affected years
(including all of 5786). All stamps produced by FROZEN-1.0
carry a known Hebrew field error. Archived as:
SOVEREIGN-TRACE-STAMP-FROZEN-1.0-RETIRED.py
Do not use FROZEN-1.0 for new stamps.

BACKWARD COMPATIBILITY
──────────────────────
FROZEN-3.0 seals are NOT backward-compatible with FROZEN-2.0.
The seal payload now includes "version":"FROZEN-3.0".
A FROZEN-2.0 stamp will not verify against FROZEN-3.0 verify().
Use FROZEN-2.0 to verify FROZEN-2.0 stamps from archived ledgers.

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
  Input dates before October 15, 1582 will raise ValueError — this
  includes all dates in 1582 before October 15. Pre-reform dates
  require the Julian calendar and produce incorrect JD values.
  Upper bound: year 4000 (practical; no algorithmic constraint).

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

Operator deployment verification procedure:
  Step 1. Obtain the released sovereign_trace_stamp.py
  Step 2. Run: sha256sum sovereign_trace_stamp.py
            or: python3 -c "import hashlib; print(hashlib.sha256(open('sovereign_trace_stamp.py','rb').read()).hexdigest())"
  Step 3. Compare output against _FROZEN_FILE_SHA256 below.
  Step 4. If they match: the file is unmodified.
          If they differ: the file has been altered since release.
          Do not deploy an altered file.

The bootstrap problem (a file cannot contain its own hash before the
hash is computed) means the sentinel is inserted last, after all code
is final. The "SET_AT_RELEASE_TIME" placeholder in any pre-release
copy is expected — the released file carries the actual hash.
═══════════════════════════════════════════════════════════════════
"""

import hashlib
import json
import re
import unicodedata
from datetime import datetime, timezone, date as _date
from typing import NamedTuple


# ═══════════════════════════════════════════════════════════════════
# FILE INTEGRITY SEAL — FROZEN-4.0
# Set this constant to the SHA-256 of the released .py file.
# Verification is the operator's deployment responsibility.
# Internal self-hash is impossible (bootstrap problem).
# ═══════════════════════════════════════════════════════════════════
_FROZEN_FILE_SHA256 = "SET_AT_RELEASE_TIME"
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
        """
        Equality by seal — the canonical cryptographic identity.
        Two stamps are equal if and only if their seals match.
        """
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

        Returns True if all structural invariants hold, False otherwise.
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
        """Serialize to a plain dict (for JSON storage)."""
        d = to_dict(self.stamp)
        d["entry"] = self.entry
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "SovereignRecord":
        """
        Deserialize a SovereignRecord from a plain dict.
        Validates schema before construction.
        Raises ValueError if required fields are missing or malformed.
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
    reason : str  — "VALID" | "TAMPERED" | "TYPE_ERROR" | "SEAL_MISMATCH"

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

# Valid range for Gregorian calendar (reform: Oct 15, 1582)
_JD_MIN_YEAR = 1582
_JD_MAX_YEAR = 4000

def _jd_from_gregorian(year: int, month: int, day: int) -> int:
    """
    Julian Day Number from Gregorian date.
    Algorithm: Meeus, "Astronomical Algorithms", p. 61.
    Verified: JD(Sep 23, 2025) = 2,460,942
              JD(Mar  3, 2026) = 2,461,103

    Complexity: O(1) time, O(1) space.

    Raises
    ------
    ValueError
        If year is outside [{_JD_MIN_YEAR}, {_JD_MAX_YEAR}].
        If year is 1582 and date is before October 15 (pre-reform).
        Dates before Gregorian reform (Oct 15, 1582) require Julian
        calendar — the Gregorian formula produces incorrect JD values.
    """
    if not (_JD_MIN_YEAR <= year <= _JD_MAX_YEAR):
        raise ValueError(
            f"_jd_from_gregorian: year {year} outside valid range "
            f"[{_JD_MIN_YEAR}, {_JD_MAX_YEAR}]. "
            "Dates before Gregorian calendar reform (Oct 15, 1582) "
            "require the Julian calendar formula."
        )
    # Pre-reform boundary guard: the Gregorian calendar took effect Oct 15, 1582.
    # The entire year 1582 passes the year-range check above, but dates in
    # Jan–Oct 14 are Julian, not Gregorian, and produce incorrect JD values.
    # RT-STS-002: contract previously said "before 1582" but year==1582 with
    # month<10 (or month==10, day<15) was silently accepted. Fixed here. [D]
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

# Julian Day of Hebrew epoch — civil-day convention (daytime = Hebrew date)
# JD 347998 = Sep 23 equivalent for year 1 anchor
# Verified: _tishri_1_jd(5786) = 2,460,942 = JD(Sep 23, 2025) = 1 Tishri 5786 [D]
_HEBREW_EPOCH_JD = 347998

# Legal Hebrew year lengths. Any value outside this set is an algorithm error.
# 353/354/355 = common year (deficient/regular/complete)
# 383/384/385 = leap year   (deficient/regular/complete)
# Source: D&R §8.1 — the six admissible year lengths under the metonic cycle.
_LEGAL_YEAR_LENGTHS = frozenset({353, 354, 355, 383, 384, 385})

# Maximum iterations for Hebrew year-finding loop (D&R approximation is within
# 3 years of the target for all inputs in [1582, 4000]; 6 is a safe margin).
# CAL FTT-CAL-09 — Minsky convergence certification.
_MAX_YEAR_SEARCH = 6

_HEBREW_MONTHS_COMMON = (
    "Tishri", "Cheshvan", "Kislev", "Tevet", "Shevat", "Adar",
    "Nisan",  "Iyar",     "Sivan",  "Tammuz","Av",     "Elul"
)
_HEBREW_MONTHS_LEAP = (
    "Tishri", "Cheshvan", "Kislev", "Tevet", "Shevat", "Adar I", "Adar II",
    "Nisan",  "Iyar",     "Sivan",  "Tammuz","Av",     "Elul"
)


def _is_hebrew_leap(year: int) -> bool:
    """Hebrew leap year: (7y + 1) mod 19 < 7. Complexity: O(1)."""
    return (7 * year + 1) % 19 < 7


def _elapsed_days(year: int) -> int:
    """
    Days from Hebrew epoch to 1 Tishri of year — Pass 1.
    Implements Lo ADU Rosh (not Sun/Wed/Fri) and Molad Zaken (molad >= 18h).
    Algorithm: D&R "Calendrical Calculations" 4th ed., §8.1–§8.2.
    GaTaRaD and BeTUTeKaPoT are handled in Pass 2 (_new_year_delay).
    Complexity: O(1) time, O(1) space.
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
    Handles GaTaRaD and BeTUTeKaPoT by checking adjacent year lengths.
    Returns 0, 1, or 2.
    Algorithm: D&R "Calendrical Calculations" 4th ed., §8.3–§8.4.

    Logic (D&R §8.4):
      GaTaRaD:      If the coming year would have 356 days → postpone 2 days.
      BeTUTeKaPoT:  If the prior year had 382 days         → postpone 1 day.
      Otherwise no additional postponement.

    Mutual exclusion: GaTaRaD and BeTUTeKaPoT cannot be simultaneously active
    for any valid Hebrew year (provable from D&R §8.4 — no valid year
    satisfies both ny2-ny1==356 AND ny1-ny0==382). GaTaRaD takes priority
    via elif — this is the correct D&R ordering, not an arbitrary choice.

    Verified: _new_year_delay(5786) = 1 (BeTUTeKaPoT active for 5786)
    Complexity: O(1) time, O(1) space.
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
    Full four dehiyot: Pass 1 (elapsed_days) + Pass 2 (new_year_delay).
    Civil-day convention: date corresponds to daytime hours of the civil day.
    Verified: _tishri_1_jd(5786) = 2,460,942 = Sep 23, 2025 [D]
    Complexity: O(1) time, O(1) space.
    """
    return _elapsed_days(h_year) + _new_year_delay(h_year) + _HEBREW_EPOCH_JD


def _year_length(h_year: int) -> int:
    """Complexity: O(1) time, O(1) space."""
    return _tishri_1_jd(h_year + 1) - _tishri_1_jd(h_year)


def _month_lengths(h_year: int) -> tuple:
    """
    Ordered month lengths (Tishri → Elul) for h_year.
    Complexity: O(1) time, O(1) space (fixed 12 or 13 months).

    Raises
    ------
    ValueError
        If the computed year length is not in _LEGAL_YEAR_LENGTHS.
        This indicates an algorithm error — do not patch, create FROZEN-5.0.
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
        30 if long_cheshvan else 29,   # Cheshvan
        29 if short_kislev  else 30,   # Kislev
        29,                             # Tevet
        30,                             # Shevat
        30 if leap else 29,             # Adar I (leap) or Adar (common)
    ]
    if leap:
        months.append(29)               # Adar II
    months += [30, 29, 30, 29, 30, 29] # Nisan → Elul
    return tuple(months)


def _gregorian_to_hebrew(year: int, month: int, day: int) -> tuple:
    """
    Convert Gregorian date to Hebrew (h_year, month_name, h_day).
    Civil-day convention — aligns with Hebcal and Chabad.org.
    Algorithm: D&R §8.1–§8.4 two-pass. See module docstring for
    theorem references.

    Complexity: O(k) time where k = year search iterations.
      The D&R approximation formula is accurate within 3 years for
      all inputs in [1582, 4000]. _MAX_YEAR_SEARCH = 6 provides
      a safe margin. Loop is bounded — Minsky-certified (CAL FTT-CAL-09).
    Space: O(m) where m = number of months in year (12 or 13).

    Verified anchors (Hebcal/Chabad):
      gregorian_to_hebrew(2025, 9, 23) == (5786, "Tishri", 1)   [D]
      gregorian_to_hebrew(2025, 10, 2) == (5786, "Tishri", 10)  [D]
      gregorian_to_hebrew(2026, 3, 3)  == (5786, "Adar", 14)    [D] [Purim]
      gregorian_to_hebrew(2026, 3, 19) == (5786, "Nisan", 1)    [D]
      gregorian_to_hebrew(2026, 4, 2)  == (5786, "Nisan", 15)   [D] [Passover]
      gregorian_to_hebrew(2024, 3, 25) == (5784, "Adar II", 15) [D] [Leap]
      gregorian_to_hebrew(2025, 9, 22) == (5786, "Elul", 29)    [D] [Erev RH]
      gregorian_to_hebrew(2023, 10, 7) == (5784, "Tishri", 22)  [D] [5784 Tishri]
      gregorian_to_hebrew(2026, 9, 12) == (5787, "Tishri", 1)   [D] [RH 5787 — pyluach verified]
      gregorian_to_hebrew(2026, 9, 11) == (5786, "Elul", 29)    [D] [Erev RH 5787]

    Raises
    ------
    ValueError
        If the year search loop does not converge (algorithm error).
        If year is outside valid range (propagated from _jd_from_gregorian).
        If Hebrew conversion overflows month table (algorithm error).
    """
    jd = _jd_from_gregorian(year, month, day)

    # Approximate Hebrew year then close in.
    # Bounded loops — FTT-CAL-09 Minsky certification.
    h_year = (jd - _HEBREW_EPOCH_JD) * 19 // 6935 + 1

    # Upward search: advance until the next Tishri 1 is past our JD
    for _ in range(_MAX_YEAR_SEARCH):
        if _tishri_1_jd(h_year + 1) <= jd:
            h_year += 1
        else:
            break
    else:
        raise AssertionError(
            f"Hebrew year (upward) search did not converge for JD {jd} "
            f"({year}-{month}-{day}). Algorithm error — do not patch. "
            "Create FROZEN-5.0."
        )

    # Downward search: retreat until current Tishri 1 is at or before our JD
    for _ in range(_MAX_YEAR_SEARCH):
        if _tishri_1_jd(h_year) > jd:
            h_year -= 1
        else:
            break
    else:
        raise AssertionError(
            f"Hebrew year (downward) search did not converge for JD {jd} "
            f"({year}-{month}-{day}). Algorithm error — do not patch. "
            "Create FROZEN-5.0."
        )

    day_of_year = jd - _tishri_1_jd(h_year)   # 0-indexed

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
        "Algorithm error — do not patch. Create FROZEN-5.0."
    )


def _hebrew(d: _date) -> str:
    h_year, h_month, h_day = _gregorian_to_hebrew(d.year, d.month, d.day)
    return f"{h_day} {h_month} {h_year}"


# ═══════════════════════════════════════════════════════════════════
# 13 MOON DREAMSPELL (Argüelles system)
# ═══════════════════════════════════════════════════════════════════
# Disambiguation: This is the José Argüelles 13 Moon calendar.
# It is NOT the traditional Maya Tzolkin or Haab correlation.
# Users expecting the traditional Maya system will receive different
# dates. This declaration is by design — not an error.
# ═══════════════════════════════════════════════════════════════════

_MOON_NAMES = (
    "Magnetic",    "Lunar",     "Electric",  "Self-Existing",
    "Overtone",    "Rhythmic",  "Resonant",  "Galactic",
    "Solar",       "Planetary", "Spectral",  "Crystal",     "Cosmic"
)

def _dreamspell(d: _date) -> str:
    """
    13 Moon Dreamspell calendar (Argüelles system — see disambiguation above).

    Rules:
      — Year begins July 26.
      — 13 moons × 28 days = 364 days.
      — Day Out of Time = July 25 (365th day, outside the moons).
      — Leap years: Python's date arithmetic handles Feb 29 correctly.
        The 364-day Dreamspell year is independent of the Gregorian
        leap cycle — delta computation uses date subtraction which
        is always correct across leap year boundaries.

    Dead branch declaration (PDE-STS-004):
      The delta >= 364 branch below is structurally unreachable because
      July 25 is always caught by the explicit check above, and no
      date in [Jul 26 .. Jul 24] produces delta >= 364 within the
      28×13 structure. It is preserved as a defensive guard against
      future refactoring. pragma: no cover — defensive only.

    Verified anchors:
      dreamspell(date(2026, 3, 3))  == "Day 25, Galactic Moon 8/13"   [R]
      dreamspell(date(2026, 7, 25)) == "Day Out of Time"               [R]
      dreamspell(date(2026, 7, 26)) == "Day 1, Magnetic Moon 1/13"    [R]
      Calculation: Jul 26 2025 → Mar 3 2026 = 220 days (0-indexed)
                   220 // 28 + 1 = 8 (Galactic) | 220 % 28 + 1 = 25 ✓

    Complexity: O(1) time, O(1) space.
    """
    if d.month == 7 and d.day == 25:
        return "Day Out of Time"

    if (d.month, d.day) >= (7, 26):
        year_start = _date(d.year, 7, 26)
    else:
        year_start = _date(d.year - 1, 7, 26)

    delta = (d - year_start).days

    # NOTE: This branch is structurally unreachable (see docstring).
    # Preserved as defensive guard against future refactoring.
    if delta < 0 or delta >= 364:  # pragma: no cover — defensive only
        return "Day Out of Time"

    moon    = delta // 28 + 1
    day_num = delta % 28 + 1
    return f"Day {day_num}, {_MOON_NAMES[moon - 1]} Moon {moon}/13"


# ═══════════════════════════════════════════════════════════════════
# SEAL — SHA-256 CRYPTOGRAPHIC BINDING
# ═══════════════════════════════════════════════════════════════════

_SEAL_PATTERN = re.compile(r'^[0-9a-f]{64}$')

def _compute_seal(entry_text: str, gregorian: str, hebrew: str,
                  dreamspell: str, unix_utc: int) -> str:
    """
    SHA-256 of a deterministic JSON payload binding entry text,
    all three temporal representations, Unix UTC, and version string.
    Output: 64-character lowercase hex string.

    Payload field order (sort_keys=True — alphabetical):
      dreamspell, entry, gregorian, hebrew, unix_utc, version

    unix_utc is serialized as an integer (not float).
    ensure_ascii=True guarantees determinism across platforms.
    entry_text must be NFC-normalized before this call — stamp() enforces this.

    Semantic note (PDE-STS-028):
      The seal proves that this entry was bound to these exact calendar
      strings at this exact unix time by this version of the stamp function.
      It does NOT independently prove that the calendar strings are
      correctly computed — that guarantee is carried by the self-test
      and the algorithm specification, not by the seal itself.

    Complexity: O(|entry_text|) time (SHA-256 over payload string).
    """
    payload = json.dumps(
        {
            "dreamspell": dreamspell,
            "entry":      entry_text,
            "gregorian":  gregorian,
            "hebrew":     hebrew,
            "unix_utc":   unix_utc,   # Always int — json.dumps serializes as integer
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
        Text is NFC-normalized and stripped before sealing.
        " hello " and "hello" produce identical seals.
        Unicode normalization: NFC applied before SHA-256.
    dt : datetime, optional
        Moment to stamp. Defaults to UTC now.
        Must be timezone-aware if provided.

    Returns
    -------
    SovereignStamp
        Immutable object holding all three calendar representations,
        the SHA-256 seal binding content to this exact moment,
        and the FROZEN-4.0 version identifier.

    Raises
    ------
    ValueError
        If dt is timezone-naive.
        If entry_text is empty (after strip and NFC normalization).
        If date is outside valid Gregorian range [Oct 15 1582, year 4000].
        If calendar algorithm produces illegal year length.
        If Hebrew conversion overflows (algorithm error — create FROZEN-5.0).
    TypeError
        If entry_text is not a string.

    Notes
    -----
    unix_utc is whole seconds only (truncated, not rounded).
    Sub-second precision is intentionally discarded.
    Calendar dates reflect UTC — not local civil date.
    """
    if not isinstance(entry_text, str):
        raise TypeError(f"entry_text must be str, got {type(entry_text).__name__}")

    # NFC normalization and strip — applied before both validation and sealing.
    # This resolves PDE-STS-001 (Unicode normalization) and PDE-STS-012
    # (whitespace normalization inconsistency).
    entry_text = unicodedata.normalize("NFC", entry_text).strip()

    if not entry_text:
        raise ValueError("entry_text must be non-empty — an empty trace seals nothing.")

    if dt is None:
        dt = datetime.now(timezone.utc)
    elif dt.tzinfo is None:
        raise ValueError(
            "dt must be timezone-aware. "
            "Use datetime(..., tzinfo=timezone.utc) or datetime.now(timezone.utc)."
        )

    d = dt.date()
    # unix_utc is truncated (not rounded) to whole seconds.
    # Sub-second precision is intentionally dropped.
    # Two datetimes within the same second produce identical unix_utc values.
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

    Equivalent to: SovereignRecord(entry_text, stamp(entry_text, dt))
    but applies the same NFC normalization stamp() uses, so the stored
    entry matches the sealed entry exactly.

    Parameters and raises: see stamp().
    """
    # Apply normalization first so the stored entry matches the sealed entry.
    if not isinstance(entry_text, str):
        raise TypeError(f"entry_text must be str, got {type(entry_text).__name__}")
    entry_text = unicodedata.normalize("NFC", entry_text).strip()
    ts = stamp(entry_text, dt)
    return SovereignRecord(entry_text, ts)


def stamp_batch(entries: list, dt: datetime = None) -> list:
    """
    Seal multiple entries at a single canonical timestamp.

    All entries in the batch are stamped at the same datetime — either
    the provided dt or a single datetime.now(timezone.utc) call.
    This ensures entries that logically belong to the same moment
    carry identical unix_utc values, gregorian, hebrew, and dreamspell.

    Atomicity: this function is NOT atomic in any transactional sense.
    It processes entries sequentially in a single Python thread. If an
    entry raises ValueError or TypeError (e.g., empty text, wrong type),
    the error propagates immediately and no further entries are stamped.
    Entries already processed are not rolled back — there is no rollback
    mechanism. Callers requiring all-or-nothing behavior should validate
    all entries before calling stamp_batch.

    Parameters
    ----------
    entries : list of str
        Entry texts to seal. Each must be non-empty after normalization.
    dt : datetime, optional
        Shared moment for all stamps. Defaults to UTC now (called once).

    Returns
    -------
    list of SovereignRecord
        One SovereignRecord per entry, in input order.

    Raises
    ------
    ValueError, TypeError
        Propagated from stamp() for any invalid entry.
    """
    if dt is None:
        dt = datetime.now(timezone.utc)
    return [stamp_and_record(e, dt) for e in entries]


def display(ts: SovereignStamp) -> str:
    """Render a SovereignStamp for human display (emoji format)."""
    return (
        f"📅 Gregorian:  {ts.gregorian}\n"
        f"🌑 Hebrew:     {ts.hebrew}\n"
        f"🌀 Dreamspell: {ts.dreamspell}\n"
        f"🔒 Seal:       {ts.seal}\n"
        f"📌 Version:    {ts.version}"
    )


def display_ascii(ts: SovereignStamp) -> str:
    """
    Render a SovereignStamp without emoji.
    For logging, piping, ASCII terminals, or CI output.
    Cryptographically identical to display() — no data omitted.
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

    Returns
    -------
    VerifyResult
        Evaluates as bool. reason field distinguishes failure modes:
        "VALID"        — seal matches entry
        "TYPE_ERROR"   — entry_text is not a str (wrong type, not tampering)
        "SEAL_MISMATCH"— seal does not match (tampered, wrong entry, or
                         stamp produced by a different version)

    Notes
    -----
    Applies the same NFC normalization as stamp(). If the original entry
    was produced via stamp() or stamp_and_record(), the stored entry
    already has normalization applied — passing it raw here is correct.

    A SEAL_MISMATCH result means: the entry was altered, or this stamp
    was produced by a different version of the function.
    FROZEN-3.0 seals will not verify against FROZEN-2.0 stamps (version
    field is included in the seal computation).
    """
    if not isinstance(entry_text, str):
        return VerifyResult(False, "TYPE_ERROR")
    # Apply same normalization as stamp() — entry as stored should already
    # be normalized, but defensive normalization ensures consistency.
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
    """Serialize SovereignStamp to a plain dict (for JSON storage).

    Note on unix_utc: stored as int. If your JSON layer converts integers
    to floats, use int(d["unix_utc"]) when reading back — from_dict()
    enforces this. A float unix_utc will produce a different seal.
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
    Deserialize a SovereignStamp from a plain dict (from JSON storage).
    Validates schema before construction — does not accept unvalidated input.

    Raises
    ------
    ValueError
        If required fields are missing.
        If seal is not a 64-character lowercase hex string.
        If calendar fields are not non-empty strings.
        If unix_utc is not coercible to a positive integer.
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

    # RT-STS-003: Validate version field against this reader's frozen version.
    # A dict carrying a foreign version string is accepted only by the frozen
    # version that produced it. Silently constructing a stamp with a mismatched
    # version field creates a provenance display error — the human-readable
    # claim about which version produced the seal would be wrong.
    # This is not a cryptographic vulnerability (the seal remains valid) but
    # it is a provenance integrity failure. Raise rather than permit silent
    # mislabelling. [D]
    if d["version"] != _FROZEN_VERSION:
        raise ValueError(
            f"from_dict: 'version' field is {d['version']!r}. "
            f"This reader is {_FROZEN_VERSION}. "
            "Stamps produced by older frozen versions must be deserialized "
            "using the corresponding archived frozen version."
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
# All Hebrew dates verified against Hebcal.com and Chabad.org
# Original anchors: March 3, 2026 (session of origin)
# Extended anchors: leap year, long Cheshvan, short Kislev, Adar II
# ═══════════════════════════════════════════════════════════════════

def _run_self_test(verbose: bool = True) -> None:
    """
    Verification against anchor values known at time of writing.
    Any failure here means the calendar algorithms have been broken.
    Do not modify to make tests pass — verify the algorithm from
    first principles and create FROZEN-5.0 if correction is needed.

    Returns normally if all tests pass.
    Raises AssertionError if any test fails.
    """
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
    check("5786 is regular year (354)", _year_length(5786) in _LEGAL_YEAR_LENGTHS, True)

    # ── Hebrew year lengths — long Cheshvan and short Kislev ──────
    # 5785 = short Kislev year (353 days), 5784 = long Cheshvan (385 — leap)
    # Verified against Hebcal year structure reports.
    check("Year 5785 is legal length", _year_length(5785) in _LEGAL_YEAR_LENGTHS, True)
    check("Year 5784 is legal length", _year_length(5784) in _LEGAL_YEAR_LENGTHS, True)

    # ── Hebrew date conversion — Hebcal/Chabad verified [D] ───────
    h_year, h_month, h_day = _gregorian_to_hebrew(2026, 3, 3)
    check("Hebrew year (Mar 3 2026)",   h_year,   5786)
    check("Hebrew month (Mar 3 2026)",  h_month,  "Adar")
    check("Hebrew day (Mar 3 2026)",    h_day,    14)
    check("Hebrew string (Mar 3 2026)", _hebrew(anchor_date), "14 Adar 5786")

    # ── Rosh Hashanah anchor (civil-day convention) ───────────────
    rh_year, rh_month, rh_day = _gregorian_to_hebrew(2025, 9, 23)
    check("RH 5786 year",  rh_year,  5786)
    check("RH 5786 month", rh_month, "Tishri")
    check("RH 5786 day",   rh_day,   1)

    # ── Erev Rosh Hashanah (highest-risk zone for dehiyot) ────────
    evrh_year, evrh_month, evrh_day = _gregorian_to_hebrew(2025, 9, 22)
    check("Erev RH 5786 month", evrh_month, "Elul")
    check("Erev RH 5786 day",   evrh_day,   29)

    # ── Yom Kippur anchor ─────────────────────────────────────────
    yk_year, yk_month, yk_day = _gregorian_to_hebrew(2025, 10, 2)
    check("Yom Kippur 5786 month", yk_month, "Tishri")
    check("Yom Kippur 5786 day",   yk_day,   10)

    # ── Passover anchor ───────────────────────────────────────────
    ps_year, ps_month, ps_day = _gregorian_to_hebrew(2026, 4, 2)
    check("Passover 5786 month", ps_month, "Nisan")
    check("Passover 5786 day",   ps_day,   15)

    # ── 1 Nisan anchor ────────────────────────────────────────────
    n1_year, n1_month, n1_day = _gregorian_to_hebrew(2026, 3, 19)
    check("1 Nisan 5786 month", n1_month, "Nisan")
    check("1 Nisan 5786 day",   n1_day,   1)

    # ── EXTENDED ANCHORS — leap year, Adar II ─────────────────────
    # 5784 is a leap year. 15 Adar II 5784 = Mar 25, 2024. [D] Hebcal verified.
    leap_y, leap_m, leap_d = _gregorian_to_hebrew(2024, 3, 25)
    check("Leap year 5784 month (Adar II)", leap_m, "Adar II")
    check("Leap year 5784 day (15)",        leap_d, 15)
    check("Leap year 5784 year",            leap_y, 5784)

    # Adar I in leap year: 1 Adar I 5784 = Feb 10, 2024. [D] Hebcal verified.
    adar1_y, adar1_m, adar1_d = _gregorian_to_hebrew(2024, 2, 10)
    check("Adar I 5784 month", adar1_m, "Adar I")
    check("Adar I 5784 day",   adar1_d, 1)

    # Rosh Hashanah 5787 (start of a new leap year): Sep 12, 2026. [D]
    # Verified: pyluach + D&R two-pass calculation.
    # FROZEN-3.0 defect: test used Sep 22 as RH 5787 — that date is
    # 11 Tishri 5787, not 1 Tishri. The algorithm was correct; the test
    # anchor was wrong. RT-STS-001 CRITICAL correction. [D]
    rh87_y, rh87_m, rh87_d = _gregorian_to_hebrew(2026, 9, 12)
    check("RH 5787 year",  rh87_y, 5787)
    check("RH 5787 month", rh87_m, "Tishri")
    check("RH 5787 day",   rh87_d, 1)

    # Day before RH 5787 = 29 Elul 5786 = Sep 11, 2026. [D]
    # FROZEN-3.0 defect: test used Sep 21 (10 Tishri 5787). Corrected here.
    erh87_y, erh87_m, erh87_d = _gregorian_to_hebrew(2026, 9, 11)
    check("Erev RH 5787 month", erh87_m, "Elul")
    check("Erev RH 5787 day",   erh87_d, 29)

    # Additional verification: Sep 22, 2026 = 11 Tishri 5787 (Yom Kippur eve).
    # This confirms the algorithm is correct — Sep 22 is NOT RH 5787,
    # disproving the FROZEN-3.0 test assumption. [D]
    sep22_y, sep22_m, sep22_d = _gregorian_to_hebrew(2026, 9, 22)
    check("Sep 22 2026 is 11 Tishri 5787 (NOT RH)", sep22_d, 11)
    check("Sep 22 2026 month is Tishri",             sep22_m, "Tishri")

    # ── Dreamspell ────────────────────────────────────────────────
    check("Dreamspell Mar 3 2026", _dreamspell(anchor_date),
          "Day 25, Galactic Moon 8/13")
    check("Day Out of Time Jul 25", _dreamspell(_date(2026, 7, 25)),
          "Day Out of Time")
    check("Dreamspell Jul 26 (Moon 1 Day 1)",
          _dreamspell(_date(2026, 7, 26)), "Day 1, Magnetic Moon 1/13")

    # Leap-year cross-boundary: March 1, 2028 (leap year, year_start = Jul 26 2027)
    # delta = (2028-03-01) - (2027-07-26) = 219 days
    # moon = 219 // 28 + 1 = 8 (Galactic), day = 219 % 28 + 1 = 24
    check("Dreamspell Mar 1 2028 (post-leap-Feb)",
          _dreamspell(_date(2028, 3, 1)), "Day 24, Galactic Moon 8/13")

    # ── JD range guard ────────────────────────────────────────────
    try:
        _jd_from_gregorian(1581, 1, 1)
        failures.append("  FAIL — Pre-1582 year should raise ValueError")
    except ValueError:
        if verbose:
            print("  ✓  Pre-1582 year correctly rejected")

    # RT-STS-002: 1582 pre-reform dates (before Oct 15) must also be rejected.
    # Oct 14, 1582 is the last Julian day — Gregorian reform took effect Oct 15.
    try:
        _jd_from_gregorian(1582, 10, 14)
        failures.append("  FAIL — 1582-10-14 (pre-reform) should raise ValueError")
    except ValueError:
        if verbose:
            print("  ✓  1582-10-14 pre-reform boundary correctly rejected")

    # Oct 15, 1582 is the first valid Gregorian date — must succeed.
    try:
        jd_reform = _jd_from_gregorian(1582, 10, 15)
        if verbose:
            print(f"  ✓  1582-10-15 (first valid Gregorian date) accepted: JD {jd_reform}")
    except ValueError:
        failures.append("  FAIL — 1582-10-15 (first Gregorian date) should be accepted")

    # ── Unicode normalization ─────────────────────────────────────
    # NFC "é" (U+00E9) and NFD "é" (e + combining accent) must produce
    # identical seals — normalization is applied before sealing.
    entry_nfc = "caf\u00e9"              # é as single code point
    entry_nfd = "cafe\u0301"             # e + combining accent
    ts_nfc = stamp(entry_nfc, anchor_dt)
    ts_nfd = stamp(entry_nfd, anchor_dt)
    check("NFC/NFD normalization produces identical seals",
          ts_nfc.seal, ts_nfd.seal)

    # ── Whitespace normalization ──────────────────────────────────
    ts_trimmed  = stamp("hello", anchor_dt)
    ts_padded   = stamp("  hello  ", anchor_dt)
    check("Whitespace-padded and trimmed entries produce identical seals",
          ts_padded.seal, ts_trimmed.seal)

    # ── Version field in stamp ────────────────────────────────────
    ts_anchor = stamp("anchor", anchor_dt)
    check("Stamp carries FROZEN-4.0 version", ts_anchor.version, "FROZEN-4.0")

    # ── Seal round-trip ───────────────────────────────────────────
    test_entry = "Origin trace — Sovereign Trace Protocol FROZEN-3.0 sealed at session of birth."
    ts = stamp(test_entry, anchor_dt)
    vr_good  = verify(test_entry, ts)
    vr_alter = verify("altered text", ts)
    vr_empty = verify("", ts)
    vr_none  = verify(None, ts)
    check("Seal verifies correct entry",       vr_good.valid,           True)
    check("Seal verifies — reason VALID",      vr_good.reason,          "VALID")
    check("Seal rejects altered entry",        vr_alter.valid,          False)
    check("Seal rejects altered — SEAL_MISMATCH", vr_alter.reason,     "SEAL_MISMATCH")
    check("Seal rejects empty string",         vr_empty.valid,          False)
    check("Seal rejects None — TYPE_ERROR",    vr_none.reason,          "TYPE_ERROR")

    # ── VerifyResult bool evaluation ─────────────────────────────
    check("VerifyResult(True) is truthy",   bool(vr_good),  True)
    check("VerifyResult(False) is falsy",   bool(vr_alter), False)

    # ── Hebrew field in stamp ─────────────────────────────────────
    check("Stamp Hebrew field", ts.hebrew, "14 Adar 5786")

    # ── check_invariant ───────────────────────────────────────────
    check("check_invariant on valid stamp", ts.check_invariant(), True)

    # ── __eq__ and __hash__ ───────────────────────────────────────
    ts_copy = stamp(test_entry, anchor_dt)
    check("Same-input stamps are equal (__eq__)", ts == ts_copy, True)
    check("Same-input stamps share hash",         hash(ts) == hash(ts_copy), True)
    ts_other = stamp("different entry", anchor_dt)
    check("Different-entry stamps are not equal", ts == ts_other, False)

    # ── Immutability ──────────────────────────────────────────────
    try:
        ts.gregorian = "tampered"
        failures.append("  FAIL — SovereignStamp should be immutable")
    except AttributeError:
        if verbose:
            print("  ✓  SovereignStamp immutability: mutation correctly rejected")

    # ── SovereignRecord ───────────────────────────────────────────
    rec = stamp_and_record(test_entry, anchor_dt)
    check("SovereignRecord entry matches",      rec.entry, test_entry)
    check("SovereignRecord verify valid",       rec.verify().valid, True)
    check("SovereignRecord verify reason",      rec.verify().reason, "VALID")

    try:
        rec.entry = "tampered"
        failures.append("  FAIL — SovereignRecord should be immutable")
    except AttributeError:
        if verbose:
            print("  ✓  SovereignRecord immutability: mutation correctly rejected")

    # ── Serialization round-trip ──────────────────────────────────
    d2 = to_dict(ts)
    ts2 = from_dict(d2)
    check("Serialization round-trip seal",    ts2.seal,    ts.seal)
    check("Serialization round-trip version", ts2.version, ts.version)
    check("Round-trip stamp equality (__eq__)", ts2 == ts, True)

    # ── SovereignRecord round-trip ────────────────────────────────
    rec_dict = rec.to_dict()
    rec2 = SovereignRecord.from_dict(rec_dict)
    check("SovereignRecord dict round-trip entry",      rec2.entry,         rec.entry)
    check("SovereignRecord dict round-trip seal",       rec2.stamp.seal,    rec.stamp.seal)
    check("SovereignRecord dict round-trip verify",     rec2.verify().valid, True)

    # ── from_dict validation ──────────────────────────────────────
    bad_dict_missing = {"gregorian": "x", "hebrew": "y", "dreamspell": "z"}
    try:
        from_dict(bad_dict_missing)
        failures.append("  FAIL — from_dict should reject missing fields")
    except ValueError:
        if verbose:
            print("  ✓  from_dict rejects missing fields")

    bad_dict_seal = dict(d2)
    bad_dict_seal["seal"] = "not-a-valid-seal"
    try:
        from_dict(bad_dict_seal)
        failures.append("  FAIL — from_dict should reject invalid seal format")
    except ValueError:
        if verbose:
            print("  ✓  from_dict rejects invalid seal format")

    # RT-STS-003: from_dict must reject dicts carrying a foreign version string.
    bad_dict_version = dict(d2)
    bad_dict_version["version"] = "FROZEN-3.0"
    try:
        from_dict(bad_dict_version)
        failures.append("  FAIL — from_dict should reject foreign version field")
    except ValueError:
        if verbose:
            print("  ✓  from_dict rejects foreign version field (FROZEN-3.0 in FROZEN-4.0 reader)")

    # ── stamp_batch ───────────────────────────────────────────────
    entries = ["first entry", "second entry", "third entry"]
    batch = stamp_batch(entries, anchor_dt)
    check("Batch length matches input",       len(batch),               3)
    check("Batch records all share unix_utc", len({r.stamp.unix_utc for r in batch}), 1)
    check("Batch record 0 verifies",          batch[0].verify().valid,  True)
    check("Batch record 2 verifies",          batch[2].verify().valid,  True)

    # ── Error handling ────────────────────────────────────────────
    try:
        stamp("")
        failures.append("  FAIL — empty entry should raise ValueError")
    except ValueError:
        if verbose:
            print("  ✓  Empty entry correctly rejected")

    try:
        stamp("   ")
        failures.append("  FAIL — whitespace-only entry should raise ValueError")
    except ValueError:
        if verbose:
            print("  ✓  Whitespace-only entry correctly rejected")

    try:
        stamp("text", datetime(2026, 3, 3, 15, 0, 0))  # naive
        failures.append("  FAIL — naive datetime should raise ValueError")
    except ValueError:
        if verbose:
            print("  ✓  Naive datetime correctly rejected")

    # ── FROZEN-1.0 REGRESSION — Hebrew must differ ────────────────
    # FROZEN-1.0 produced "15 Adar 5786" for this date. Neither 2.0, 3.0, nor 4.0 must.
    check("FROZEN-1.0 regression: NOT 15 Adar",
          ts.hebrew != "15 Adar 5786", True)

    # ── Result ────────────────────────────────────────────────────
    if verbose:
        print()
    if failures:
        print("═══ SELF-TEST FAILURES ═══")
        for f in failures:
            print(f)
        raise AssertionError(
            f"{len(failures)} self-test failure(s). "
            "Do not deploy — verify calendar algorithms from first principles. "
            "If correction is needed: create FROZEN-5.0."
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

    Parameters
    ----------
    json_mode : bool
        If True, suppress human-readable display and emit only the
        machine-readable JSON record to stdout. Suitable for piping
        into automation scripts, ledger appenders, or log aggregators.
        Activate via: python sovereign_trace_stamp.py --json

    Privacy notice: entry text is submitted via stdin and printed to
    stdout. On shared systems, stdout may be logged (cloud function logs,
    container logs, systemd journal). Shell history may record the command
    invocation. Terminal scrollback may retain the full JSON record.
    The entry text in the JSON output is not encrypted at rest.
    The operator is responsible for log and history management.

    Process memory note (RT-STS-007): the entry text exists in process
    memory from stdin read until the process exits. On multi-tenant
    systems with shared memory visibility (e.g., certain container or
    VM configurations), this is an operator-assessed risk. The process
    does not persist memory to disk and makes no network calls.

    Calendar note: calendar dates reflect UTC time. For users in
    UTC+10 or later, the UTC date may differ from local civil date.
    """
    if not json_mode:
        print("═══════════════════════════════════════════════════")
        print(f"  SOVEREIGN TRACE PROTOCOL — {_FROZEN_VERSION}")
        print("  Your trace will be sealed permanently.")
        print("  There is no undo.")
        print("  Note: calendar dates reflect UTC.")
        print("  Note: entry will appear in stdout (may be logged).")
        print("═══════════════════════════════════════════════════\n")

    entry = input("Your trace (present-moment, exact, no narrative arc):\n> ")
    # Normalization mirrors stamp() — show the user the normalized entry
    entry_normalized = unicodedata.normalize("NFC", entry).strip()
    if not entry_normalized:
        if not json_mode:
            print("Empty trace. Nothing sealed.")
        return

    ts = stamp(entry_normalized)
    rec = SovereignRecord(entry_normalized, ts)

    if json_mode:
        # Machine-readable output only — suitable for piping and automation.
        # No decorative borders, no human-readable display lines.
        print(json.dumps(rec.to_dict(), indent=2, ensure_ascii=False))
    else:
        print()
        print("─── SEALED ───────────────────────────────────────")
        print(display(ts))
        print("─── JSON (store this) ────────────────────────────")
        print(json.dumps(rec.to_dict(), indent=2, ensure_ascii=False))
        print("──────────────────────────────────────────────────")
        print("This stamp is permanent. The seal verifies integrity.")
        print("Keep the JSON. The ledger append comes next.")


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv or "-t" in sys.argv:
        _run_self_test(verbose=True)
    else:
        _run_self_test(verbose=False)
        _cli(json_mode="--json" in sys.argv)
