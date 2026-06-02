"""Gregorian date string formatting."""
import pytest
from datetime import date
from hypothesis import given, settings
from hypothesis.strategies import dates

from sovereign_trace.sovereign_trace_stamp import _gregorian


# =============================================================================
# Standard tests
# =============================================================================

def test_march_3_2026():
    """March 3, 2026 → "March 3, 2026"."""
    result = _gregorian(date(2026, 3, 3))
    assert result == "March 3, 2026"


@pytest.mark.parametrize("month, expected_name", [
    (1, "January"),
    (2, "February"),
    (3, "March"),
    (4, "April"),
    (5, "May"),
    (6, "June"),
    (7, "July"),
    (8, "August"),
    (9, "September"),
    (10, "October"),
    (11, "November"),
    (12, "December"),
])
def test_all_12_month_names_parametrized(month, expected_name):
    """All 12 month names appear correctly (day 1 of each month)."""
    result = _gregorian(date(2026, month, 1))
    assert expected_name in result


def test_single_digit_day_no_zero_padding():
    """Single digit day has no zero padding: "March 3" not "March 03"."""
    result = _gregorian(date(2026, 3, 3))
    assert "March 3," in result
    assert "March 03," not in result


def test_double_digit_day():
    """Double digit day formatted correctly: "March 14"."""
    result = _gregorian(date(2026, 3, 14))
    assert "March 14," in result


def test_triple_digit_day_impossible():
    """Triple digit day is impossible (max is 31)."""
    # This is more of a documentation test - we can't have day > 31
    # Just verify that valid days work
    result = _gregorian(date(2026, 3, 31))
    assert "March 31," in result


def test_jan_1():
    """January 1 formatted correctly."""
    result = _gregorian(date(2026, 1, 1))
    assert result == "January 1, 2026"


def test_dec_31():
    """December 31 formatted correctly."""
    result = _gregorian(date(2026, 12, 31))
    assert result == "December 31, 2026"


def test_year_four_digits():
    """Year always has four digits, no leading zeros."""
    result = _gregorian(date(2026, 3, 3))
    assert ", 2026" in result
    # Check it's exactly 4 digits
    year_part = result.split(", ")[-1]
    assert len(year_part) == 4


def test_year_1582():
    """October 15, 1582 (first Gregorian date)."""
    result = _gregorian(date(1582, 10, 15))
    assert result == "October 15, 1582"


def test_year_3999():
    """December 31, 3999."""
    result = _gregorian(date(3999, 12, 31))
    assert result == "December 31, 3999"


def test_leap_day_feb_29():
    """February 29, 2024 (leap day)."""
    result = _gregorian(date(2024, 2, 29))
    assert result == "February 29, 2024"


# =============================================================================
# Hypothesis tests
# =============================================================================

@given(dates(min_value=date(1582, 10, 15), max_value=date(3999, 12, 31)))
@settings(max_examples=50)
def test_gregorian_output_always_contains_year(test_date):
    """Year always appears in output."""
    result = _gregorian(test_date)
    assert str(test_date.year) in result


@given(dates(min_value=date(1582, 10, 15), max_value=date(3999, 12, 31)))
@settings(max_examples=50)
def test_gregorian_output_always_contains_day_as_int(test_date):
    """Day numeral always in output."""
    result = _gregorian(test_date)
    day_str = str(test_date.day)
    assert day_str in result
