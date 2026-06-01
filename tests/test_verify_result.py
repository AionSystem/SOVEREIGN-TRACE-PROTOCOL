#!/usr/bin/env python3
"""
VerifyResult named tuple — boolean evaluation, field access, unpacking.
"""
import pytest
from collections import namedtuple

from sovereign_trace import VerifyResult


class TestVerifyResultBooleanEvaluation:
    """Test VerifyResult boolean evaluation."""

    def test_valid_true_is_truthy(self):
        result = VerifyResult(True, "VALID")
        assert result

    def test_valid_false_is_falsy(self):
        result = VerifyResult(False, "SEAL_MISMATCH")
        assert not result

    def test_valid_true_bool_is_true(self):
        result = VerifyResult(True, "VALID")
        assert bool(result) is True

    def test_valid_false_bool_is_false(self):
        result = VerifyResult(False, "SEAL_MISMATCH")
        assert bool(result) is False


class TestVerifyResultFieldAccess:
    """Test VerifyResult field access by name and index."""

    def test_valid_field_accessible_by_name(self):
        result = VerifyResult(True, "VALID")
        assert result.valid is True

    def test_reason_field_accessible_by_name(self):
        result = VerifyResult(False, "SEAL_MISMATCH")
        assert result.reason == "SEAL_MISMATCH"

    def test_valid_field_accessible_by_index(self):
        result = VerifyResult(True, "VALID")
        assert result[0] is True

    def test_reason_field_accessible_by_index(self):
        result = VerifyResult(False, "TYPE_ERROR")
        assert result[1] == "TYPE_ERROR"

    def test_result_unpacks_to_two_values(self):
        result = VerifyResult(True, "VALID")
        valid, reason = result
        assert valid is True
        assert reason == "VALID"


class TestVerifyResultType:
    """Test VerifyResult is a NamedTuple."""

    def test_is_named_tuple_instance(self):
        result = VerifyResult(True, "VALID")
        assert isinstance(result, tuple)
        # Check it's a NamedTuple subclass
        assert hasattr(result, "_fields")
        assert result._fields == ("valid", "reason")


class TestVerifyResultReasonStrings:
    """Test VerifyResult reason string values."""

    def test_valid_result_reason_valid(self):
        result = VerifyResult(True, "VALID")
        assert result.reason == "VALID"

    def test_invalid_result_reason_seal_mismatch(self):
        result = VerifyResult(False, "SEAL_MISMATCH")
        assert result.reason == "SEAL_MISMATCH"

    def test_invalid_result_reason_type_error(self):
        result = VerifyResult(False, "TYPE_ERROR")
        assert result.reason == "TYPE_ERROR"

    def test_all_three_reason_strings_defined(self):
        # The three standard reason strings
        reasons = {"VALID", "SEAL_MISMATCH", "TYPE_ERROR"}
        result_valid = VerifyResult(True, "VALID")
        result_tampered = VerifyResult(False, "SEAL_MISMATCH")
        result_type_error = VerifyResult(False, "TYPE_ERROR")
        assert result_valid.reason in reasons
        assert result_tampered.reason in reasons
        assert result_type_error.reason in reasons


class TestVerifyResultEquality:
    """Test VerifyResult equality by value."""

    def test_equality_by_value(self):
        result1 = VerifyResult(True, "VALID")
        result2 = VerifyResult(True, "VALID")
        assert result1 == result2

        result3 = VerifyResult(False, "SEAL_MISMATCH")
        result4 = VerifyResult(False, "SEAL_MISMATCH")
        assert result3 == result4

        assert result1 != result3


class TestVerifyResultImmutability:
    """Test VerifyResult is immutable (NamedTuple property)."""

    def test_immutable_namedtuple(self):
        result = VerifyResult(True, "VALID")
        with pytest.raises(AttributeError):
            result.valid = False
