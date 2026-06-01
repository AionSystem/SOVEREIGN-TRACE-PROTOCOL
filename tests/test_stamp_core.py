"""
Core `stamp()` function behavior — the primary public interface.

Tests cover: return type, field correctness, determinism, seal format,
version constant, and basic invariant checking.
"""
import os
import sys
import pytest
from datetime import datetime, timezone

# Add stamp directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'stamp'))

from sovereign_trace_stamp import stamp, SovereignStamp, _FROZEN_VERSION


class TestStampReturns:
    """Test that stamp() returns correct type and structure."""

    def test_stamp_returns_sovereign_stamp(self, anchor_entry, anchor_dt):
        """stamp() returns a SovereignStamp instance."""
        result = stamp(anchor_entry, anchor_dt)
        assert isinstance(result, SovereignStamp)

    def test_stamp_all_fields_non_empty(self, anchor_stamp):
        """All string fields in stamp are non-empty."""
        assert anchor_stamp.gregorian
        assert anchor_stamp.hebrew
        assert anchor_stamp.dreamspell
        assert anchor_stamp.seal
        assert anchor_stamp.version

    def test_stamp_check_invariant_passes(self, anchor_stamp):
        """anchor_stamp passes check_invariant()."""
        assert anchor_stamp.check_invariant() is True


class TestStampFields:
    """Test individual field correctness."""

    def test_stamp_gregorian_field_correct(self, anchor_stamp, known_gregorian):
        """Gregorian field matches expected value."""
        assert anchor_stamp.gregorian == known_gregorian

    def test_stamp_hebrew_field_correct(self, anchor_stamp, known_hebrew):
        """Hebrew field matches expected value [D]."""
        assert anchor_stamp.hebrew == known_hebrew

    def test_stamp_dreamspell_field_correct(self, anchor_stamp, known_dreamspell):
        """Dreamspell field matches expected value."""
        assert anchor_stamp.dreamspell == known_dreamspell

    def test_stamp_unix_utc_is_int(self, anchor_stamp):
        """unix_utc is an integer, not float."""
        assert isinstance(anchor_stamp.unix_utc, int)

    def test_stamp_unix_utc_is_positive(self, anchor_stamp):
        """unix_utc is a positive integer."""
        assert anchor_stamp.unix_utc > 0

    def test_stamp_unix_utc_matches_anchor(self, anchor_stamp, known_unix_utc):
        """unix_utc matches expected anchor timestamp."""
        assert anchor_stamp.unix_utc == known_unix_utc

    def test_stamp_seal_is_64_char_lowercase_hex(self, anchor_stamp):
        """Seal is exactly 64 lowercase hex characters."""
        import re
        assert len(anchor_stamp.seal) == 64
        assert re.match(r'^[0-9a-f]{64}$', anchor_stamp.seal)

    def test_stamp_version_is_frozen_4(self, anchor_stamp):
        """Version field is FROZEN-4.0."""
        assert anchor_stamp.version == "FROZEN-4.0"


class TestStampDeterminism:
    """Test deterministic behavior of stamp()."""

    def test_stamp_deterministic_same_entry_same_dt(self, anchor_entry, anchor_dt):
        """Same entry + same dt produces identical seal."""
        s1 = stamp(anchor_entry, anchor_dt)
        s2 = stamp(anchor_entry, anchor_dt)
        assert s1.seal == s2.seal

    def test_stamp_deterministic_multiple_calls(self, anchor_entry, anchor_dt):
        """Multiple calls with same input produce same seal."""
        seals = [stamp(anchor_entry, anchor_dt).seal for _ in range(10)]
        assert len(set(seals)) == 1

    def test_stamp_different_entries_different_seals(self, anchor_dt):
        """Different entries produce different seals."""
        s1 = stamp("entry one", anchor_dt)
        s2 = stamp("entry two", anchor_dt)
        assert s1.seal != s2.seal

    def test_stamp_different_dt_different_seals(self, anchor_entry):
        """Different datetimes produce different seals."""
        dt1 = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
        dt2 = datetime(2026, 3, 3, 15, 0, 1, tzinfo=timezone.utc)
        s1 = stamp(anchor_entry, dt1)
        s2 = stamp(anchor_entry, dt2)
        assert s1.seal != s2.seal

    def test_stamp_one_second_apart_different_seals(self, anchor_entry, anchor_dt):
        """Datetimes one second apart produce different seals."""
        from datetime import timedelta
        dt2 = anchor_dt + timedelta(seconds=1)
        s1 = stamp(anchor_entry, anchor_dt)
        s2 = stamp(anchor_entry, dt2)
        assert s1.seal != s2.seal


