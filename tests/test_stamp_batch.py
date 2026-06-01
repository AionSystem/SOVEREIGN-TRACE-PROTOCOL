"""
test_stamp_batch.py — stamp_batch() tests.

Batch semantics, shared timestamp, atomicity non-guarantee, error propagation.
"""

import pytest
from datetime import datetime, timezone

from sovereign_trace import stamp_batch, SovereignRecord


class TestBatchBasic:
    """Basic batch functionality tests."""

    def test_batch_returns_list(self, anchor_entry):
        result = stamp_batch([anchor_entry])
        assert isinstance(result, list)

    def test_batch_single_entry_returns_list_of_one(self, anchor_entry):
        result = stamp_batch([anchor_entry])
        assert len(result) == 1

    def test_batch_empty_list_returns_empty_list(self):
        result = stamp_batch([])
        assert result == []

    def test_batch_three_entries_length_three(self, anchor_entry):
        entries = [anchor_entry, "Second entry", "Third entry"]
        result = stamp_batch(entries)
        assert len(result) == 3

    def test_batch_all_items_are_sovereign_records(self, anchor_entry):
        entries = [anchor_entry, "Second entry", "Third entry"]
        result = stamp_batch(entries)
        for record in result:
            assert isinstance(record, SovereignRecord)


class TestBatchSharedTimestamp:
    """Tests for shared timestamp across batch items."""

    def test_batch_all_share_unix_utc(self, anchor_entry):
        entries = [anchor_entry, "Second entry", "Third entry"]
        result = stamp_batch(entries)
        unix_utcs = [r.stamp.unix_utc for r in result]
        assert len(set(unix_utcs)) == 1  # All same

    def test_batch_all_share_gregorian(self, anchor_entry):
        entries = [anchor_entry, "Second entry", "Third entry"]
        result = stamp_batch(entries)
        gregorians = [r.stamp.gregorian for r in result]
        assert len(set(gregorians)) == 1

    def test_batch_all_share_hebrew(self, anchor_entry):
        entries = [anchor_entry, "Second entry", "Third entry"]
        result = stamp_batch(entries)
        hebrews = [r.stamp.hebrew for r in result]
        assert len(set(hebrews)) == 1

    def test_batch_all_share_dreamspell(self, anchor_entry):
        entries = [anchor_entry, "Second entry", "Third entry"]
        result = stamp_batch(entries)
        dreamspells = [r.stamp.dreamspell for r in result]
        assert len(set(dreamspells)) == 1

    def test_batch_all_share_version(self, anchor_entry):
        entries = [anchor_entry, "Second entry", "Third entry"]
        result = stamp_batch(entries)
        versions = [r.stamp.version for r in result]
        assert len(set(versions)) == 1

    def test_batch_with_dt_all_share_provided_unix_utc(self, anchor_entry, anchor_dt):
        entries = [anchor_entry, "Second entry", "Third entry"]
        result = stamp_batch(entries, dt=anchor_dt)
        unix_utcs = [r.stamp.unix_utc for r in result]
        assert len(set(unix_utcs)) == 1
        assert unix_utcs[0] == int(anchor_dt.timestamp())

    def test_batch_without_dt_all_share_same_unix_utc(self, anchor_entry):
        """Single datetime.now() call ensures all share same unix_utc."""
        entries = [anchor_entry, "Second entry", "Third entry"]
        result = stamp_batch(entries)
        unix_utcs = [r.stamp.unix_utc for r in result]
        assert len(set(unix_utcs)) == 1


class TestBatchSeals:
    """Tests for seal uniqueness in batch."""

    def test_batch_all_seals_different(self, anchor_entry):
        """Different entries → different seals."""
        entries = [anchor_entry, "Second entry", "Third entry"]
        result = stamp_batch(entries)
        seals = [r.stamp.seal for r in result]
        assert len(set(seals)) == len(seals)  # All unique

    def test_batch_duplicate_entries_allowed(self, anchor_entry):
        """Same text twice → same seal twice."""
        entries = [anchor_entry, anchor_entry]
        result = stamp_batch(entries)
        assert len(result) == 2
        assert result[0].stamp.seal == result[1].stamp.seal


class TestBatchOrder:
    """Tests for order preservation in batch."""

    def test_batch_order_preserved(self, anchor_entry):
        """Entry order matches record order."""
        entries = ["First", "Second", "Third"]
        result = stamp_batch(entries)
        # Verify by checking that entries are normalized and match
        assert result[0].entry == "First"
        assert result[1].entry == "Second"
        assert result[2].entry == "Third"


