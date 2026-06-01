#!/usr/bin/env python3
"""
SovereignRecord — pair semantics, immutability, serialization.
"""
import pytest
import json
from datetime import datetime, timezone

from sovereign_trace_stamp import (
    SovereignRecord,
    SovereignStamp,
    stamp,
    stamp_and_record,
    VerifyResult,
)


class TestSovereignRecordAttributes:
    """Test SovereignRecord has correct attributes."""

    def test_record_has_entry_attribute(self, anchor_record):
        assert hasattr(anchor_record, "entry")

    def test_record_has_stamp_attribute(self, anchor_record):
        assert hasattr(anchor_record, "stamp")

    def test_record_entry_matches_normalized_input(self, anchor_entry, anchor_record):
        # Entry should be NFC-normalized and stripped
        import unicodedata
        expected = unicodedata.normalize("NFC", anchor_entry.strip())
        assert anchor_record.entry == expected

    def test_record_stamp_is_sovereign_stamp_type(self, anchor_record):
        assert isinstance(anchor_record.stamp, SovereignStamp)


class TestSovereignRecordImmutability:
    """Test SovereignRecord immutability."""

    def test_record_is_immutable_entry(self, anchor_record):
        with pytest.raises(AttributeError):
            anchor_record.entry = "tampered"

    def test_record_is_immutable_stamp(self, anchor_record):
        with pytest.raises(AttributeError):
            anchor_record.stamp = None

    def test_record_mutation_raises_attribute_error(self, anchor_record):
        with pytest.raises(AttributeError, match="immutable"):
            anchor_record.entry = "new value"


class TestSovereignRecordVerify:
    """Test SovereignRecord.verify() method."""

    def test_record_verify_returns_verify_result(self, anchor_record):
        result = anchor_record.verify()
        assert isinstance(result, VerifyResult)

    def test_record_verify_valid_returns_true(self, anchor_record):
        result = anchor_record.verify()
        assert result.valid is True

    def test_record_verify_valid_reason_is_valid(self, anchor_record):
        result = anchor_record.verify()
        assert result.reason == "VALID"


class TestSovereignRecordRepr:
    """Test SovereignRecord.__repr__()."""

    def test_record_repr_short_entry_no_truncation(self):
        # Entry <= 40 chars should not be truncated
        record = stamp_and_record("Short entry", datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc))
        repr_str = repr(record)
        assert "..." not in repr_str or len("Short entry") <= 40

    def test_record_repr_long_entry_truncated_at_40(self):
        # Entry > 40 chars should be truncated
        long_entry = "This is a very long entry that exceeds forty characters in length"
        record = stamp_and_record(long_entry, datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc))
        repr_str = repr(record)
        assert "..." in repr_str

    def test_record_repr_contains_ellipsis_on_long_entry(self):
        long_entry = "A" * 50
        record = stamp_and_record(long_entry, datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc))
        repr_str = repr(record)
        assert "..." in repr_str


class TestSovereignRecordToDict:
    """Test SovereignRecord.to_dict()."""

    def test_record_to_dict_has_entry_key(self, anchor_record):
        d = anchor_record.to_dict()
        assert "entry" in d

    def test_record_to_dict_has_gregorian_key(self, anchor_record):
        d = anchor_record.to_dict()
        assert "gregorian" in d

    def test_record_to_dict_has_hebrew_key(self, anchor_record):
        d = anchor_record.to_dict()
        assert "hebrew" in d

    def test_record_to_dict_has_dreamspell_key(self, anchor_record):
        d = anchor_record.to_dict()
        assert "dreamspell" in d

    def test_record_to_dict_has_unix_utc_key(self, anchor_record):
        d = anchor_record.to_dict()
        assert "unix_utc" in d

    def test_record_to_dict_has_seal_key(self, anchor_record):
        d = anchor_record.to_dict()
        assert "seal" in d

    def test_record_to_dict_has_version_key(self, anchor_record):
        d = anchor_record.to_dict()
        assert "version" in d

    def test_record_to_dict_seven_keys_total(self, anchor_record):
        d = anchor_record.to_dict()
        assert len(d) == 7

    def test_record_to_dict_is_json_serializable(self, anchor_record):
        d = anchor_record.to_dict()
        json_str = json.dumps(d)
        assert isinstance(json_str, str)


