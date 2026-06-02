"""
Async wrappers around the synchronous API — simulating future async vault/ledger
integration. The package is sync; these tests verify the API is safe to call
from async contexts and document patterns for Stage 2 (vault) and Stage 3 (ledger).
"""
import pytest
import asyncio
from datetime import datetime, timezone

from sovereign_trace.sovereign_trace_stamp import (
    stamp,
    stamp_and_record,
    stamp_batch,
    verify,
    to_dict,
    from_dict,
    display,
    SovereignRecord,
)

pytestmark = pytest.mark.asyncio


async def test_async_stamp_returns_sovereign_stamp():
    """await asyncio.to_thread(stamp, entry, dt) returns SovereignStamp."""
    entry = "Async test entry"
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    result = await asyncio.to_thread(stamp, entry, dt)
    assert hasattr(result, 'seal')
    assert hasattr(result, 'gregorian')
    assert len(result.seal) == 64


async def test_async_stamp_deterministic():
    """Two async calls with same input produce same result."""
    entry = "Deterministic async"
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    result1 = await asyncio.to_thread(stamp, entry, dt)
    result2 = await asyncio.to_thread(stamp, entry, dt)
    assert result1.seal == result2.seal


async def test_async_stamp_and_record():
    """to_thread wrapper for stamp_and_record."""
    entry = "Async record test"
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    result = await asyncio.to_thread(stamp_and_record, entry, dt)
    assert isinstance(result, SovereignRecord)
    assert result.entry == entry
    assert hasattr(result.stamp, 'seal')


async def test_async_verify():
    """to_thread wrapper for verify, returns valid."""
    entry = "Async verify test"
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    record = stamp_and_record(entry, dt)
    result = await asyncio.to_thread(verify, entry, record.stamp)
    assert result.valid is True
    assert result.reason == "VALID"


async def test_async_to_dict():
    """Serialize in thread."""
    entry = "Async serialize"
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    s = stamp(entry, dt)
    result = await asyncio.to_thread(to_dict, s)
    assert isinstance(result, dict)
    assert 'seal' in result
    assert 'gregorian' in result


async def test_async_from_dict():
    """Deserialize in thread."""
    entry = "Async deserialize"
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    s = stamp(entry, dt)
    d = to_dict(s)
    result = await asyncio.to_thread(from_dict, d)
    assert result.seal == s.seal
    assert result.gregorian == s.gregorian


async def test_async_display():
    """Display in thread."""
    entry = "Async display"
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    s = stamp(entry, dt)
    result = await asyncio.to_thread(display, s)
    assert isinstance(result, str)
    assert s.seal in result


async def test_async_stamp_batch():
    """Batch in thread."""
    entries = ["batch1", "batch2", "batch3"]
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    result = await asyncio.to_thread(stamp_batch, entries, dt)
    assert isinstance(result, list)
    assert len(result) == 3
    assert all(isinstance(r, SovereignRecord) for r in result)


async def test_async_concurrent_stamps_all_correct():
    """asyncio.gather() 10 concurrent stamp calls, all verify."""
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    entries = [f"concurrent_{i}" for i in range(10)]
    
    async def stamp_entry(e):
        return await asyncio.to_thread(stamp, e, dt)
    
    results = await asyncio.gather(*[stamp_entry(e) for e in entries])
    
    for i, result in enumerate(results):
        assert hasattr(result, 'seal')
        # Verify each
        v = verify(entries[i], result)
        assert v.valid is True


async def test_async_concurrent_batch_stamps():
    """5 concurrent stamp_batch() calls, all records verify."""
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    
    async def run_batch(prefix):
        entries = [f"{prefix}_{i}" for i in range(5)]
        return await asyncio.to_thread(stamp_batch, entries, dt)
    
    results = await asyncio.gather(*[run_batch(f"batch{i}") for i in range(5)])
    
    for batch in results:
        for record in batch:
            v = verify(record.entry, record.stamp)
            assert v.valid is True


async def test_async_concurrent_verify_all_valid():
    """Verify 50 records concurrently."""
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    entries = [f"verify_concurrent_{i}" for i in range(50)]
    records = [stamp_and_record(e, dt) for e in entries]
    
    async def verify_record(r):
        return await asyncio.to_thread(verify, r.entry, r.stamp)
    
    results = await asyncio.gather(*[verify_record(r) for r in records])
    
    assert all(r.valid is True for r in results)


async def test_async_concurrent_stamps_deterministic():
    """Same entry + dt in 10 concurrent calls → all seals equal."""
    entry = "deterministic_concurrent"
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    
    async def stamp_same():
        return await asyncio.to_thread(stamp, entry, dt)
    
    results = await asyncio.gather(*[stamp_same() for _ in range(10)])
    
    seals = [r.seal for r in results]
    assert len(set(seals)) == 1  # All identical


async def test_async_concurrent_different_entries_no_collision():
    """20 distinct entries stamped concurrently, all seals distinct."""
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    entries = [f"unique_{i}_entry" for i in range(20)]
    
    async def stamp_entry(e):
        return await asyncio.to_thread(stamp, e, dt)
    
    results = await asyncio.gather(*[stamp_entry(e) for e in entries])
    
    seals = [r.seal for r in results]
    assert len(set(seals)) == 20  # All unique


async def test_async_vault_write_pattern():
    """Stub: async function that stamps + stores to dict, verify dict round-trips."""
    vault = {}
    
    async def vault_write(key, entry, dt):
        record = await asyncio.to_thread(stamp_and_record, entry, dt)
        # to_dict works on SovereignStamp, so use record.stamp
        vault[key] = {
            'entry': record.entry,
            **to_dict(record.stamp)
        }
        return key
    
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    key = await vault_write("doc1", "Vault test", dt)
    
    assert key in vault
    record_dict = vault[key]
    reconstructed_stamp = from_dict(record_dict)
    v = verify(record_dict['entry'], reconstructed_stamp)
    assert v.valid is True


async def test_async_ledger_append_pattern():
    """Stub: async function that stamps + serializes to JSON string."""
    import json
    
    ledger = []
    
    async def ledger_append(entry, dt):
        record = await asyncio.to_thread(stamp_and_record, entry, dt)
        # Build dict with entry + stamp fields
        record_dict = {
            'entry': record.entry,
            **to_dict(record.stamp)
        }
        json_str = json.dumps(record_dict)
        ledger.append(json_str)
        return json_str
    
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    json_str = await ledger_append("Ledger entry", dt)
    
    assert len(ledger) == 1
    parsed = json.loads(json_str)
    assert 'seal' in parsed
    assert 'entry' in parsed


async def test_async_batch_then_serialize_pattern():
    """Stamp_batch then serialize all records to JSON."""
    import json
    
    entries = ["serialize1", "serialize2", "serialize3"]
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    
    async def process():
        records = await asyncio.to_thread(stamp_batch, entries, dt)
        json_list = []
        for r in records:
            record_dict = {
                'entry': r.entry,
                **to_dict(r.stamp)
            }
            json_list.append(json.dumps(record_dict))
        return json_list
    
    json_list = await process()
    
    assert len(json_list) == 3
    for json_str in json_list:
        parsed = json.loads(json_str)
        assert 'seal' in parsed
        assert 'entry' in parsed
        # Verify the reconstructed stamp
        reconstructed_stamp = from_dict(parsed)
        v = verify(parsed['entry'], reconstructed_stamp)
        assert v.valid is True
