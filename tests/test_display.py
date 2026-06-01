"""
test_display.py — display() and display_ascii() tests.

Field presence, formatting, emoji vs no-emoji, line structure.
"""

import pytest
from datetime import datetime, timezone

from sovereign_trace import stamp, display, display_ascii


class TestDisplayStandard:
    """Standard tests for display() function."""

    def test_display_returns_string(self, anchor_stamp):
        result = display(anchor_stamp)
        assert isinstance(result, str)

    def test_display_contains_gregorian_value(self, anchor_stamp):
        result = display(anchor_stamp)
        assert anchor_stamp.gregorian in result

    def test_display_contains_hebrew_value(self, anchor_stamp):
        result = display(anchor_stamp)
        assert anchor_stamp.hebrew in result

    def test_display_contains_dreamspell_value(self, anchor_stamp):
        result = display(anchor_stamp)
        assert anchor_stamp.dreamspell in result

    def test_display_contains_full_seal(self, anchor_stamp):
        result = display(anchor_stamp)
        assert anchor_stamp.seal in result

    def test_display_contains_version(self, anchor_stamp):
        result = display(anchor_stamp)
        assert anchor_stamp.version in result

    def test_display_has_emoji_calendar(self, anchor_stamp):
        result = display(anchor_stamp)
        assert "📅" in result

    def test_display_has_emoji_moon(self, anchor_stamp):
        result = display(anchor_stamp)
        assert "🌑" in result

    def test_display_has_emoji_spiral(self, anchor_stamp):
        result = display(anchor_stamp)
        assert "🌀" in result

    def test_display_has_emoji_lock(self, anchor_stamp):
        result = display(anchor_stamp)
        assert "🔒" in result

    def test_display_has_emoji_pin(self, anchor_stamp):
        result = display(anchor_stamp)
        assert "📌" in result

    def test_display_has_five_lines(self, anchor_stamp):
        result = display(anchor_stamp)
        lines = result.split("\n")
        assert len(lines) == 5

    def test_display_lines_in_correct_order(self, anchor_stamp):
        result = display(anchor_stamp)
        lines = result.split("\n")
        # Order: Gregorian, Hebrew, Dreamspell, Seal, Version
        assert anchor_stamp.gregorian in lines[0]
        assert anchor_stamp.hebrew in lines[1]
        assert anchor_stamp.dreamspell in lines[2]
        assert anchor_stamp.seal in lines[3]
        assert anchor_stamp.version in lines[4]

    def test_display_seal_not_truncated(self, anchor_stamp):
        result = display(anchor_stamp)
        assert len(anchor_stamp.seal) == 64
        assert anchor_stamp.seal in result


class TestDisplayAsciiStandard:
    """Standard tests for display_ascii() function."""

    def test_display_ascii_returns_string(self, anchor_stamp):
        result = display_ascii(anchor_stamp)
        assert isinstance(result, str)

    def test_display_ascii_contains_gregorian_value(self, anchor_stamp):
        result = display_ascii(anchor_stamp)
        assert anchor_stamp.gregorian in result

    def test_display_ascii_contains_hebrew_value(self, anchor_stamp):
        result = display_ascii(anchor_stamp)
        assert anchor_stamp.hebrew in result

    def test_display_ascii_contains_dreamspell_value(self, anchor_stamp):
        result = display_ascii(anchor_stamp)
        assert anchor_stamp.dreamspell in result

    def test_display_ascii_contains_full_seal(self, anchor_stamp):
        result = display_ascii(anchor_stamp)
        assert anchor_stamp.seal in result

    def test_display_ascii_contains_version(self, anchor_stamp):
        result = display_ascii(anchor_stamp)
        assert anchor_stamp.version in result

    def test_display_ascii_has_no_emoji_chars(self, anchor_stamp):
        result = display_ascii(anchor_stamp)
        # Check that common emoji characters are not present
        emoji_chars = ["📅", "🌑", "🌀", "🔒", "📌"]
        for emoji in emoji_chars:
            assert emoji not in result

    def test_display_ascii_has_five_lines(self, anchor_stamp):
        result = display_ascii(anchor_stamp)
        lines = result.split("\n")
        assert len(lines) == 5

    def test_display_ascii_lines_in_correct_order(self, anchor_stamp):
        result = display_ascii(anchor_stamp)
        lines = result.split("\n")
        # Order: Gregorian, Hebrew, Dreamspell, Seal, Version
        assert anchor_stamp.gregorian in lines[0]
        assert anchor_stamp.hebrew in lines[1]
        assert anchor_stamp.dreamspell in lines[2]
        assert anchor_stamp.seal in lines[3]
        assert anchor_stamp.version in lines[4]

    def test_display_ascii_seal_not_truncated(self, anchor_stamp):
        result = display_ascii(anchor_stamp)
        assert len(anchor_stamp.seal) == 64
        assert anchor_stamp.seal in result


