"""
test_file_integrity.py — _FROZEN_FILE_SHA256 sentinel and file integrity concept.
"""
import pytest
import hashlib
import os
from pathlib import Path

import sovereign_trace.sovereign_trace_stamp as stp
from sovereign_trace.sovereign_trace_stamp import _FROZEN_FILE_SHA256, _FROZEN_VERSION


class TestFileIntegrity:
    """_FROZEN_FILE_SHA256 sentinel and file integrity concept."""

    def test_frozen_sha256_constant_exists(self):
        """Attribute accessible."""
        assert hasattr(stp, '_FROZEN_FILE_SHA256')

    def test_frozen_sha256_is_string(self):
        """Is a string."""
        assert isinstance(_FROZEN_FILE_SHA256, str)

    def test_frozen_sha256_pre_release_value(self):
        """SET_AT_RELEASE_TIME OR 64-char hex."""
        # In pre-release, this should be the sentinel value
        assert _FROZEN_FILE_SHA256 in ("SET_AT_RELEASE_TIME", "") or len(_FROZEN_FILE_SHA256) == 64

    def test_frozen_sha256_if_set_is_valid_format(self):
        """When not sentinel, is 64-char lowercase hex."""
        if _FROZEN_FILE_SHA256 not in ("SET_AT_RELEASE_TIME", ""):
            assert len(_FROZEN_FILE_SHA256) == 64
            assert _FROZEN_FILE_SHA256 == _FROZEN_FILE_SHA256.lower()
            # Verify it's valid hex
            int(_FROZEN_FILE_SHA256, 16)

    def test_file_sha256_computable(self):
        """hashlib.sha256(open(file,"rb").read()).hexdigest() works."""
        # Get the path to the main module file
        module_file = Path(stp.__file__)
        
        with open(module_file, "rb") as f:
            content = f.read()
        
        sha256_hash = hashlib.sha256(content).hexdigest()
        
        assert len(sha256_hash) == 64
        assert sha256_hash == sha256_hash.lower()

    def test_file_sha256_deterministic(self):
        """Same file → same sha256 on two reads."""
        module_file = Path(stp.__file__)
        
        with open(module_file, "rb") as f:
            content1 = f.read()
        sha256_1 = hashlib.sha256(content1).hexdigest()
        
        with open(module_file, "rb") as f:
            content2 = f.read()
        sha256_2 = hashlib.sha256(content2).hexdigest()
        
        assert sha256_1 == sha256_2

    def test_file_sha256_changes_on_tamper(self, tmp_path):
        """Modify one byte → different sha256."""
        # Create a temporary file with known content
        test_file = tmp_path / "test_file.txt"
        original_content = b"Hello, World!"
        
        test_file.write_bytes(original_content)
        
        # Compute original hash
        with open(test_file, "rb") as f:
            original_hash = hashlib.sha256(f.read()).hexdigest()
        
        # Modify one byte
        tampered_content = original_content[:5] + b'X' + original_content[6:]
        test_file.write_bytes(tampered_content)
        
        # Compute tampered hash
        with open(test_file, "rb") as f:
            tampered_hash = hashlib.sha256(f.read()).hexdigest()
        
        # Hashes should differ
        assert original_hash != tampered_hash
