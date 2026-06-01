"""
Shared pytest fixtures for the entire Sovereign Trace test suite.

All calendar-verified values sourced from Hebcal.com, Chabad.org, and pyluach — tagged [D].
"""
import os
import sys
from datetime import datetime, timezone, date

# Add stamp directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'stamp'))

import pytest


# ═══════════════════════════════════════════════════════════════════
# HYPOTHESIS PROFILE FIXTURE (session-scoped)
# ═══════════════════════════════════════════════════════════════════

@pytest.fixture(scope="session", autouse=True)
def hypothesis_profile():
    """Configure Hypothesis profiles for CI vs full runs."""
    from hypothesis import settings, HealthCheck
    
    settings.register_profile(
        "ci", 
        max_examples=50, 
        suppress_health_check=[HealthCheck.too_slow]
    )
    settings.register_profile("full", max_examples=500)
    
    profile_name = os.getenv("HYPOTHESIS_PROFILE", "ci")
    settings.load_profile(profile_name)


# ═══════════════════════════════════════════════════════════════════
# ANCHOR FIXTURES — March 3, 2026 / 14 Adar 5786 [D]
# ═══════════════════════════════════════════════════════════════════

@pytest.fixture
def anchor_dt():
    """Primary anchor datetime: March 3, 2026 at 15:00 UTC [D]."""
    return datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)


@pytest.fixture
def anchor_date():
    """Primary anchor date: March 3, 2026."""
    return date(2026, 3, 3)


@pytest.fixture
def anchor_entry():
    """Anchor entry text for origin trace."""
    return "Origin trace — Sovereign Trace Protocol FROZEN-4.0."


@pytest.fixture
def anchor_stamp(anchor_entry, anchor_dt):
    """Stamp generated from anchor_entry at anchor_dt."""
    from sovereign_trace import stamp
    return stamp(anchor_entry, anchor_dt)


@pytest.fixture
def anchor_record(anchor_entry, anchor_dt):
    """SovereignRecord generated from anchor_entry at anchor_dt."""
    from sovereign_trace import stamp_and_record
    return stamp_and_record(anchor_entry, anchor_dt)


@pytest.fixture
def known_seal(anchor_stamp):
    """Expected 64-char hex seal for anchor_entry at anchor_dt."""
    return anchor_stamp.seal


@pytest.fixture
def known_hebrew():
    """Expected Hebrew date for anchor: 14 Adar 5786 [D]."""
    return "14 Adar 5786"


@pytest.fixture
def known_gregorian():
    """Expected Gregorian date for anchor: March 3, 2026."""
    return "March 3, 2026"


@pytest.fixture
def known_dreamspell():
    """Expected Dreamspell for anchor: Day 25, Galactic Moon 8/13."""
    return "Day 25, Galactic Moon 8/13"


@pytest.fixture
def known_unix_utc():
    """Expected Unix timestamp for anchor: 1772550000 (March 3, 2026 15:00 UTC)."""
    return 1772550000


# ═══════════════════════════════════════════════════════════════════
# DATETIME BOUNDARY FIXTURES
# ═══════════════════════════════════════════════════════════════════

@pytest.fixture
def naive_dt():
    """Naive datetime (no tzinfo) — should raise ValueError."""
    return datetime(2026, 3, 3, 15, 0, 0)


@pytest.fixture
def pre_reform_dt():
    """Last Julian date: October 14, 1582 — should raise ValueError [D]."""
    return datetime(1582, 10, 14, tzinfo=timezone.utc)


@pytest.fixture
def first_reform_dt():
    """First valid Gregorian date: October 15, 1582 [D]."""
    return datetime(1582, 10, 15, tzinfo=timezone.utc)


@pytest.fixture
def far_future_dt():
    """Far future date: December 31, 3999."""
    return datetime(3999, 12, 31, tzinfo=timezone.utc)


# ═══════════════════════════════════════════════════════════════════
# HEBREW CALENDAR ANCHOR FIXTURES [D]
# ═══════════════════════════════════════════════════════════════════

@pytest.fixture
def rh_5786_dt():
    """Rosh Hashanah 5786: September 23, 2025 [D] — Hebcal/Chabad verified."""
    return datetime(2025, 9, 23, tzinfo=timezone.utc)


@pytest.fixture
def rh_5787_dt():
    """Rosh Hashanah 5787: September 12, 2026 [D] — pyluach verified."""
    return datetime(2026, 9, 12, tzinfo=timezone.utc)


@pytest.fixture
def erev_rh_5787_dt():
    """Erev Rosh Hashanah 5787: September 11, 2026 = 29 Elul 5786 [D]."""
    return datetime(2026, 9, 11, tzinfo=timezone.utc)


@pytest.fixture
def leap_year_dt():
    """Leap year date: March 25, 2024 = 15 Adar II 5784 [D]."""
    return datetime(2024, 3, 25, tzinfo=timezone.utc)


@pytest.fixture
def day_out_of_time_dt():
    """Day Out of Time: July 25, 2026."""
    return datetime(2026, 7, 25, tzinfo=timezone.utc)


@pytest.fixture
def new_year_dt():
    """13 Moon New Year: July 26, 2026 = Moon 1 Day 1."""
    return datetime(2026, 7, 26, tzinfo=timezone.utc)


# ═══════════════════════════════════════════════════════════════════
# SERIALIZATION FIXTURES
# ═══════════════════════════════════════════════════════════════════

@pytest.fixture
def valid_stamp_dict(anchor_stamp):
    """Pre-built dict from anchor_stamp for from_dict tests."""
    from sovereign_trace import to_dict
    return to_dict(anchor_stamp)


@pytest.fixture
def valid_record_dict(anchor_record):
    """Pre-built dict from anchor_record for from_dict tests."""
    return anchor_record.to_dict()
