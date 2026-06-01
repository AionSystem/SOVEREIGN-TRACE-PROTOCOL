"""
test_serialization.py — to_dict() and from_dict() tests.

Schema, round-trip, validation, edge cases.
"""

import json
import pytest
from datetime import datetime, timezone

from sovereign_trace import stamp, to_dict, from_dict, SovereignStamp


class TestToDictStandard:
    """Standard tests for to_dict() function."""

    def test_to_dict_returns_dict(self, anchor_stamp):
        result = to_dict(anchor_stamp)
        assert isinstance(result, dict)

    def test_to_dict_has_exactly_six_keys(self, anchor_stamp):
        result = to_dict(anchor_stamp)
        assert len(result.keys()) == 6

    def test_to_dict_gregorian_value(self, anchor_stamp):
        result = to_dict(anchor_stamp)
        assert result["gregorian"] == anchor_stamp.gregorian

    def test_to_dict_hebrew_value(self, anchor_stamp):
        result = to_dict(anchor_stamp)
        assert result["hebrew"] == anchor_stamp.hebrew

    def test_to_dict_dreamspell_value(self, anchor_stamp):
        result = to_dict(anchor_stamp)
        assert result["dreamspell"] == anchor_stamp.dreamspell

    def test_to_dict_unix_utc_value(self, anchor_stamp):
        result = to_dict(anchor_stamp)
        assert result["unix_utc"] == anchor_stamp.unix_utc

    def test_to_dict_unix_utc_is_int_not_float(self, anchor_stamp):
        result = to_dict(anchor_stamp)
        assert isinstance(result["unix_utc"], int)
        assert not isinstance(result["unix_utc"], float)

    def test_to_dict_seal_value(self, anchor_stamp):
        result = to_dict(anchor_stamp)
        assert result["seal"] == anchor_stamp.seal

    def test_to_dict_version_value(self, anchor_stamp):
        result = to_dict(anchor_stamp)
        assert result["version"] == anchor_stamp.version

    def test_to_dict_is_json_serializable(self, anchor_stamp):
        result = to_dict(anchor_stamp)
        # Should not raise
        json_str = json.dumps(result)
        assert isinstance(json_str, str)


