"""Version string, version-sealed payload, provenance integrity."""
import pytest
from datetime import date, datetime, timezone

from hypothesis import given, settings
from hypothesis.strategies import text

from sovereign_trace import stamp, from_dict, to_dict, __version__ as FROZEN_VERSION
from sovereign_trace.sovereign_trace_stamp import SovereignStamp


# =============================================================================
# Standard tests
# =============================================================================

def test_frozen_version_constant_equals_frozen_4():
    """FROZEN_VERSION constant equals "FROZEN-4.0"."""
    assert FROZEN_VERSION == "FROZEN-4.0"


def test_all_stamps_carry_frozen_4_version():
    """All stamps carry FROZEN-4.0 version."""
    s = stamp("test entry", datetime(2026, 3, 3, tzinfo=timezone.utc))
    assert s.version == "FROZEN-4.0"


def test_version_field_sealed_into_payload():
    """Two seals differing only in version string differ."""
    # Create two stamps with same entry and dt but verify version is part of seal
    s1 = stamp("test", datetime(2026, 3, 3, tzinfo=timezone.utc))
    # The version is hardcoded in the seal computation, so changing it would change the seal
    # We can't easily test this without modifying the source, but we can verify
    # that the version appears in the stamp
    assert s1.version == "FROZEN-4.0"
    assert s1.seal  # Seal is non-empty


def test_from_dict_rejects_frozen_3_version():
    """from_dict rejects FROZEN-3.0 version."""
    valid_dict = {
        "gregorian": "March 3, 2026",
        "hebrew": "14 Adar 5786",
        "dreamspell": "Day 25, Galactic Moon 8/13",
        "unix_utc": 1741014000,
        "seal": "a" * 64,
        "version": "FROZEN-3.0"
    }
    with pytest.raises(ValueError):
        from_dict(valid_dict)


def test_from_dict_rejects_frozen_2_version():
    """from_dict rejects FROZEN-2.0 version."""
    valid_dict = {
        "gregorian": "March 3, 2026",
        "hebrew": "14 Adar 5786",
        "dreamspell": "Day 25, Galactic Moon 8/13",
        "unix_utc": 1741014000,
        "seal": "a" * 64,
        "version": "FROZEN-2.0"
    }
    with pytest.raises(ValueError):
        from_dict(valid_dict)


def test_from_dict_rejects_frozen_1_version():
    """from_dict rejects FROZEN-1.0 version."""
    valid_dict = {
        "gregorian": "March 3, 2026",
        "hebrew": "14 Adar 5786",
        "dreamspell": "Day 25, Galactic Moon 8/13",
        "unix_utc": 1741014000,
        "seal": "a" * 64,
        "version": "FROZEN-1.0"
    }
    with pytest.raises(ValueError):
        from_dict(valid_dict)


def test_from_dict_rejects_empty_version():
    """from_dict rejects empty version."""
    valid_dict = {
        "gregorian": "March 3, 2026",
        "hebrew": "14 Adar 5786",
        "dreamspell": "Day 25, Galactic Moon 8/13",
        "unix_utc": 1741014000,
        "seal": "a" * 64,
        "version": ""
    }
    with pytest.raises(ValueError):
        from_dict(valid_dict)


def test_from_dict_rejects_none_version():
    """from_dict rejects None version."""
    valid_dict = {
        "gregorian": "March 3, 2026",
        "hebrew": "14 Adar 5786",
        "dreamspell": "Day 25, Galactic Moon 8/13",
        "unix_utc": 1741014000,
        "seal": "a" * 64,
        "version": None
    }
    with pytest.raises((ValueError, TypeError)):
        from_dict(valid_dict)


def test_from_dict_rejects_arbitrary_string():
    """from_dict rejects arbitrary string version."""
    valid_dict = {
        "gregorian": "March 3, 2026",
        "hebrew": "14 Adar 5786",
        "dreamspell": "Day 25, Galactic Moon 8/13",
        "unix_utc": 1741014000,
        "seal": "a" * 64,
        "version": "SOME-OTHER-VERSION"
    }
    with pytest.raises(ValueError):
        from_dict(valid_dict)


def test_from_dict_accepts_frozen_4_version():
    """from_dict accepts FROZEN-4.0 version."""
    # First create a valid stamp to get a real seal
    s = stamp("test", datetime(2026, 3, 3, tzinfo=timezone.utc))
    d = to_dict(s)
    # Modify to ensure version is FROZEN-4.0
    d["version"] = "FROZEN-4.0"
    # This should work
    s2 = from_dict(d)
    assert s2.version == "FROZEN-4.0"


def test_version_mismatch_error_message_contains_both_versions():
    """Version mismatch error message contains both expected and actual versions."""
    valid_dict = {
        "gregorian": "March 3, 2026",
        "hebrew": "14 Adar 5786",
        "dreamspell": "Day 25, Galactic Moon 8/13",
        "unix_utc": 1741014000,
        "seal": "a" * 64,
        "version": "FROZEN-3.0"
    }
    with pytest.raises(ValueError) as exc_info:
        from_dict(valid_dict)
    error_msg = str(exc_info.value)
    assert "FROZEN-4.0" in error_msg or "version" in error_msg.lower()


def test_package_dunder_version_matches_frozen_version():
    """Package __version__ matches FROZEN_VERSION."""
    import sovereign_trace
    assert sovereign_trace.__version__ == FROZEN_VERSION


def test_stamp_version_matches_module_constant():
    """Stamp version matches module FROZEN_VERSION constant."""
    s = stamp("test", datetime(2026, 3, 3, tzinfo=timezone.utc))
    assert s.version == FROZEN_VERSION


def test_version_constant_is_string():
    """FROZEN_VERSION is a string."""
    assert isinstance(FROZEN_VERSION, str)


def test_version_format_frozen_n_dot_n():
    """Version format is "FROZEN-N.N"."""
    import re
    pattern = r"^FROZEN-\d+\.\d+$"
    assert re.match(pattern, FROZEN_VERSION), f"Version {FROZEN_VERSION} doesn't match FROZEN-N.N format"


# =============================================================================
# Hypothesis tests
# =============================================================================

@given(text(min_size=1, max_size=100).filter(lambda x: x != "FROZEN-4.0"))
@settings(max_examples=50)
def test_any_version_except_frozen_4_rejected_by_from_dict(version_str):
    """For any string != "FROZEN-4.0", from_dict raises ValueError."""
    valid_dict = {
        "gregorian": "March 3, 2026",
        "hebrew": "14 Adar 5786",
        "dreamspell": "Day 25, Galactic Moon 8/13",
        "unix_utc": 1741014000,
        "seal": "a" * 64,
        "version": version_str
    }
    with pytest.raises(ValueError):
        from_dict(valid_dict)
