"""Named regression guards — one test per named defect, never modify expected values."""
import pytest
from datetime import datetime, timezone, date
from sovereign_trace import stamp, verify, from_dict, SovereignStamp


class TestRegression:
    """Regression tests for named defects from retired versions."""

    @pytest.mark.regression
    def test_regression_frozen_1_not_15_adar(self):
        """Mar 3, 2026 must not → "15 Adar 5786" [D]."""
        dt = datetime(2026, 3, 3, tzinfo=timezone.utc)
        s = stamp("test", dt)
        # Should be 14 Adar, not 15 Adar
        assert "14 Adar" in s.hebrew
        assert "15 Adar" not in s.hebrew

    @pytest.mark.regression
    def test_regression_frozen_1_dehiyot_correct(self):
        """Sep 23, 2025 → 1 Tishri 5786 (not Sep 22) [D]."""
        dt = datetime(2025, 9, 23, tzinfo=timezone.utc)
        s = stamp("test", dt)
        assert "1 Tishri 5786" in s.hebrew

    @pytest.mark.regression
    def test_regression_frozen_2_nfc_normalization(self):
        """NFC/NFD seals match."""
        # NFC form
        entry_nfc = "café"  # U+00E9
        # NFD form
        entry_nfd = "cafe\u0301"  # e + combining acute
        
        dt = datetime(2026, 3, 3, tzinfo=timezone.utc)
        seal_nfc = stamp(entry_nfc, dt).seal
        seal_nfd = stamp(entry_nfd, dt).seal
        
        assert seal_nfc == seal_nfd

    @pytest.mark.regression
    def test_regression_frozen_2_whitespace_normalization(self):
        """" x " seals == "x" seal."""
        dt = datetime(2026, 3, 3, tzinfo=timezone.utc)
        seal_stripped = stamp("  x  ", dt).seal
        seal_plain = stamp("x", dt).seal
        assert seal_stripped == seal_plain

    @pytest.mark.regression
    def test_regression_frozen_2_version_field_present(self):
        """Version in stamp object."""
        dt = datetime(2026, 3, 3, tzinfo=timezone.utc)
        s = stamp("test", dt)
        assert hasattr(s, "version")
        assert s.version == "FROZEN-4.0"

    @pytest.mark.regression
    def test_regression_frozen_2_version_sealed_in_payload(self):
        """Version change → seal change."""
        entry = "test"
        dt = datetime(2026, 3, 3, tzinfo=timezone.utc)
        
        # Current seal with FROZEN-4.0
        seal_4 = stamp(entry, dt).seal
        
        # Manually compute with different version
        import hashlib
        import unicodedata
        normalized = unicodedata.normalize("NFC", entry.strip())
        unix_utc = int(dt.timestamp())
        payload_3 = f"{normalized}|{unix_utc}|FROZEN-3.0"
        seal_3 = hashlib.sha256(payload_3.encode("utf-8")).hexdigest()
        
        assert seal_4 != seal_3

    @pytest.mark.regression
    def test_regression_frozen_2_from_dict_validates_seal_format(self):
        """from_dict validates seal format."""
        from sovereign_trace import to_dict
        dt = datetime(2026, 3, 3, tzinfo=timezone.utc)
        s = stamp("test", dt)
        d = to_dict(s)
        
        # Invalid seal (too short)
        d["seal"] = "abc123"
        with pytest.raises(ValueError):
            from_dict(d)
        
        # Invalid seal (uppercase)
        d["seal"] = s.seal.upper()
        with pytest.raises(ValueError):
            from_dict(d)

    @pytest.mark.regression
    def test_regression_frozen_2_from_dict_validates_fields(self):
        """from_dict validates required fields."""
        from sovereign_trace import to_dict
        dt = datetime(2026, 3, 3, tzinfo=timezone.utc)
        s = stamp("test", dt)
        d = to_dict(s)
        
        # Missing field
        del d["gregorian"]
        with pytest.raises(ValueError):
            from_dict(d)

    @pytest.mark.regression
    def test_regression_frozen_3_rh_5787_is_sep_12(self):
        """CRITICAL — Sep 12, 2026 → 1 Tishri 5787 [D]."""
        dt = datetime(2026, 9, 12, tzinfo=timezone.utc)
        s = stamp("test", dt)
        assert "1 Tishri 5787" in s.hebrew

    @pytest.mark.regression
    def test_regression_frozen_3_sep_22_is_not_rh_5787(self):
        """Sep 22, 2026 → day != 1 [D]."""
        dt = datetime(2026, 9, 22, tzinfo=timezone.utc)
        s = stamp("test", dt)
        # Should be 11 Tishri, not 1 Tishri
        assert "1 Tishri" not in s.hebrew or "11 Tishri" in s.hebrew

    @pytest.mark.regression
    def test_regression_frozen_3_sep_22_is_11_tishri_5787(self):
        """Exact day == 11 [D]."""
        dt = datetime(2026, 9, 22, tzinfo=timezone.utc)
        s = stamp("test", dt)
        assert "11 Tishri 5787" in s.hebrew

    @pytest.mark.regression
    def test_regression_frozen_3_erev_rh_5787_is_sep_11(self):
        """Sep 11, 2026 → 29 Elul 5786 [D]."""
        dt = datetime(2026, 9, 11, tzinfo=timezone.utc)
        s = stamp("test", dt)
        assert "29 Elul 5786" in s.hebrew

    @pytest.mark.regression
    def test_regression_frozen_3_pre_reform_oct_14_raises(self):
        """Month/day guard active."""
        dt = datetime(1582, 10, 14, tzinfo=timezone.utc)
        with pytest.raises(ValueError):
            stamp("test", dt)

    @pytest.mark.regression
    def test_regression_frozen_3_from_dict_rejects_frozen_3_version(self):
        """from_dict rejects FROZEN-3.0 version."""
        from sovereign_trace import to_dict
        dt = datetime(2026, 3, 3, tzinfo=timezone.utc)
        s = stamp("test", dt)
        d = to_dict(s)
        d["version"] = "FROZEN-3.0"
        with pytest.raises(ValueError):
            from_dict(d)

    @pytest.mark.regression
    def test_regression_frozen_3_from_dict_version_check_is_equality(self):
        """from_dict version check is equality."""
        from sovereign_trace import to_dict
        dt = datetime(2026, 3, 3, tzinfo=timezone.utc)
        s = stamp("test", dt)
        d = to_dict(s)
        d["version"] = "FROZEN-4.0-patch"
        with pytest.raises(ValueError):
            from_dict(d)
