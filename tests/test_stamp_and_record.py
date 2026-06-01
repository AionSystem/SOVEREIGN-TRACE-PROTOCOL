"""
test_stamp_and_record.py
stamp_and_record() — canonical {entry, stamp} pair generation.
"""
import pytest
import unicodedata
from datetime import datetime, timezone
from sovereign_trace import stamp_and_record, SovereignRecord, SovereignStamp


class TestStampAndRecordStandard:
    """Standard tests for stamp_and_record()."""

    def test_returns_sovereign_record(self, anchor_entry, anchor_dt):
        record = stamp_and_record(anchor_entry, anchor_dt)
        assert isinstance(record, SovereignRecord)

    def test_entry_matches_normalized_input(self, anchor_entry, anchor_dt):
        normalized = unicodedata.normalize("NFC", anchor_entry.strip())
        record = stamp_and_record(anchor_entry, anchor_dt)
        assert record.entry == normalized

    def test_entry_is_nfc_normalized(self, anchor_dt):
        # NFD 'e' + combining acute
        entry_nfd = "Caf\u0065\u0301"
        record = stamp_and_record(entry_nfd, anchor_dt)
        assert record.entry == "Café"  # NFC form

    def test_entry_is_stripped(self, anchor_dt):
        entry_padded = "  Hello World  "
        record = stamp_and_record(entry_padded, anchor_dt)
        assert record.entry == "Hello World"

    def test_stamp_is_sovereign_stamp(self, anchor_entry, anchor_dt):
        record = stamp_and_record(anchor_entry, anchor_dt)
        assert isinstance(record.stamp, SovereignStamp)

    def test_verify_valid(self, anchor_entry, anchor_dt):
        record = stamp_and_record(anchor_entry, anchor_dt)
        result = record.verify()
        assert result.valid is True

    def test_verify_reason_valid(self, anchor_entry, anchor_dt):
        record = stamp_and_record(anchor_entry, anchor_dt)
        result = record.verify()
        assert result.reason == "VALID"

    def test_entry_matches_seal(self, anchor_entry, anchor_dt):
        record = stamp_and_record(anchor_entry, anchor_dt)
        # Verify that the stored entry matches the seal
        valid, reason = record.verify()
        assert valid is True
        assert reason == "VALID"

    def test_deterministic(self, anchor_entry, anchor_dt):
        record1 = stamp_and_record(anchor_entry, anchor_dt)
        record2 = stamp_and_record(anchor_entry, anchor_dt)
        assert record1.stamp.seal == record2.stamp.seal

    def test_none_raises_type_error(self, anchor_dt):
        with pytest.raises(TypeError):
            stamp_and_record(None, anchor_dt)

    def test_empty_raises_value_error(self, anchor_dt):
        with pytest.raises(ValueError):
            stamp_and_record("", anchor_dt)

    def test_whitespace_only_raises_value_error(self, anchor_dt):
        with pytest.raises(ValueError):
            stamp_and_record("   ", anchor_dt)

    def test_naive_dt_raises_value_error(self, anchor_entry):
        naive_dt = datetime(2026, 3, 3, 15, 0, 0)
        with pytest.raises(ValueError):
            stamp_and_record(anchor_entry, naive_dt)

    def test_entry_in_record_already_normalized(self, anchor_entry, anchor_dt):
        record = stamp_and_record(anchor_entry, anchor_dt)
        # Verifying should not require re-normalization because it's already stored normalized
        result = record.verify()
        assert result.valid is True

    def test_different_entries_different_seals(self, anchor_dt):
        record1 = stamp_and_record("Entry A", anchor_dt)
        record2 = stamp_and_record("Entry B", anchor_dt)
        assert record1.stamp.seal != record2.stamp.seal

    def test_with_dt_uses_provided_dt(self, anchor_entry, anchor_dt):
        record = stamp_and_record(anchor_entry, anchor_dt)
        assert record.stamp.unix_utc == int(anchor_dt.timestamp())


class TestStampAndRecordHypothesis:
    """Hypothesis property-based tests for stamp_and_record()."""

    def test_stamp_and_record_always_verifies(self, hypothesis_entry_dt):
        entry, dt = hypothesis_entry_dt
        try:
            record = stamp_and_record(entry, dt)
            assert record.verify().valid is True
        except (ValueError, TypeError):
            # If input is invalid (e.g., whitespace only), it should raise, not return invalid
            pytest.skip("Input invalid by design")

    def test_stored_entry_matches_normalized_form(self, hypothesis_entry_dt):
        entry, dt = hypothesis_entry_dt
        try:
            record = stamp_and_record(entry, dt)
            expected = unicodedata.normalize("NFC", entry.strip())
            assert record.entry == expected
        except (ValueError, TypeError):
            pytest.skip("Input invalid by design")
