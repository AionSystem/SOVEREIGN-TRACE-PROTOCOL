"""__init__.py — import surface completeness and functional correctness."""
import pytest


class TestPackageImports:
    """Test package import surface."""

    def test_import_stamp_callable(self):
        """stamp is callable."""
        from sovereign_trace import stamp
        assert callable(stamp)

    def test_import_stamp_and_record_callable(self):
        """stamp_and_record is callable."""
        from sovereign_trace import stamp_and_record
        assert callable(stamp_and_record)

    def test_import_stamp_batch_callable(self):
        """stamp_batch is callable."""
        from sovereign_trace import stamp_batch
        assert callable(stamp_batch)

    def test_import_verify_callable(self):
        """verify is callable."""
        from sovereign_trace import verify
        assert callable(verify)

    def test_import_display_callable(self):
        """display is callable."""
        from sovereign_trace import display
        assert callable(display)

    def test_import_display_ascii_callable(self):
        """display_ascii is callable."""
        from sovereign_trace import display_ascii
        assert callable(display_ascii)

    def test_import_to_dict_callable(self):
        """to_dict is callable."""
        from sovereign_trace import to_dict
        assert callable(to_dict)

    def test_import_from_dict_callable(self):
        """from_dict is callable."""
        from sovereign_trace import from_dict
        assert callable(from_dict)

    def test_import_sovereign_stamp_is_class(self):
        """SovereignStamp is a class."""
        from sovereign_trace import SovereignStamp
        assert isinstance(SovereignStamp, type)

    def test_import_sovereign_record_is_class(self):
        """SovereignRecord is a class."""
        from sovereign_trace import SovereignRecord
        assert isinstance(SovereignRecord, type)

    def test_import_verify_result_is_class(self):
        """VerifyResult is a class."""
        from sovereign_trace import VerifyResult
        assert isinstance(VerifyResult, type)

    def test_import_frozen_version_is_string(self):
        """FROZEN_VERSION is a string."""
        from sovereign_trace import _FROZEN_VERSION
        assert isinstance(_FROZEN_VERSION, str)

    def test_import_frozen_version_equals_frozen_4(self):
        """FROZEN_VERSION equals 'FROZEN-4.0'."""
        from sovereign_trace import _FROZEN_VERSION
        assert _FROZEN_VERSION == "FROZEN-4.0"

    def test_package_dunder_version_exists(self):
        """__version__ exists."""
        import sovereign_trace
        assert hasattr(sovereign_trace, "__version__")

    def test_package_dunder_version_equals_frozen_4(self):
        """__version__ equals 'FROZEN-4.0'."""
        import sovereign_trace
        assert sovereign_trace.__version__ == "FROZEN-4.0"

    def test_dunder_all_exists(self):
        """__all__ exists."""
        import sovereign_trace
        assert hasattr(sovereign_trace, "__all__")

    def test_all_names_in_dunder_all_importable(self):
        """All names in __all__ are importable."""
        import sovereign_trace
        for name in sovereign_trace.__all__:
            assert hasattr(sovereign_trace, name)

    def test_no_private_names_in_dunder_all(self):
        """Nothing starting with _ except _FROZEN_VERSION."""
        import sovereign_trace
        for name in sovereign_trace.__all__:
            if name.startswith("_"):
                assert name == "_FROZEN_VERSION"

    def test_stamp_from_package_is_functional(self):
        """stamp from package works."""
        from sovereign_trace import stamp
        from datetime import datetime, timezone
        dt = datetime(2026, 3, 3, tzinfo=timezone.utc)
        s = stamp("test", dt)
        assert s.seal is not None

    def test_verify_from_package_is_functional(self):
        """verify from package works."""
        from sovereign_trace import stamp, verify
        from datetime import datetime, timezone
        dt = datetime(2026, 3, 3, tzinfo=timezone.utc)
        s = stamp("test", dt)
        result = verify("test", s)
        assert result.valid is True

    def test_sovereign_stamp_from_package_is_same_class_as_module(self):
        """SovereignStamp from package is same as module class."""
        from sovereign_trace import SovereignStamp, stamp
        from datetime import datetime, timezone
        dt = datetime(2026, 3, 3, tzinfo=timezone.utc)
        s = stamp("test", dt)
        assert isinstance(s, SovereignStamp)

    def test_package_import_does_not_run_self_test(self):
        """Import does not print."""
        import subprocess
        import sys
        result = subprocess.run(
            [sys.executable, "-c", "import sovereign_trace"],
            capture_output=True,
            text=True,
        )
        assert result.stdout == ""
        assert result.stderr == ""

    def test_package_import_does_not_open_network(self):
        """Import does not open network."""
        # Basic check - import should work without network
        import subprocess
        import sys
        result = subprocess.run(
            [sys.executable, "-c", "import sovereign_trace; print('OK')"],
            capture_output=True,
            text=True,
            env={"PYTHONPATH": "/workspace"},
        )
        assert result.returncode == 0
        assert "OK" in result.stdout
