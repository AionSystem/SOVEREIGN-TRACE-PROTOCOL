"""13 Moon Dreamspell (Argüelles system)."""
import pytest
from datetime import date, timedelta
from hypothesis import given, settings
from hypothesis.strategies import dates, integers

from sovereign_trace import stamp
from sovereign_trace.sovereign_trace_stamp import _dreamspell


# =============================================================================
# Standard tests
# =============================================================================

def test_anchor_mar_3_2026():
    """Mar 3, 2026 → "Day 25, Galactic Moon 8/13"."""
    result = _dreamspell(date(2026, 3, 3))
    assert result == "Day 25, Galactic Moon 8/13"


def test_day_out_of_time_jul_25_2026():
    """Jul 25, 2026 → "Day Out of Time"."""
    result = _dreamspell(date(2026, 7, 25))
    assert result == "Day Out of Time"


def test_day_out_of_time_jul_25_2025():
    """Jul 25, 2025 → "Day Out of Time"."""
    result = _dreamspell(date(2025, 7, 25))
    assert result == "Day Out of Time"


@pytest.mark.parametrize("year", [2024, 2025, 2026, 2027, 2028, 2029, 2030])
def test_day_out_of_time_jul_25_any_year(year):
    """Jul 25 any year (2024–2030) → "Day Out of Time"."""
    result = _dreamspell(date(year, 7, 25))
    assert result == "Day Out of Time"


def test_new_year_jul_26_2026():
    """Jul 26, 2026 → "Day 1, Magnetic Moon 1/13"."""
    result = _dreamspell(date(2026, 7, 26))
    assert result == "Day 1, Magnetic Moon 1/13"


def test_last_day_moon_1():
    """Last day of Moon 1 → "Day 28, Magnetic Moon 1/13"."""
    # Moon 1 has 28 days, so day 28 is Jul 23 (since Jul 26 is day 1)
    result = _dreamspell(date(2026, 8, 22))
    assert result == "Day 28, Magnetic Moon 1/13"


def test_first_day_moon_2():
    """First day of Moon 2 → "Day 1, Lunar Moon 2/13"."""
    result = _dreamspell(date(2026, 8, 23))
    assert result == "Day 1, Lunar Moon 2/13"


def test_first_day_moon_13():
    """First day of Moon 13 → "Day 1, Cosmic Moon 13/13"."""
    # Moon 13 starts after 12 moons of 28 days = 336 days from Jul 26
    # Jul 26 + 336 days = Jun 27, 2027 (approximate, need to calculate)
    result = _dreamspell(date(2027, 6, 27))
    assert result == "Day 1, Cosmic Moon 13/13"


def test_last_day_moon_13():
    """Last day of Moon 13 → "Day 28, Cosmic Moon 13/13"."""
    result = _dreamspell(date(2027, 7, 24))
    assert result == "Day 28, Cosmic Moon 13/13"


def test_jul_24_is_day_28_cosmic():
    """Jul 24 is Day 28, Cosmic Moon 13/13 — last day before Day Out of Time."""
    result = _dreamspell(date(2026, 7, 24))
    assert result == "Day 28, Cosmic Moon 13/13"


def test_leap_year_feb_29_no_exception():
    """Leap year Feb 29 should not raise exception."""
    result = _dreamspell(date(2024, 2, 29))
    assert isinstance(result, str)
    assert len(result) > 0


def test_leap_year_cross_boundary():
    """Mar 1, 2028 → "Day 24, Galactic Moon 8/13"."""
    result = _dreamspell(date(2028, 3, 1))
    assert result == "Day 24, Galactic Moon 8/13"


def test_all_13_moon_names_appear():
    """Cycle through a full year, all 13 moon names seen."""
    moon_names = ["Magnetic", "Lunar", "Electric", "Self-Existing", "Overtone", 
                  "Rhythmic", "Resonant", "Galactic", "Solar", "Planetary", 
                  "Spectral", "Crystal", "Cosmic"]
    found_names = set()
    
    # Start from Jul 26, 2026 and go through 365 days
    start = date(2026, 7, 26)
    for i in range(365):
        current_date = start + timedelta(days=i)
        result = _dreamspell(current_date)
        if result != "Day Out of Time":
            for name in moon_names:
                if name in result:
                    found_names.add(name)
    
    assert found_names == set(moon_names), f"Missing moon names: {set(moon_names) - found_names}"


