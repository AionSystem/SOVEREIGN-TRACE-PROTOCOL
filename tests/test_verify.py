#!/usr/bin/env python3
"""
verify() — all code paths, normalization application, reason codes.
"""
import pytest
import unicodedata
from datetime import datetime, timezone

from sovereign_trace_stamp import (
    stamp,
    verify,
    VerifyResult,
    SovereignStamp,
)


class TestVerifyCorrectEntry:
    """Test verify() with correct entry."""

    def test_verify_correct_entry_valid_true(self, anchor_entry, anchor_stamp):
        result = verify(anchor_entry, anchor_stamp)
        assert result.valid is True

    def test_verify_correct_entry_reason_valid(self, anchor_entry, anchor_stamp):
        result = verify(anchor_entry, anchor_stamp)
        assert result.reason == "VALID"

    def test_verify_returns_verify_result(self, anchor_entry, anchor_stamp):
        result = verify(anchor_entry, anchor_stamp)
        assert isinstance(result, VerifyResult)

    def test_verify_evaluates_as_bool_true_on_valid(self, anchor_entry, anchor_stamp):
        result = verify(anchor_entry, anchor_stamp)
        assert result  # truthy


class TestVerifyMismatchedEntry:
    """Test verify() with altered/incorrect entries."""

    def test_verify_evaluates_as_bool_false_on_mismatch(self, anchor_entry, anchor_stamp):
        result = verify("tampered entry", anchor_stamp)
        assert not result  # falsy

    def test_verify_altered_entry_false(self, anchor_entry, anchor_stamp):
        result = verify(anchor_entry + " extra", anchor_stamp)
        assert result.valid is False

    def test_verify_altered_entry_seal_mismatch(self, anchor_entry, anchor_stamp):
        result = verify(anchor_entry + " extra", anchor_stamp)
        assert result.reason == "SEAL_MISMATCH"

    def test_verify_extra_char_at_end_mismatch(self, anchor_entry, anchor_stamp):
        result = verify(anchor_entry + "X", anchor_stamp)
        assert result.valid is False
        assert result.reason == "SEAL_MISMATCH"

    def test_verify_extra_char_at_start_mismatch(self, anchor_entry, anchor_stamp):
        result = verify("X" + anchor_entry, anchor_stamp)
        assert result.valid is False
        assert result.reason == "SEAL_MISMATCH"

    def test_verify_case_change_mismatch(self, anchor_entry, anchor_stamp):
        # Change case of first character if it's alphabetic
        if anchor_entry and anchor_entry[0].isalpha():
            altered = anchor_entry[0].upper() + anchor_entry[1:] if anchor_entry[0].islower() else anchor_entry[0].lower() + anchor_entry[1:]
            result = verify(altered, anchor_stamp)
            assert result.valid is False
            assert result.reason == "SEAL_MISMATCH"

    def test_verify_empty_string_mismatch(self, anchor_stamp):
        result = verify("", anchor_stamp)
        assert result.valid is False
        # Empty string normalizes to empty, which won't match a non-empty seal
        assert result.reason == "SEAL_MISMATCH"

    def test_verify_whitespace_only_mismatch(self, anchor_stamp):
        result = verify("   ", anchor_stamp)
        assert result.valid is False
        # Whitespace-only normalizes to empty, which won't match
        assert result.reason == "SEAL_MISMATCH"


class TestVerifyTypeErrors:
    """Test verify() with wrong types."""

    def test_verify_none_type_error(self, anchor_stamp):
        result = verify(None, anchor_stamp)
        assert result.valid is False
        assert result.reason == "TYPE_ERROR"

    def test_verify_int_type_error(self, anchor_stamp):
        result = verify(12345, anchor_stamp)
        assert result.valid is False
        assert result.reason == "TYPE_ERROR"

    def test_verify_bytes_type_error(self, anchor_stamp):
        result = verify(b"bytes entry", anchor_stamp)
        assert result.valid is False
        assert result.reason == "TYPE_ERROR"

    def test_verify_list_type_error(self, anchor_stamp):
        result = verify(["list", "entry"], anchor_stamp)
        assert result.valid is False
        assert result.reason == "TYPE_ERROR"


class TestVerifyNormalization:
    """Test verify() applies NFC normalization and strip."""

    def test_verify_applies_nfc_normalization(self, anchor_entry, anchor_dt):
        # Create a stamp with NFC-normalized entry
        ts = stamp(anchor_entry, anchor_dt)
        
        # Create NFD version of the same entry
        nfd_entry = unicodedata.normalize("NFD", anchor_entry)
        
        # NFD entry should verify against NFC-sealed stamp
        result = verify(nfd_entry, ts)
        assert result.valid is True
        assert result.reason == "VALID"

    def test_verify_applies_strip(self, anchor_entry, anchor_dt):
        # Create a stamp with stripped entry
        ts = stamp(anchor_entry, anchor_dt)
        
        # Padded entry should verify against stripped-sealed stamp
        padded_entry = "  " + anchor_entry + "  "
        result = verify(padded_entry, ts)
        assert result.valid is True
        assert result.reason == "VALID"


class TestVerifyWrongStamp:
    """Test verify() with wrong stamp for entry."""

    def test_verify_wrong_stamp_for_entry_mismatch(self, anchor_entry, anchor_dt):
        # Create two different stamps
        ts1 = stamp(anchor_entry, anchor_dt)
        ts2 = stamp("different entry", anchor_dt)
        
        # Entry 1 verified against stamp 2 should fail
        result = verify(anchor_entry, ts2)
        assert result.valid is False
        assert result.reason == "SEAL_MISMATCH"

    def test_verify_swapped_entries_mismatch(self, anchor_dt):
        entry_a = "Entry A"
        entry_b = "Entry B"
        
        ts_a = stamp(entry_a, anchor_dt)
        ts_b = stamp(entry_b, anchor_dt)
        
        # Entry A against stamp B should fail
        result = verify(entry_a, ts_b)
        assert result.valid is False
        assert result.reason == "SEAL_MISMATCH"