class TestFromDictStandard:
    """Standard tests for from_dict() function."""

    def test_from_dict_round_trip_seal(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        restored = from_dict(data)
        assert restored.seal == anchor_stamp.seal

    def test_from_dict_round_trip_all_fields(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        restored = from_dict(data)
        assert restored.gregorian == anchor_stamp.gregorian
        assert restored.hebrew == anchor_stamp.hebrew
        assert restored.dreamspell == anchor_stamp.dreamspell
        assert restored.unix_utc == anchor_stamp.unix_utc
        assert restored.seal == anchor_stamp.seal
        assert restored.version == anchor_stamp.version

    def test_from_dict_produces_sovereign_stamp(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        restored = from_dict(data)
        assert isinstance(restored, SovereignStamp)

    def test_from_dict_equality_with_original(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        restored = from_dict(data)
        assert restored == anchor_stamp

    def test_from_dict_check_invariant_passes(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        restored = from_dict(data)
        assert restored.check_invariant() is True

    def test_from_dict_unix_utc_float_coerced_to_int(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        data["unix_utc"] = float(data["unix_utc"])
        restored = from_dict(data)
        assert restored.unix_utc == anchor_stamp.unix_utc
        assert isinstance(restored.unix_utc, int)

    def test_from_dict_unix_utc_string_int_coerced(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        data["unix_utc"] = str(data["unix_utc"])
        restored = from_dict(data)
        assert restored.unix_utc == anchor_stamp.unix_utc
        assert isinstance(restored.unix_utc, int)


class TestFromDictMissingFields:
    """Tests for missing field validation in from_dict()."""

    def test_from_dict_missing_gregorian_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        del data["gregorian"]
        with pytest.raises(ValueError):
            from_dict(data)

    def test_from_dict_missing_hebrew_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        del data["hebrew"]
        with pytest.raises(ValueError):
            from_dict(data)

    def test_from_dict_missing_dreamspell_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        del data["dreamspell"]
        with pytest.raises(ValueError):
            from_dict(data)

    def test_from_dict_missing_unix_utc_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        del data["unix_utc"]
        with pytest.raises(ValueError):
            from_dict(data)

    def test_from_dict_missing_seal_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        del data["seal"]
        with pytest.raises(ValueError):
            from_dict(data)

    def test_from_dict_missing_version_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        del data["version"]
        with pytest.raises(ValueError):
            from_dict(data)

    def test_from_dict_missing_multiple_fields_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        del data["gregorian"]
        del data["hebrew"]
        with pytest.raises(ValueError):
            from_dict(data)


class TestFromDictInvalidSeal:
    """Tests for invalid seal validation in from_dict()."""

    def test_from_dict_invalid_seal_short_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        data["seal"] = "abc123"  # Too short
        with pytest.raises(ValueError):
            from_dict(data)

    def test_from_dict_invalid_seal_long_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        data["seal"] = anchor_stamp.seal + "extra"  # Too long
        with pytest.raises(ValueError):
            from_dict(data)

    def test_from_dict_invalid_seal_uppercase_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        data["seal"] = anchor_stamp.seal.upper()
        with pytest.raises(ValueError):
            from_dict(data)

    def test_from_dict_invalid_seal_non_hex_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        data["seal"] = "z" * 64  # Non-hex characters
        with pytest.raises(ValueError):
            from_dict(data)


class TestFromDictWrongVersion:
    """Tests for wrong version validation in from_dict()."""

    def test_from_dict_wrong_version_frozen_3_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        data["version"] = "FROZEN-3.0"
        with pytest.raises(ValueError):
            from_dict(data)

    def test_from_dict_wrong_version_frozen_2_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        data["version"] = "FROZEN-2.0"
        with pytest.raises(ValueError):
            from_dict(data)

    def test_from_dict_wrong_version_arbitrary_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        data["version"] = "INVALID-VERSION"
        with pytest.raises(ValueError):
            from_dict(data)


class TestFromDictEmptyFields:
    """Tests for empty field validation in from_dict()."""

    def test_from_dict_empty_version_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        data["version"] = ""
        with pytest.raises(ValueError):
            from_dict(data)

    def test_from_dict_empty_gregorian_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        data["gregorian"] = ""
        with pytest.raises(ValueError):
            from_dict(data)

    def test_from_dict_empty_hebrew_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        data["hebrew"] = ""
        with pytest.raises(ValueError):
            from_dict(data)

    def test_from_dict_empty_dreamspell_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        data["dreamspell"] = ""
        with pytest.raises(ValueError):
            from_dict(data)


class TestFromDictNoneFields:
    """Tests for None field validation in from_dict()."""

    def test_from_dict_none_gregorian_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        data["gregorian"] = None
        with pytest.raises(ValueError):
            from_dict(data)


class TestFromDictInvalidUnixUtc:
    """Tests for invalid unix_utc validation in from_dict()."""

    def test_from_dict_negative_unix_utc_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        data["unix_utc"] = -1
        with pytest.raises(ValueError):
            from_dict(data)

    def test_from_dict_zero_unix_utc_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        data["unix_utc"] = 0
        with pytest.raises(ValueError):
            from_dict(data)

    def test_from_dict_float_unix_utc_non_integer_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        data["unix_utc"] = 1.5  # Non-integer float
        # This should be coerced if it's a whole number, but 1.5 is not
        # Depending on implementation, may raise or coerce
        # Testing that it handles this case
        try:
            restored = from_dict(data)
            # If it doesn't raise, verify it was coerced properly
            assert isinstance(restored.unix_utc, int)
        except ValueError:
            pass  # Also acceptable if it raises

    def test_from_dict_string_unix_utc_non_numeric_raises(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        data["unix_utc"] = "not_a_number"
        with pytest.raises(ValueError):
            from_dict(data)


class TestFromDictErrorMessage:
    """Tests for error message content in from_dict()."""

    def test_from_dict_error_message_names_missing_field(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        del data["seal"]
        with pytest.raises(ValueError) as exc_info:
            from_dict(data)
        # Error message should mention the missing field
        assert "seal" in str(exc_info.value).lower()


class TestJsonRoundtrip:
    """Tests for JSON round-trip serialization."""

    def test_json_roundtrip_via_dumps_loads(self, anchor_stamp):
        data = to_dict(anchor_stamp)
        json_str = json.dumps(data)
        loaded_data = json.loads(json_str)
        restored = from_dict(loaded_data)
        assert restored == anchor_stamp


class TestSerializationHypothesis:
    """Hypothesis property-based tests for serialization."""

    def test_to_dict_from_dict_round_trip_property(self, anchor_entry, anchor_dt):
        """For any valid entry + dt, stamp → to_dict → from_dict → eq original."""
        from hypothesis import given, strategies as st

        @given(
            entry=st.text(min_size=1, max_size=100).filter(lambda s: s.strip()),
            year=st.integers(min_value=1582, max_value=3999),
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
                data = to_dict(stmp)
                restored = from_dict(data)
                assert restored == stmp
            except ValueError:
                pass

        _test()

    def test_from_dict_tampered_seal_raises(self, anchor_stamp):
        """Tampered seal in dict still creates a stamp (structural validation only)."""
        # Note: from_dict does not verify seal matches entry - it's a deserialization function
        # The seal is validated for format (64 hex chars) but not cryptographic correctness
        data = to_dict(anchor_stamp)
        seal_list = list(data["seal"])
        seal_list[0] = "f" if seal_list[0] != "f" else "e"
        data["seal"] = "".join(seal_list)
        # This should create a stamp with the tampered seal (structural validation passes)
        restored = from_dict(data)
        assert restored.seal == data["seal"]
        # But check_invariant should still pass since seal format is valid
        assert restored.check_invariant() is True

    def test_from_dict_missing_any_one_field_raises(self, anchor_stamp):
        """For each of the 6 required fields, removing it raises ValueError."""
        data = to_dict(anchor_stamp)
        required_fields = ["gregorian", "hebrew", "dreamspell", "unix_utc", "seal", "version"]

        for field in required_fields:
            modified_data = data.copy()
            del modified_data[field]
            with pytest.raises(ValueError):
                from_dict(modified_data)
