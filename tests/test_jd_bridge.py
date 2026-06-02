"""Julian Day Number internal bridge — `_jd_from_gregorian()`."""
import pytest
from datetime import date, timedelta
from hypothesis import given, settings
from hypothesis.strategies import dates

from sovereign_trace.sovereign_trace_stamp import _jd_from_gregorian


# =============================================================================
# Standard tests
# =============================================================================

def test_jd_sep_23_2025_equals_2460942():
    """Sep 23, 2025 → JD 2460942."""
    jd = _jd_from_gregorian(2025, 9, 23)
    assert jd == 2460942


def test_jd_mar_3_2026_equals_2461103():
    """Mar 3, 2026 → JD 2461103."""
    jd = _jd_from_gregorian(2026, 3, 3)
    assert jd == 2461103


def test_jd_oct_15_1582_accepted():
    """Oct 15, 1582 (first Gregorian date) is accepted."""
    jd = _jd_from_gregorian(1582, 10, 15)
    assert isinstance(jd, int)
    assert jd > 0


def test_jd_oct_14_1582_raises():
    """Oct 14, 1582 (last pre-reform date) raises ValueError."""
    with pytest.raises(ValueError):
        _jd_from_gregorian(1582, 10, 14)


def test_jd_oct_15_1582_exact_value():
    """Oct 15, 1582 exact JD value: 2299161."""
    jd = _jd_from_gregorian(1582, 10, 15)
    assert jd == 2299161


def test_jd_year_1581_raises():
    """Year 1581 (pre-reform) raises ValueError."""
    with pytest.raises(ValueError):
        _jd_from_gregorian(1581, 6, 15)


def test_jd_year_1582_jan_1_raises():
    """Jan 1, 1582 (full year pre-reform) raises ValueError."""
    with pytest.raises(ValueError):
        _jd_from_gregorian(1582, 1, 1)


def test_jd_year_4000_dec_31_accepted():
    """Dec 31, 4000 is accepted."""
    jd = _jd_from_gregorian(4000, 12, 31)
    assert isinstance(jd, int)
    assert jd > 0


def test_jd_year_4001_raises():
    """Year 4001 raises ValueError."""
    with pytest.raises(ValueError):
        _jd_from_gregorian(4001, 1, 1)


def test_jd_jan_1_2000():
    """Jan 1, 2000 → JD 2451545 (known value)."""
    jd = _jd_from_gregorian(2000, 1, 1)
    assert jd == 2451545


def test_jd_dec_31_any_year():
    """Dec 31 of any valid year produces no exception."""
    for year in [1600, 1700, 1800, 1900, 2000, 2100, 3000, 3999]:
        jd = _jd_from_gregorian(year, 12, 31)
        assert isinstance(jd, int)


def test_jd_leap_day_feb_29_2024():
    """Feb 29, 2024 (leap day) produces valid JD."""
    jd = _jd_from_gregorian(2024, 2, 29)
    assert isinstance(jd, int)
    # Should be one day after Feb 28, 2024
    jd_feb_28 = _jd_from_gregorian(2024, 2, 28)
    assert jd == jd_feb_28 + 1


def test_jd_sequential_days_differ_by_one():
    """JD(d+1) == JD(d) + 1."""
    base_date = date(2026, 3, 3)
    jd_base = _jd_from_gregorian(base_date.year, base_date.month, base_date.day)
    next_date = base_date + timedelta(days=1)
    jd_next = _jd_from_gregorian(next_date.year, next_date.month, next_date.day)
    assert jd_next == jd_base + 1


def test_jd_sequential_months_correct():
    """JD difference between months is approximately correct."""
    jd_mar_1 = _jd_from_gregorian(2026, 3, 1)
    jd_apr_1 = _jd_from_gregorian(2026, 4, 1)
    # March has 31 days
    assert jd_apr_1 == jd_mar_1 + 31


def test_jd_year_boundary_dec_31_to_jan_1():
    """JD handles year boundary correctly (Dec 31 to Jan 1)."""
    jd_dec_31 = _jd_from_gregorian(2025, 12, 31)
    jd_jan_1 = _jd_from_gregorian(2026, 1, 1)
    assert jd_jan_1 == jd_dec_31 + 1


def test_jd_always_positive_in_valid_range():
    """JD is always positive for valid dates."""
    for year in [1600, 1700, 1800, 1900, 2000, 2100, 3000, 3999]:
        jd = _jd_from_gregorian(year, 6, 15)
        assert jd > 0


# =============================================================================
# Hypothesis tests
# =============================================================================

@given(dates(min_value=date(1582, 10, 15), max_value=date(3999, 12, 30)))
@settings(max_examples=50)
def test_jd_sequential_difference_always_1_property(test_date):
    """For any valid date d, JD(d+1day) == JD(d) + 1."""
    jd_current = _jd_from_gregorian(test_date.year, test_date.month, test_date.day)
    jd_next = _jd_from_gregorian((test_date + timedelta(days=1)).year, (test_date + timedelta(days=1)).month, (test_date + timedelta(days=1)).day)
    assert jd_next == jd_current + 1


@given(dates(min_value=date(1582, 10, 15), max_value=date(3999, 12, 31)))
@settings(max_examples=50)
def test_jd_monotone_in_valid_range_property(test_date):
    """JD is monotonically increasing."""
    if test_date < date(3999, 12, 31):
        jd_current = _jd_from_gregorian(test_date.year, test_date.month, test_date.day)
        jd_next = _jd_from_gregorian((test_date + timedelta(days=1)).year, (test_date + timedelta(days=1)).month, (test_date + timedelta(days=1)).day)
        assert jd_next > jd_current


@given(dates(min_value=date(1, 1, 1), max_value=date(1582, 10, 14)))
@settings(max_examples=20)
def test_jd_raises_outside_valid_range_property_pre_reform(test_date):
    """Year < 1582 or before Oct 15, 1582 always raises ValueError."""
    with pytest.raises(ValueError):
        _jd_from_gregorian(test_date.year, test_date.month, test_date.day)


@given(dates(min_value=date(4001, 1, 1), max_value=date(9999, 12, 31)))
@settings(max_examples=20)
def test_jd_raises_outside_valid_range_property_post_4000(test_date):
    """Year > 4000 always raises ValueError."""
    with pytest.raises(ValueError):
        _jd_from_gregorian(test_date.year, test_date.month, test_date.day)