class TestVerifyNoRaise:
    """Test verify() does not raise on any string input."""

    def test_verify_does_not_raise_on_any_string(self, anchor_stamp):
        # Should not raise, just return VerifyResult
        result = verify("any string at all!@#$%", anchor_stamp)
        assert isinstance(result, VerifyResult)


class TestVerifyTamperedFields:
    """Test verify() detects tampered calendar fields."""

    def test_verify_tampered_gregorian_mismatch(self, anchor_entry, anchor_stamp):
        # Manually create a stamp with tampered gregorian field
        tampered = SovereignStamp(
            gregorian="January 1, 2000",  # Wrong date
            hebrew=anchor_stamp.hebrew,
            dreamspell=anchor_stamp.dreamspell,
            unix_utc=anchor_stamp.unix_utc,
            seal=anchor_stamp.seal,
            version=anchor_stamp.version,
        )
        result = verify(anchor_entry, tampered)
        # The seal was computed with original gregorian, so verification fails
        assert result.valid is False
        assert result.reason == "SEAL_MISMATCH"

    def test_verify_tampered_hebrew_mismatch(self, anchor_entry, anchor_stamp):
        tampered = SovereignStamp(
            gregorian=anchor_stamp.gregorian,
            hebrew="1 Tishri 5700",  # Wrong Hebrew date
            dreamspell=anchor_stamp.dreamspell,
            unix_utc=anchor_stamp.unix_utc,
            seal=anchor_stamp.seal,
            version=anchor_stamp.version,
        )
        result = verify(anchor_entry, tampered)
        assert result.valid is False
        assert result.reason == "SEAL_MISMATCH"

    def test_verify_tampered_dreamspell_mismatch(self, anchor_entry, anchor_stamp):
        tampered = SovereignStamp(
            gregorian=anchor_stamp.gregorian,
            hebrew=anchor_stamp.hebrew,
            dreamspell="Day 1, Galactic Moon 1/13",  # Wrong Dreamspell
            unix_utc=anchor_stamp.unix_utc,
            seal=anchor_stamp.seal,
            version=anchor_stamp.version,
        )
        result = verify(anchor_entry, tampered)
        assert result.valid is False
        assert result.reason == "SEAL_MISMATCH"

    def test_verify_tampered_unix_utc_mismatch(self, anchor_entry, anchor_stamp):
        tampered = SovereignStamp(
            gregorian=anchor_stamp.gregorian,
            hebrew=anchor_stamp.hebrew,
            dreamspell=anchor_stamp.dreamspell,
            unix_utc=1234567890,  # Wrong timestamp
            seal=anchor_stamp.seal,
            version=anchor_stamp.version,
        )
        result = verify(anchor_entry, tampered)
        assert result.valid is False
        assert result.reason == "SEAL_MISMATCH"


# Hypothesis tests would go here if hypothesis is available
try:
    from hypothesis import given, strategies as st
    HYPOTHESIS_AVAILABLE = True
except ImportError:
    HYPOTHESIS_AVAILABLE = False


@pytest.mark.skipif(not HYPOTHESIS_AVAILABLE, reason="hypothesis not installed")
class TestVerifyHypothesis:
    """Hypothesis property-based tests for verify()."""

    @given(
        entry=st.text(min_size=1, max_size=100).filter(lambda s: s.strip()),
        dt=st.datetimes(
            min_value=datetime(2000, 1, 1),  # Safe range to avoid algorithm limits
            max_value=datetime(3000, 12, 31),
        ).map(lambda d: d.replace(tzinfo=timezone.utc))
    )
    def test_verify_always_valid_for_original_entry(self, entry, dt):
        """For any entry + dt, stamp then verify always returns True."""
        ts = stamp(entry, dt)
        result = verify(entry, ts)
        assert result.valid is True

    @given(
        entry_a=st.text(min_size=1, max_size=50).filter(lambda s: s.strip()),
        entry_b=st.text(min_size=1, max_size=50).filter(lambda s: s.strip()),
        dt=st.datetimes(
            min_value=datetime(2000, 1, 1),
            max_value=datetime(3000, 12, 31),
        ).map(lambda d: d.replace(tzinfo=timezone.utc))
    )
    def test_verify_always_invalid_for_different_entry(self, entry_a, entry_b, dt):
        """For any two distinct entries, verify(entry_b, stamp(entry_a)) returns False."""
        # Ensure entries are different
        assume(entry_a != entry_b)
        ts_a = stamp(entry_a, dt)
        result = verify(entry_b, ts_a)
        assert result.valid is False

    @given(
        non_str=st.one_of(
            st.none(),
            st.integers(),
            st.floats(),
            st.booleans(),
            st.lists(st.text()),
            st.dictionaries(st.text(), st.text()),
            st.binary(),
        ),
    )
    def test_verify_type_error_for_non_string(self, non_str):
        """For any non-str input, reason is TYPE_ERROR."""
        # Use a fixed safe datetime to avoid hypothesis generating dates that trigger algorithm limits
        dt = datetime(2026, 3, 3, tzinfo=timezone.utc)
        ts = stamp("test", dt)
        result = verify(non_str, ts)
        assert result.reason == "TYPE_ERROR"


# Need to import assume for hypothesis tests
if HYPOTHESIS_AVAILABLE:
    from hypothesis import assume