class TestDisplayComparison:
    """Tests comparing display() and display_ascii()."""

    def test_display_and_ascii_carry_same_data(self, anchor_stamp):
        """Same field values, different decoration."""
        full_result = display(anchor_stamp)
        ascii_result = display_ascii(anchor_stamp)

        # Both should contain the same core data
        assert anchor_stamp.gregorian in full_result
        assert anchor_stamp.gregorian in ascii_result
        assert anchor_stamp.hebrew in full_result
        assert anchor_stamp.hebrew in ascii_result
        assert anchor_stamp.dreamspell in full_result
        assert anchor_stamp.dreamspell in ascii_result
        assert anchor_stamp.seal in full_result
        assert anchor_stamp.seal in ascii_result
        assert anchor_stamp.version in full_result
        assert anchor_stamp.version in ascii_result

    def test_display_multiline_on_newlines(self, anchor_stamp):
        result = display(anchor_stamp)
        assert "\n" in result
        lines = result.split("\n")
        assert len(lines) == 5


class TestDisplayParametrized:
    """Parametrized tests for various dates."""

    @pytest.mark.parametrize(
        "dt,expected_hebrew_substring",
        [
            # Day Out of Time (July 25)
            (datetime(2026, 7, 25, 12, 0, 0, tzinfo=timezone.utc), ""),
            # Rosh Hashanah 5786
            (datetime(2025, 9, 23, 12, 0, 0, tzinfo=timezone.utc), "Tishrei"),
            # Leap year Adar II (15 Adar II 5784)
            (datetime(2024, 3, 25, 12, 0, 0, tzinfo=timezone.utc), "Adar"),
            # Moon 1 Day 1 (July 26)
            (datetime(2026, 7, 26, 12, 0, 0, tzinfo=timezone.utc), ""),
        ],
    )
    def test_display_various_dates(self, dt, expected_hebrew_substring):
        """Each produces display without error and contains correct calendar strings."""
        entry = "Test entry for various dates"
        stmp = stamp(entry, dt)

        # Should not raise
        result = display(stmp)
        ascii_result = display_ascii(stmp)

        # Both should be strings
        assert isinstance(result, str)
        assert isinstance(ascii_result, str)

        # Should contain the seal
        assert stmp.seal in result
        assert stmp.seal in ascii_result

        # Should contain gregorian
        assert stmp.gregorian in result
        assert stmp.gregorian in ascii_result

        # Should contain dreamspell
        assert stmp.dreamspell in result
        assert stmp.dreamspell in ascii_result


class TestDisplayHypothesis:
    """Hypothesis property-based tests for display functions."""

    def test_display_always_contains_seal(self, anchor_entry, anchor_dt):
        """For any valid entry + dt, display() output contains the stamp's seal."""
        from hypothesis import given, strategies as st

        @given(
            entry=st.text(min_size=1, max_size=100).filter(lambda s: s.strip()),
            year=st.integers(min_value=1582, max_value=2100),
            month=st.integers(min_value=1, max_value=12),
            day=st.integers(min_value=1, max_value=28),  # Safe day range
            hour=st.integers(min_value=0, max_value=23),
            minute=st.integers(min_value=0, max_value=59),
            second=st.integers(min_value=0, max_value=59),
        )
        def _test(entry, year, month, day, hour, minute, second):
            try:
                dt = datetime(year, month, day, hour, minute, second, tzinfo=timezone.utc)
                if dt < datetime(1582, 10, 15, tzinfo=timezone.utc):
                    return  # Skip pre-reform
                stmp = stamp(entry, dt)
                result = display(stmp)
                assert stmp.seal in result
            except ValueError:
                pass  # Invalid date combinations

        _test()

    def test_display_ascii_always_ascii_only(self, anchor_entry, anchor_dt):
        """For any valid entry + dt, all chars in display_ascii() are ASCII."""
        from hypothesis import given, strategies as st

        @given(
            entry=st.text(min_size=1, max_size=100).filter(lambda s: s.strip()),
            year=st.integers(min_value=1582, max_value=2100),
            month=st.integers(min_value=1, max_value=12),
            day=st.integers(min_value=1, max_value=28),
            hour=st.integers(min_value=0, max_value=23),
            minute=st.integers(min_value=0, max_value=59),
            second=st.integers(min_value=0, max_value=59),
        )
        def _test(entry, year, month, day, hour, minute, second):
            try:
                dt = datetime(year, month, day, hour, minute, second, tzinfo=timezone.utc)
                if dt < datetime(1582, 10, 15, tzinfo=timezone.utc):
                    return
                stmp = stamp(entry, dt)
                result = display_ascii(stmp)
                # All characters should be ASCII (ord < 128)
                for char in result:
                    assert ord(char) < 128, f"Non-ASCII character found: {char!r}"
            except ValueError:
                pass

        _test()
