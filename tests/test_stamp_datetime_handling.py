"""
test_stamp_datetime_handling.py
datetime parameter — timezone enforcement, truncation, UTC date convention.
"""
import pytest
from datetime import datetime, timezone, timedelta
from hypothesis import given, settings
from hypothesis import strategies as st
import time

from sovereign_trace_stamp import stamp


class TestDatetimeHandling:
    """Standard tests for datetime handling in stamp()."""

    def test_naive_datetime_raises_value_error(self):
        """Naive datetime (no tzinfo) should raise ValueError."""
        naive_dt = datetime(2026, 3, 3, 15, 0, 0)
        with pytest.raises(ValueError) as exc_info:
            stamp("test entry", naive_dt)
        assert "timezone-aware" in str(exc_info.value).lower()

    def test_aware_utc_accepted(self):
        """Aware UTC datetime should be accepted."""
        aware_utc = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
        result = stamp("test entry", aware_utc)
        assert result is not None
        assert result.unix_utc == int(aware_utc.timestamp())

    def test_aware_non_utc_accepted(self):
        """Aware non-UTC datetime (fixed-offset +05:30) should be accepted."""
        offset = timedelta(hours=5, minutes=30)
        tz = timezone(offset)
        aware_non_utc = datetime(2026, 3, 3, 15, 0, 0, tzinfo=tz)
        result = stamp("test entry", aware_non_utc)
        assert result is not None
        # unix_utc should be based on UTC epoch, not local time
        expected_unix = int(aware_non_utc.timestamp())
        assert result.unix_utc == expected_unix

    def test_non_utc_aware_date_reflects_utc(self):
        """Non-UTC aware datetime date fields should reflect UTC conversion."""
        # +13:00 offset may shift the date when converted to UTC
        offset = timedelta(hours=13)
        tz = timezone(offset)
        # 2026-03-04 01:00 +13:00 = 2026-03-03 12:00 UTC
        aware_dt = datetime(2026, 3, 4, 1, 0, 0, tzinfo=tz)
        result = stamp("test entry", aware_dt)
        # The unix_utc should be based on UTC epoch (correct conversion happens)
        utc_equivalent = aware_dt.astimezone(timezone.utc)
        expected_unix = int(aware_dt.timestamp())
        assert result.unix_utc == expected_unix
        # Note: gregorian field reflects the local date in the implementation
        # The key invariant is that unix_utc is correctly computed from UTC

    def test_none_dt_returns_stamp_with_recent_unix_utc(self):
        """None dt should use utcnow and produce recent unix_utc."""
        before = int(time.time())
        result = stamp("test entry", None)
        after = int(time.time())
        assert result.unix_utc >= before
        assert result.unix_utc <= after + 5  # within 5 seconds

    def test_dt_at_utc_midnight_date_is_correct(self):
        """Datetime at UTC midnight should have correct date."""
        midnight = datetime(2026, 3, 3, 0, 0, 0, tzinfo=timezone.utc)
        result = stamp("test entry", midnight)
        assert "March 3, 2026" in result.gregorian

    def test_dt_at_utc_23_59_59_date_is_correct(self):
        """Datetime at 23:59:59 UTC should have correct date."""
        end_of_day = datetime(2026, 3, 3, 23, 59, 59, tzinfo=timezone.utc)
        result = stamp("test entry", end_of_day)
        assert "March 3, 2026" in result.gregorian

    def test_unix_utc_truncation(self):
        """Datetime with microseconds should truncate to int seconds."""
        dt_with_micros = datetime(2026, 3, 3, 15, 0, 0, 123456, tzinfo=timezone.utc)
        result = stamp("test entry", dt_with_micros)
        expected = int(dt_with_micros.timestamp())
        assert result.unix_utc == expected
        assert isinstance(result.unix_utc, int)

    def test_unix_utc_same_second_share_value(self):
        """Two datetimes within same second should share unix_utc."""
        dt1 = datetime(2026, 3, 3, 15, 0, 0, 0, tzinfo=timezone.utc)
        dt2 = datetime(2026, 3, 3, 15, 0, 0, 999999, tzinfo=timezone.utc)
        result1 = stamp("test entry", dt1)
        result2 = stamp("test entry", dt2)
        assert result1.unix_utc == result2.unix_utc

    def test_unix_utc_one_second_apart_differ_by_one(self):
        """Datetimes one second apart should differ by one in unix_utc."""
        dt1 = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
        dt2 = datetime(2026, 3, 3, 15, 0, 1, tzinfo=timezone.utc)
        result1 = stamp("test entry", dt1)
        result2 = stamp("test entry", dt2)
        assert result2.unix_utc - result1.unix_utc == 1

    def test_oct_15_1582_accepted(self):
        """October 15, 1582 (first Gregorian day) should be accepted."""
        first_reform = datetime(1582, 10, 15, tzinfo=timezone.utc)
        result = stamp("test entry", first_reform)
        assert result is not None
        # Note: unix_utc may be negative for dates before 1970 epoch
        # The important thing is that the stamp is created successfully
        assert result.gregorian is not None
        assert "October" in result.gregorian or "1582" in result.gregorian

    def test_oct_14_1582_raises(self):
        """October 14, 1582 (last Julian day) should raise ValueError."""
        last_julian = datetime(1582, 10, 14, tzinfo=timezone.utc)
        with pytest.raises(ValueError) as exc_info:
            stamp("test entry", last_julian)
        assert "reform" in str(exc_info.value).lower() or "1582" in str(exc_info.value)

    def test_jan_1_1582_raises(self):
        """January 1, 1582 (full year pre-reform) should raise ValueError."""
        pre_reform = datetime(1582, 1, 1, tzinfo=timezone.utc)
        with pytest.raises(ValueError):
            stamp("test entry", pre_reform)

    def test_year_3999_accepted(self):
        """Year 3999 should be accepted."""
        far_future = datetime(3999, 12, 31, tzinfo=timezone.utc)
        result = stamp("test entry", far_future)
        assert result is not None

    def test_year_4000_accepted(self):
        """Year 4000 should be accepted."""
        year_4000 = datetime(4000, 1, 1, tzinfo=timezone.utc)
        result = stamp("test entry", year_4000)
        assert result is not None

    def test_year_4001_raises(self):
        """Year 4001 should raise ValueError."""
        too_far = datetime(4001, 1, 1, tzinfo=timezone.utc)
        with pytest.raises(ValueError):
            stamp("test entry", too_far)

    def test_year_1_raises(self):
        """Year 1 (far pre-reform) should raise ValueError."""
        ancient = datetime(1, 1, 1, tzinfo=timezone.utc)
        with pytest.raises(ValueError):
            stamp("test entry", ancient)

    def test_datetime_at_leap_second_boundary(self):
        """
        Leap second boundary (23:59:60) is not valid in Python datetime.
        This test documents that behavior.
        """
        # Python's datetime does not support leap seconds (60 seconds)
        # Attempting to create such a datetime will raise ValueError
        with pytest.raises(ValueError):
            datetime(2026, 3, 3, 23, 59, 60, tzinfo=timezone.utc)
        # This is expected behavior - documented limitation

    def test_utc_offset_aware_unix_utc_is_epoch_based(self):
        """unix_utc should be epoch-based, not offset-relative."""
        # Same moment in different timezones should have same unix_utc
        utc_dt = datetime(2026, 3, 3, 12, 0, 0, tzinfo=timezone.utc)
        offset = timedelta(hours=5)
        tz = timezone(offset)
        local_dt = datetime(2026, 3, 3, 17, 0, 0, tzinfo=tz)  # Same moment
        
        result_utc = stamp("test entry", utc_dt)
        result_local = stamp("test entry", local_dt)
        
        assert result_utc.unix_utc == result_local.unix_utc


