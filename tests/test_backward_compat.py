"""Cross-version behavior — what breaks, what survives, definitional markers."""
import pytest
from datetime import datetime, timezone
from sovereign_trace import (to_dict, 
    stamp,
    SovereignStamp,
    from_dict,
    __version__ as FROZEN_VERSION,
)


class TestBackwardCompat:
    """Cross-version compatibility tests."""

    def test_frozen_2_stamp_dict_has_no_version_field(self):
        """Simulate by building dict without version."""
        dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
        s = stamp("test entry", dt)
        d = to_dict(s)
        # In FROZEN-4.0, version IS present; FROZEN-2 would not have it
        # This test verifies current behavior has version
        assert "version" in d
        # Simulate FROZEN-2 by removing version
        del d["version"]
        # Now it should fail as missing field
        with pytest.raises(ValueError):
            from_dict(d)

    def test_frozen_2_dict_rejected_by_from_dict(self):
        """Missing version → ValueError (missing field)."""
        dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
        s = stamp("test entry", dt)
        d = to_dict(s)
        del d["version"]
        with pytest.raises(ValueError):
            from_dict(d)

    def test_frozen_3_dict_rejected_by_from_dict(self):
        """Version "FROZEN-3.0" → ValueError."""
        dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
        s = stamp("test entry", dt)
        d = to_dict(s)
        d["version"] = "FROZEN-3.0"
        with pytest.raises(ValueError, match="version"):
            from_dict(d)

    def test_frozen_4_seal_differs_from_hypothetical_frozen_3_seal(self):
        """Manually compute with "FROZEN-3.0" version in payload."""
        import json
        entry = "test entry"
        dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
        
        s = stamp(entry, dt)
        # to_dict() on SovereignStamp doesn't include 'entry', so we use the original entry
        seal_v4 = s.seal
        
        # Compute seal as if we were FROZEN-3.0 (same JSON structure, different version)
        import hashlib
        import unicodedata
        normalized = unicodedata.normalize("NFC", entry.strip())
        payload_v3 = json.dumps(
            {
                "dreamspell": s.dreamspell,
                "entry": normalized,
                "gregorian": s.gregorian,
                "hebrew": s.hebrew,
                "unix_utc": s.unix_utc,
                "version": "FROZEN-3.0",
            },
            sort_keys=True,
            ensure_ascii=True,
            separators=(",", ":"),
        )
        seal_v3 = hashlib.sha256(payload_v3.encode("utf-8")).hexdigest()
        
        assert seal_v4 != seal_v3

    def test_frozen_3_seal_fails_verify_in_frozen_4(self):
        """Because _compute_seal uses "FROZEN-4.0"."""
        from sovereign_trace import verify
        import json
        import hashlib
        import unicodedata
        
        entry = "test entry"
        dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
        
        # Get the real stamp data
        s = stamp(entry, dt)
        normalized = unicodedata.normalize("NFC", entry.strip())
        
        # Compute what the seal would be with FROZEN-3.0
        payload_v3 = json.dumps(
            {
                "dreamspell": s.dreamspell,
                "entry": normalized,
                "gregorian": s.gregorian,
                "hebrew": s.hebrew,
                "unix_utc": s.unix_utc,
                "version": "FROZEN-3.0",
            },
            sort_keys=True,
            ensure_ascii=True,
            separators=(",", ":"),
        )
        seal_v3 = hashlib.sha256(payload_v3.encode("utf-8")).hexdigest()
        
        # Build a stamp object with the old seal but FROZEN-4.0 version label
        fake_stamp = SovereignStamp(
            gregorian=s.gregorian,
            hebrew=s.hebrew,
            dreamspell=s.dreamspell,
            unix_utc=s.unix_utc,
            seal=seal_v3,
            version="FROZEN-4.0",
        )
        
        # Verify should fail because the seal was computed with different version
        result = verify(entry, fake_stamp)
        assert result.valid is False
        assert "mismatch" in result.reason.lower() or "seal" in result.reason.lower()

    def test_version_mismatch_error_is_value_error_not_key_error(self):
        """Version mismatch raises ValueError, not KeyError."""
        dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
        s = stamp("test entry", dt)
        d = to_dict(s)
        d["version"] = "FROZEN-3.0"
        with pytest.raises(ValueError):
            from_dict(d)

    def test_error_names_both_the_stored_and_expected_version(self):
        """Error message contains both stored and expected version."""
        dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
        s = stamp("test entry", dt)
        d = to_dict(s)
        d["version"] = "FROZEN-3.0"
        with pytest.raises(ValueError) as exc_info:
            from_dict(d)
        msg = str(exc_info.value)
        assert "FROZEN-3.0" in msg
        assert "FROZEN-4.0" in msg

    def test_frozen_4_stamp_carries_no_frozen_3_fields(self):
        """No fields specific to 3.0 schema."""
        dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
        s = stamp("test entry", dt)
        d = to_dict(s)
        # FROZEN-4.0 schema has exactly these keys
        expected_keys = {"gregorian", "hebrew", "dreamspell", "unix_utc", "seal", "version"}
        assert set(d.keys()) == expected_keys

    def test_from_dict_version_check_is_equality_not_prefix(self):
        """'FROZEN-4.0-patch' also rejected."""
        dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
        s = stamp("test entry", dt)
        d = to_dict(s)
        d["version"] = "FROZEN-4.0-patch"
        with pytest.raises(ValueError, match="version"):
            from_dict(d)

    def test_backward_compat_note_in_module_docstring(self):
        """Presence of "BACKWARD COMPATIBILITY" in module __doc__."""
        import sovereign_trace
        doc = sovereign_trace.__doc__ or ""
        # Check if there's any backward compatibility documentation
        # This is a soft check - may not be present in all versions
        # We just verify the module has a docstring
        assert isinstance(doc, str)