class TestStampDatetimeParameter:
    """Test dt parameter handling."""

    def test_stamp_without_dt_uses_utc_now(self, anchor_entry):
        """Omitting dt uses datetime.now(timezone.utc)."""
        before = datetime.now(timezone.utc)
        s = stamp(anchor_entry)
        after = datetime.now(timezone.utc)
        
        # unix_utc should be within the time window (comparing ints to floats)
        assert int(before.timestamp()) <= s.unix_utc <= int(after.timestamp())

    def test_stamp_with_dt_uses_provided_dt_exactly(self, anchor_entry, anchor_dt):
        """Providing dt uses that exact datetime."""
        s = stamp(anchor_entry, anchor_dt)
        assert s.unix_utc == int(anchor_dt.timestamp())


class TestStampUnixUtcTruncation:
    """Test unix_utc truncation behavior."""

    def test_stamp_unix_utc_is_truncated_not_rounded(self, anchor_entry):
        """Microseconds are truncated, not rounded."""
        # Create datetime with 999999 microseconds
        dt = datetime(2026, 3, 3, 15, 0, 5, 999999, tzinfo=timezone.utc)
        s = stamp(anchor_entry, dt)
        # Should truncate to 5 seconds, not round to 6
        expected = int(dt.timestamp())  # This truncates
        assert s.unix_utc == expected

    def test_stamp_two_within_same_second_share_unix_utc(self, anchor_entry):
        """Two datetimes within same second share unix_utc."""
        dt1 = datetime(2026, 3, 3, 15, 0, 5, 0, tzinfo=timezone.utc)
        dt2 = datetime(2026, 3, 3, 15, 0, 5, 999999, tzinfo=timezone.utc)
        s1 = stamp(anchor_entry, dt1)
        s2 = stamp(anchor_entry, dt2)
        assert s1.unix_utc == s2.unix_utc


class TestStampVariousEntries:
    """Parametrized tests over various entry types."""

    @pytest.mark.parametrize("entry", [
        "simple ascii text",
        "Unicode: café résumé naïve",
        "Emoji: hello 🌍 world 🚀",
        "Long text: " + "x" * 1000,
        "single",
        "123456789",
        "Mixed scripts: English עברית العربية 中文",
        "Tab\tcharacter",
        "Newline\ncharacter",
        "Special chars: !@#$%^&*()",
    ])
    def test_stamp_various_entries(self, entry, anchor_dt):
        """Stamp works correctly with various entry types."""
        s = stamp(entry, anchor_dt)
        assert isinstance(s, SovereignStamp)
        assert s.seal
        assert s.version == _FROZEN_VERSION


class TestStampHypothesis:
    """Hypothesis property-based tests for stamp()."""

    def test_stamp_determinism_property(self, anchor_entry, anchor_dt):
        """For any valid entry + dt, stamp twice → same seal."""
        from hypothesis import given
        from hypothesis import strategies as st
        
        @given(st.text(min_size=1, max_size=100), 
               st.integers(min_value=1582, max_value=3999))
        def _test(entry, year):
            try:
                dt = datetime(year, 6, 15, 12, 0, 0, tzinfo=timezone.utc)
                s1 = stamp(entry, dt)
                s2 = stamp(entry, dt)
                assert s1.seal == s2.seal
            except ValueError:
                # Date might be invalid (e.g., pre-reform) — that's OK
                pass
        
        _test()