def test_moon_number_always_1_to_13():
    """No date in a full year produces moon > 13."""
    start = date(2026, 7, 26)
    for i in range(365):
        current_date = start + timedelta(days=i)
        result = _dreamspell(current_date)
        if result != "Day Out of Time":
            # Extract moon number from "Day N, Name Moon M/13"
            parts = result.split()
            moon_part = parts[-1]  # "M/13"
            moon_num = int(moon_part.split('/')[0])
            assert 1 <= moon_num <= 13, f"Moon number {moon_num} out of range for {current_date}"


def test_day_number_always_1_to_28():
    """Day number always 1 to 28."""
    start = date(2026, 7, 26)
    for i in range(365):
        current_date = start + timedelta(days=i)
        result = _dreamspell(current_date)
        if result != "Day Out of Time":
            # Extract day number from "Day N, Name Moon M/13"
            # Format is "Day 1, Magnetic Moon 1/13" so split by space and remove comma
            day_part = result.split()[1].rstrip(',')
            day_num = int(day_part)
            assert 1 <= day_num <= 28, f"Day number {day_num} out of range for {current_date}"


def test_output_format_standard():
    """Output format is "Day N, Name Moon M/13"."""
    result = _dreamspell(date(2026, 7, 26))
    assert result.startswith("Day ")
    assert ", " in result
    assert " Moon " in result
    assert "/13" in result


def test_output_format_day_out_of_time():
    """Day Out of Time exact string."""
    result = _dreamspell(date(2026, 7, 25))
    assert result == "Day Out of Time"


def test_pre_jul_26_uses_prior_year_as_start():
    """Dates before Jul 26 use prior year's Jul 26 as cycle start."""
    # Dec 31, 2025 should be in the cycle that started Jul 26, 2025
    result = _dreamspell(date(2025, 12, 31))
    assert isinstance(result, str)
    assert result != "Day Out of Time"


def test_post_jul_26_uses_current_year_as_start():
    """Dates after Jul 26 use current year's Jul 26 as cycle start."""
    # Aug 1, 2026 should be in the cycle that started Jul 26, 2026
    result = _dreamspell(date(2026, 8, 1))
    assert isinstance(result, str)
    assert result != "Day Out of Time"


@pytest.mark.parametrize("year", range(2000, 2051))
def test_year_start_jul_26_always_day_1(year):
    """Jul 26 of any year (2000–2050) is always Day 1, Magnetic Moon 1/13."""
    result = _dreamspell(date(year, 7, 26))
    assert result == "Day 1, Magnetic Moon 1/13"


def test_day_count_in_full_year_364():
    """Count non-DOT days in Jul 26–Jul 24 = 364."""
    start = date(2026, 7, 26)
    count = 0
    for i in range(365):
        current_date = start + timedelta(days=i)
        result = _dreamspell(current_date)
        if result != "Day Out of Time":
            count += 1
    assert count == 364


# =============================================================================
# Hypothesis tests
# =============================================================================

@given(dates(min_value=date(1582, 10, 15), max_value=date(3999, 12, 31)))
@settings(max_examples=50)
def test_any_non_dot_date_produces_standard_format(test_date):
    """For any date not Jul 25, output matches "Day N, Name Moon M/13"."""
    import re
    result = _dreamspell(test_date)
    if test_date.month == 7 and test_date.day == 25:
        assert result == "Day Out of Time"
    else:
        pattern = r"^Day \d+, [A-Za-z\-]+ Moon \d+/13$"
        assert re.match(pattern, result), f"Invalid format: {result}"


@given(integers(min_value=1582, max_value=3999))
@settings(max_examples=50)
def test_any_jul_25_is_day_out_of_time(year):
    """Any Jul 25 is Day Out of Time."""
    result = _dreamspell(date(year, 7, 25))
    assert result == "Day Out of Time"


@given(dates(min_value=date(1582, 10, 15), max_value=date(3999, 12, 31)))
@settings(max_examples=50)
def test_moon_always_valid_range(test_date):
    """Moon number always in 1-13 range."""
    result = _dreamspell(test_date)
    if result != "Day Out of Time":
        parts = result.split()
        moon_part = parts[-1]
        moon_num = int(moon_part.split('/')[0])
        assert 1 <= moon_num <= 13


@given(dates(min_value=date(1582, 10, 15), max_value=date(3999, 12, 31)))
@settings(max_examples=50)
def test_day_always_valid_range(test_date):
    """Day number always in 1-28 range."""
    result = _dreamspell(test_date)
    if result != "Day Out of Time":
        # Format is "Day N, Name Moon M/13" so split by space and remove comma
        day_part = result.split()[1].rstrip(',')
        day_num = int(day_part)
        assert 1 <= day_num <= 28
