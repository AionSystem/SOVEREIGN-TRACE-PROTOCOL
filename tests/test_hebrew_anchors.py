"""
test_hebrew_anchors.py
Hebrew date conversion — verified anchor values only. [D]-tagged.
Do not modify expected values without re-verifying against Hebcal, Chabad, and pyluach.
"""
import pytest
from datetime import date
from sovereign_trace.sovereign_trace_stamp import _gregorian_to_hebrew


class TestHebrewAnchors:
    """Anchor tests with verified values from Hebcal, Chabad, pyluach [D]."""

    def test_anchor_rh_5786(self):
        """Sep 23, 2025 → (5786, "Tishri", 1) [D]"""
        h_year, h_month, h_day = _gregorian_to_hebrew(2025, 9, 23)
        assert h_year == 5786
        assert h_month == "Tishri"
        assert h_day == 1

    def test_anchor_yom_kippur_5786(self):
        """Oct 2, 2025 → (5786, "Tishri", 10) [D]"""
        h_year, h_month, h_day = _gregorian_to_hebrew(2025, 10, 2)
        assert h_year == 5786
        assert h_month == "Tishri"
        assert h_day == 10

    def test_anchor_purim_5786(self):
        """Mar 3, 2026 → (5786, "Adar", 14) [D]"""
        h_year, h_month, h_day = _gregorian_to_hebrew(2026, 3, 3)
        assert h_year == 5786
        assert h_month == "Adar"
        assert h_day == 14

    def test_anchor_1_nisan_5786(self):
        """Mar 19, 2026 → (5786, "Nisan", 1) [D]"""
        h_year, h_month, h_day = _gregorian_to_hebrew(2026, 3, 19)
        assert h_year == 5786
        assert h_month == "Nisan"
        assert h_day == 1

    def test_anchor_passover_5786(self):
        """Apr 2, 2026 → (5786, "Nisan", 15) [D]"""
        h_year, h_month, h_day = _gregorian_to_hebrew(2026, 4, 2)
        assert h_year == 5786
        assert h_month == "Nisan"
        assert h_day == 15

    def test_anchor_erev_rh_5786(self):
        """Sep 22, 2025 → (5785, "Elul", 29) [D] - Erev Rosh Hashanah is still in previous year"""
        h_year, h_month, h_day = _gregorian_to_hebrew(2025, 9, 22)
        assert h_year == 5785
        assert h_month == "Elul"
        assert h_day == 29

    def test_anchor_15_adar_ii_5784(self):
        """Mar 25, 2024 → (5784, "Adar II", 15) [D]"""
        h_year, h_month, h_day = _gregorian_to_hebrew(2024, 3, 25)
        assert h_year == 5784
        assert h_month == "Adar II"
        assert h_day == 15

    def test_anchor_1_adar_i_5784(self):
        """Feb 10, 2024 → (5784, "Adar I", 1) [D]"""
        h_year, h_month, h_day = _gregorian_to_hebrew(2024, 2, 10)
        assert h_year == 5784
        assert h_month == "Adar I"
        assert h_day == 1

    def test_anchor_rh_5787(self):
        """Sep 12, 2026 → (5787, "Tishri", 1) [D] CRITICAL correction from FROZEN-3.0"""
        h_year, h_month, h_day = _gregorian_to_hebrew(2026, 9, 12)
        assert h_year == 5787
        assert h_month == "Tishri"
        assert h_day == 1

    def test_anchor_erev_rh_5787(self):
        """Sep 11, 2026 → (5786, "Elul", 29) [D]"""
        h_year, h_month, h_day = _gregorian_to_hebrew(2026, 9, 11)
        assert h_year == 5786
        assert h_month == "Elul"
        assert h_day == 29

    def test_anchor_5784_tishri_22(self):
        """Oct 7, 2023 → (5784, "Tishri", 22) [D]"""
        h_year, h_month, h_day = _gregorian_to_hebrew(2023, 10, 7)
        assert h_year == 5784
        assert h_month == "Tishri"
        assert h_day == 22

    def test_anchor_sep_22_2026_is_11_tishri_not_rh(self):
        """Sep 22, 2026 → day == 11, month == "Tishri" [D] regression guard"""
        h_year, h_month, h_day = _gregorian_to_hebrew(2026, 9, 22)
        assert h_year == 5787
        assert h_month == "Tishri"
        assert h_day == 11

    def test_anchor_hebrew_string_format_purim(self):
        """_hebrew(date(2026,3,3)) == "14 Adar 5786" """
        from sovereign_trace.sovereign_trace_stamp import _hebrew
        greg_date = date(2026, 3, 3)
        hebrew_str = _hebrew(greg_date)
        assert hebrew_str == "14 Adar 5786"

    def test_anchor_hebrew_string_format_rh(self):
        """_hebrew(date(2025,9,23)) == "1 Tishri 5786" """
        from sovereign_trace.sovereign_trace_stamp import _hebrew
        greg_date = date(2025, 9, 23)
        hebrew_str = _hebrew(greg_date)
        assert hebrew_str == "1 Tishri 5786"

    def test_anchor_hebrew_string_format_adar_ii(self):
        """_hebrew(date(2024,3,25)) == "15 Adar II 5784" """
        from sovereign_trace.sovereign_trace_stamp import _hebrew
        greg_date = date(2024, 3, 25)
        hebrew_str = _hebrew(greg_date)
        assert hebrew_str == "15 Adar II 5784"