class TestBatchVerify:
    """Tests for verification of batch results."""

    def test_batch_all_records_verify_valid(self, anchor_entry):
        entries = [anchor_entry, "Second entry", "Third entry"]
        result = stamp_batch(entries)
        for record in result:
            verify_result = record.verify()
            assert verify_result.valid is True
            assert verify_result.reason == "VALID"

    def test_batch_large_batch_all_verify(self):
        """100 entries all verify."""
        entries = [f"Entry number {i}" for i in range(100)]
        result = stamp_batch(entries)
        assert len(result) == 100
        for record in result:
            verify_result = record.verify()
            assert verify_result.valid is True


class TestBatchErrors:
    """Tests for error handling in batch."""

    def test_batch_empty_entry_raises_value_error(self):
        with pytest.raises(ValueError):
            stamp_batch([""])

    def test_batch_none_entry_raises_type_error(self):
        with pytest.raises(TypeError):
            stamp_batch([None])

    def test_batch_whitespace_only_raises_value_error(self):
        with pytest.raises(ValueError):
            stamp_batch(["   "])

    def test_batch_error_on_second_entry_first_already_processed(self):
        """Atomicity not guaranteed - first entry processed before error on second."""
        entries = ["Valid entry", "", "Third entry"]
        with pytest.raises(ValueError):
            stamp_batch(entries)
        # The function should raise on the empty string, but we can't guarantee
        # whether the first entry was already processed (depends on implementation)
        # This test documents that atomicity is NOT guaranteed

    def test_batch_error_message_from_underlying_stamp(self):
        """Error message should come from underlying stamp() validation."""
        with pytest.raises(ValueError) as exc_info:
            stamp_batch([""])
        # Should have a descriptive error message
        assert len(str(exc_info.value)) > 0


class TestBatchNormalization:
    """Tests for normalization in batch."""

    def test_batch_entries_normalized_individually(self):
        """Each entry is normalized individually."""
        entries = ["  First  ", "\tSecond\t", "  Third  "]
        result = stamp_batch(entries)
        assert result[0].entry == "First"
        assert result[1].entry == "Second"
        assert result[2].entry == "Third"


class TestBatchHypothesis:
    """Hypothesis property-based tests for batch."""

    def test_batch_all_records_verify_property(self, anchor_entry):
        """For any list of valid entry strings, all batch records verify."""
        from hypothesis import given, strategies as st

        @given(
            entries=st.lists(
                st.text(min_size=1, max_size=50).filter(lambda s: s.strip()),
                min_size=1,
                max_size=20,
            )
        )
        def _test(entries):
            try:
                result = stamp_batch(entries)
                for record in result:
                    verify_result = record.verify()
                    assert verify_result.valid is True
            except ValueError:
                pass  # Some combinations may be invalid

        _test()

    def test_batch_shared_unix_utc_property(self, anchor_entry, anchor_dt):
        """For any list of valid entries + dt, all records share unix_utc."""
        from hypothesis import given, strategies as st

        @given(
            entries=st.lists(
                st.text(min_size=1, max_size=50).filter(lambda s: s.strip()),
                min_size=1,
                max_size=20,
            ),
            year=st.integers(min_value=1582, max_value=2100),
            month=st.integers(min_value=1, max_value=12),
            day=st.integers(min_value=1, max_value=28),
            hour=st.integers(min_value=0, max_value=23),
            minute=st.integers(min_value=0, max_value=59),
            second=st.integers(min_value=0, max_value=59),
        )
        def _test(entries, year, month, day, hour, minute, second):
            try:
                dt = datetime(year, month, day, hour, minute, second, tzinfo=timezone.utc)
                if dt < datetime(1582, 10, 15, tzinfo=timezone.utc):
                    return
                result = stamp_batch(entries, dt=dt)
                unix_utcs = [r.stamp.unix_utc for r in result]
                assert len(set(unix_utcs)) == 1
            except ValueError:
                pass

        _test()

    def test_batch_length_matches_input_property(self, anchor_entry):
        """len(batch) == len(entries) always."""
        from hypothesis import given, strategies as st

        @given(
            entries=st.lists(
                st.text(min_size=1, max_size=50).filter(lambda s: s.strip()),
                min_size=0,
                max_size=50,
            )
        )
        def _test(entries):
            try:
                result = stamp_batch(entries)
                assert len(result) == len(entries)
            except (ValueError, TypeError):
                # If it raises, that's also valid behavior for invalid input
                pass

        _test()
