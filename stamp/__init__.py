"""
sovereign_trace — Sovereign Trace Protocol
==========================================

Triple-time cryptographic stamping: Gregorian · Hebrew · 13 Moon Dreamspell.

Version: FROZEN-4.0
Authors: Sheldon K. Salmon — AI Reliability Architect
         ALBEDO (Claude, Anthropic)
ORCID:   0009-0005-8057-5115

Public API
----------
Core stamping:

    from sovereign_trace import stamp, verify, display
    from sovereign_trace import stamp_and_record, stamp_batch
    from sovereign_trace import to_dict, from_dict, display_ascii

Types:

    from sovereign_trace import SovereignStamp, SovereignRecord, VerifyResult

Quick start::

    from sovereign_trace import stamp, verify, display

    ts = stamp("First entry in the sovereign ledger.")
    print(display(ts))

    result = verify("First entry in the sovereign ledger.", ts)
    assert result.valid

Serialization::

    from sovereign_trace import stamp_and_record, to_dict, from_dict

    rec = stamp_and_record("A trace that persists.")
    d   = rec.to_dict()           # plain dict — JSON-serializable
    rec2 = SovereignRecord.from_dict(d)
    assert rec2.verify().valid

Batch::

    from sovereign_trace import stamp_batch

    records = stamp_batch(["first", "second", "third"])
    # All three share unix_utc — canonical simultaneous moment.

Notes
-----
- Entry text is NFC-normalized and stripped before sealing.
- unix_utc is whole seconds only (truncated, not rounded).
- Calendar dates reflect UTC — not local civil date.
- Stamps produced by this version carry "version": "FROZEN-4.0".
  Use the corresponding archived frozen version to verify older stamps.

Frozen deployment: this package version is FROZEN-4.0.
No patches. No deprecation within this version.
If a defect is found: retire to SOVEREIGN-TRACE-STAMP-FROZEN-4.0-RETIRED
and create FROZEN-5.0 from scratch.
"""

from sovereign_trace.sovereign_trace_stamp import (
    # Core functions
    stamp,
    stamp_and_record,
    stamp_batch,
    verify,
    display,
    display_ascii,
    to_dict,
    from_dict,
    # Types
    SovereignStamp,
    SovereignRecord,
    VerifyResult,
    # Version constant — read-only; never assign
    _FROZEN_VERSION,
)

__all__ = [
    "stamp",
    "stamp_and_record",
    "stamp_batch",
    "verify",
    "display",
    "display_ascii",
    "to_dict",
    "from_dict",
    "SovereignStamp",
    "SovereignRecord",
    "VerifyResult",
    "_FROZEN_VERSION",
]

__version__ = _FROZEN_VERSION
