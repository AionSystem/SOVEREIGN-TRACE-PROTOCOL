"""
test_stamp_error_handling.py
Input validation — exact error types and message content.
"""
import pytest
from datetime import datetime, timezone
from hypothesis import given, settings
from hypothesis import strategies as st

from sovereign_trace_stamp import stamp


class TestErrorHandling:
    """Standard tests for input validation and error handling."""

    def test_empty_string_raises_value_error(self):
        """Empty string should raise ValueError."""
        with pytest.raises(ValueError):
            stamp("")

    def test_whitespace_only_space_raises_value_error(self):
        """Whitespace-only string (space) should raise ValueError."""
        with pytest.raises(ValueError):
            stamp(" ")

    def test_whitespace_only_tab_raises_value_error(self):
        """Whitespace-only string (tab) should raise ValueError."""
        with pytest.raises(ValueError):
            stamp("\t")

    def test_whitespace_only_newline_raises_value_error(self):
        """Whitespace-only string (newline) should raise ValueError."""
        with pytest.raises(ValueError):
            stamp("\n")

    def test_whitespace_only_mixed_raises_value_error(self):
        """Whitespace-only string (mixed) should raise ValueError."""
        with pytest.raises(ValueError):
            stamp("  \t\n  ")

    def test_whitespace_only_unicode_raises_value_error(self):
        """Whitespace-only string (Unicode U+00A0) should raise ValueError."""
        with pytest.raises(ValueError):
            stamp("\u00a0")

    def test_none_entry_raises_type_error(self):
        """None entry should raise TypeError."""
        with pytest.raises(TypeError):
            stamp(None)

    def test_int_entry_raises_type_error(self):
        """Integer entry should raise TypeError."""
        with pytest.raises(TypeError):
            stamp(123)

    def test_float_entry_raises_type_error(self):
        """Float entry should raise TypeError."""
        with pytest.raises(TypeError):
            stamp(12.34)

    def test_list_entry_raises_type_error(self):
        """List entry should raise TypeError."""
        with pytest.raises(TypeError):
            stamp(["entry"])

    def test_dict_entry_raises_type_error(self):
        """Dict entry should raise TypeError."""
        with pytest.raises(TypeError):
            stamp({"entry": "value"})

    def test_bytes_entry_raises_type_error(self):
        """Bytes entry should raise TypeError."""
        with pytest.raises(TypeError):
            stamp(b"entry")

    def test_bool_entry_raises_type_error(self):
        """Boolean entry should raise TypeError."""
        with pytest.raises(TypeError):
            stamp(True)

    def test_type_error_message_names_actual_type(self):
        """TypeError message should name the actual type."""
        with pytest.raises(TypeError) as exc_info:
            stamp(123)
        assert "int" in str(exc_info.value).lower() or "type" in str(exc_info.value).lower()

    def test_value_error_empty_has_descriptive_message(self):
        """ValueError for empty string should have descriptive message."""
        with pytest.raises(ValueError) as exc_info:
            stamp("")
        assert len(str(exc_info.value)) > 0

    def test_naive_dt_raises_value_error(self):
        """Naive datetime should raise ValueError."""
        naive_dt = datetime(2026, 3, 3, 15, 0, 0)
        with pytest.raises(ValueError):
            stamp("test", naive_dt)

    def test_naive_dt_message_mentions_timezone_aware(self):
        """ValueError for naive dt should mention timezone-aware."""
        naive_dt = datetime(2026, 3, 3, 15, 0, 0)
        with pytest.raises(ValueError) as exc_info:
            stamp("test", naive_dt)
        assert "timezone" in str(exc_info.value).lower() or "aware" in str(exc_info.value).lower()

    def test_pre_reform_oct_14_1582_raises_value_error(self):
        """October 14, 1582 should raise ValueError."""
        pre_reform = datetime(1582, 10, 14, tzinfo=timezone.utc)
        with pytest.raises(ValueError):
            stamp("test", pre_reform)

    def test_pre_reform_jan_1_1582_raises_value_error(self):
        """January 1, 1582 should raise ValueError."""
        pre_reform = datetime(1582, 1, 1, tzinfo=timezone.utc)
        with pytest.raises(ValueError):
            stamp("test", pre_reform)

    def test_pre_reform_1582_message_mentions_reform_date(self):
        """ValueError for pre-reform date should mention reform date."""
        pre_reform = datetime(1582, 1, 1, tzinfo=timezone.utc)
        with pytest.raises(ValueError) as exc_info:
            stamp("test", pre_reform)
        assert "1582" in str(exc_info.value) or "reform" in str(exc_info.value).lower()

    def test_year_1581_raises_value_error(self):
        """Year 1581 should raise ValueError."""
        ancient = datetime(1581, 6, 15, tzinfo=timezone.utc)
        with pytest.raises(ValueError):
            stamp("test", ancient)

    def test_year_4001_raises_value_error(self):
        """Year 4001 should raise ValueError."""
        future = datetime(4001, 1, 1, tzinfo=timezone.utc)
        with pytest.raises(ValueError):
            stamp("test", future)

    def test_year_range_error_message_names_bounds(self):
        """ValueError for year out of range should mention bounds."""
        future = datetime(4001, 1, 1, tzinfo=timezone.utc)
        with pytest.raises(ValueError) as exc_info:
            stamp("test", future)
        # Message should indicate valid range
        msg = str(exc_info.value)
        assert "1582" in msg or "4000" in msg or "range" in msg.lower() or "valid" in msg.lower()


class TestErrorHandlingHypothesis:
    """Hypothesis property-based tests for error handling."""

    @settings(max_examples=50, deadline=None)
    @given(st.none() | st.booleans() | st.integers() | st.floats() | st.lists(st.text()) | st.dictionaries(st.text(), st.text()) | st.binary())
    def test_non_string_entry_always_raises_type_error(self, non_string):
        """For any non-str Python object, TypeError is raised."""
        with pytest.raises(TypeError):
            stamp(non_string)

    @settings(max_examples=50, deadline=None)
    @given(
        st.builds(
            lambda s: s,
            st.text(alphabet=" \t\n\r\u00a0\u2002\u2003\u200b").filter(lambda s: len(s) > 0 and s.strip() == "")
        )
    )
    def test_whitespace_only_always_raises(self, whitespace_string):
        """For any string composed only of unicode whitespace chars, ValueError is raised."""
        with pytest.raises(ValueError):
            stamp(whitespace_string)

    @settings(max_examples=50, deadline=None)
    @given(year=st.integers(min_value=1, max_value=1581))
    def test_year_below_1582_always_raises(self, year):
        """For year in [1, 1581], ValueError is always raised."""
        try:
            dt = datetime(year, 6, 15, tzinfo=timezone.utc)
            with pytest.raises(ValueError):
                stamp("test", dt)
        except ValueError:
            # datetime constructor may raise for invalid years
            pass

    @settings(max_examples=50, deadline=None)
    @given(year=st.integers(min_value=4001, max_value=9999))
    def test_year_above_4000_always_raises(self, year):
        """For year in [4001, 9999], ValueError is always raised."""
        try:
            dt = datetime(year, 1, 1, tzinfo=timezone.utc)
            with pytest.raises(ValueError):
                stamp("test", dt)
        except ValueError:
            # datetime constructor may raise for invalid years
            pass
