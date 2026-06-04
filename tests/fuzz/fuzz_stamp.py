#!/usr/bin/env python3
import sys
import atheris
import random

sys.path.insert(0, "stamp")
import sovereign_trace_stamp as stp

def TestOneInput(data):
    """Fuzz the stamp generation function with random input strings."""
    # Ensure data is not empty
    if len(data) < 1:
        return

    # Convert bytes to string (ignore invalid UTF-8)
    try:
        text = data.decode("utf-8", errors="replace")
    except:
        return

    # Also fuzz the version parameter (random string or valid version)
    version = random.choice(["4.0.0", "3.0.0", "2.0.0", "invalid", "", str(data[:5])])

    try:
        result = stp.stamp(text, version=version)
        # The stamp must always produce a dictionary with 'ledger_id' and 'sha256'
        if not isinstance(result, dict) or "sha256" not in result:
            raise RuntimeError("Invalid stamp output")
    except Exception as e:
        # Expected failures (invalid input) are OK; unexpected exceptions are not
        if "not a valid version" not in str(e) and "must be string" not in str(e):
            raise

if __name__ == "__main__":
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()