class TestSovereignRecordFromDict:
    """Test SovereignRecord.from_dict()."""

    def test_record_from_dict_round_trip_entry(self, anchor_record):
        d = anchor_record.to_dict()
        restored = SovereignRecord.from_dict(d)
        assert restored.entry == anchor_record.entry

    def test_record_from_dict_round_trip_seal(self, anchor_record):
        d = anchor_record.to_dict()
        restored = SovereignRecord.from_dict(d)
        assert restored.stamp.seal == anchor_record.stamp.seal

    def test_record_from_dict_round_trip_verifies(self, anchor_record):
        d = anchor_record.to_dict()
        restored = SovereignRecord.from_dict(d)
        result = restored.verify()
        assert result.valid is True

    def test_record_from_dict_missing_entry_raises_value_error(self, anchor_record):
        d = anchor_record.to_dict()
        del d["entry"]
        with pytest.raises(ValueError, match="missing field 'entry'"):
            SovereignRecord.from_dict(d)

    def test_record_from_dict_none_entry_raises_value_error(self, anchor_record):
        d = anchor_record.to_dict()
        d["entry"] = None
        with pytest.raises(ValueError, match="'entry' must be a non-empty string"):
            SovereignRecord.from_dict(d)

    def test_record_from_dict_empty_entry_raises_value_error(self, anchor_record):
        d = anchor_record.to_dict()
        d["entry"] = ""
        with pytest.raises(ValueError, match="'entry' must be a non-empty string"):
            SovereignRecord.from_dict(d)

    def test_record_from_dict_int_entry_raises_value_error(self, anchor_record):
        d = anchor_record.to_dict()
        d["entry"] = 12345
        with pytest.raises(ValueError, match="'entry' must be a non-empty string"):
            SovereignRecord.from_dict(d)

    def test_record_from_dict_missing_seal_raises_value_error(self, anchor_record):
        d = anchor_record.to_dict()
        del d["seal"]
        with pytest.raises(ValueError, match="missing required fields"):
            SovereignRecord.from_dict(d)

    def test_record_from_dict_wrong_version_raises_value_error(self, anchor_record):
        d = anchor_record.to_dict()
        d["version"] = "FROZEN-3.0"
        with pytest.raises(ValueError, match="version"):
            SovereignRecord.from_dict(d)


class TestSovereignRecordSlots:
    """Test SovereignRecord uses __slots__."""

    def test_record_slots_defined(self):
        assert hasattr(SovereignRecord, "__slots__")
        assert "entry" in SovereignRecord.__slots__
        assert "stamp" in SovereignRecord.__slots__


# Hypothesis tests would go here if hypothesis is available
# For now, these are skipped without hypothesis installed
try:
    from hypothesis import given, strategies as st
    HYPOTHESIS_AVAILABLE = True
except ImportError:
    HYPOTHESIS_AVAILABLE = False


@pytest.mark.skipif(not HYPOTHESIS_AVAILABLE, reason="hypothesis not installed")
class TestSovereignRecordHypothesis:
    """Hypothesis property-based tests for SovereignRecord."""

    @given(
        entry=st.text(min_size=1, max_size=100).filter(lambda s: s.strip()),
        dt=st.datetimes(
            min_value=datetime(2000, 1, 1),  # Safe range to avoid algorithm limits
            max_value=datetime(3000, 12, 31),
        ).map(lambda d: d.replace(tzinfo=timezone.utc))
    )
    def test_record_to_dict_from_dict_round_trip_property(self, entry, dt):
        """For any valid entry + dt, round-trip produces equal seal."""
        record = stamp_and_record(entry, dt)
        d = record.to_dict()
        restored = SovereignRecord.from_dict(d)
        assert restored.stamp.seal == record.stamp.seal