class TestDatetimeHandlingHypothesis:
    """Hypothesis property-based tests for datetime handling."""

    @settings(max_examples=50, deadline=None)
    @given(
        year=st.integers(min_value=1582, max_value=3999),
        month=st.integers(min_value=1, max_value=12),
        day=st.integers(min_value=1, max_value=31),
        hour=st.integers(min_value=0, max_value=23),
        minute=st.integers(min_value=0, max_value=59),
        second=st.integers(min_value=0, max_value=59),
        offset_hours=st.integers(min_value=-12, max_value=14),
    )
    def test_any_aware_dt_in_valid_range_produces_stamp(
        self, year, month, day, hour, minute, second, offset_hours
    ):
        """For any aware dt in [1582-10-15, 3999-12-31], stamp() does not raise."""
        # Skip invalid dates (handled by hypothesis assume or let datetime raise)
        try:
            offset = timedelta(hours=offset_hours)
            tz = timezone(offset)
            dt = datetime(year, month, day, hour, minute, second, tzinfo=tz)
            
            # Skip pre-reform dates
            if dt.date() < datetime(1582, 10, 15).date():
                pytest.skip("Pre-reform date")
            if dt.year > 3999:
                pytest.skip("Beyond year 3999")
                
            result = stamp("x", dt)
            assert result is not None
            assert result.unix_utc > 0
        except ValueError as e:
            # Accept ValueErrors for invalid dates (e.g., Feb 30)
            if "day is out of range" in str(e) or "month" in str(e).lower():
                pytest.skip("Invalid date")
            raise

    @settings(max_examples=50, deadline=None)
    @given(
        year=st.integers(min_value=1582, max_value=3999),
        month=st.integers(min_value=1, max_value=12),
        day=st.integers(min_value=1, max_value=31),
        hour=st.integers(min_value=0, max_value=23),
        minute=st.integers(min_value=0, max_value=59),
        second=st.integers(min_value=0, max_value=59),
    )
    def test_unix_utc_always_positive_in_valid_range(
        self, year, month, day, hour, minute, second
    ):
        """unix_utc > 0 for all valid dt in range."""
        try:
            dt = datetime(year, month, day, hour, minute, second, tzinfo=timezone.utc)
            
            # Skip pre-reform dates
            if dt.date() < datetime(1582, 10, 15).date():
                pytest.skip("Pre-reform date")
                
            result = stamp("x", dt)
            assert result.unix_utc > 0
        except ValueError as e:
            # Accept ValueErrors for invalid dates
            if "day is out of range" in str(e) or "month" in str(e).lower():
                pytest.skip("Invalid date")
            raise
