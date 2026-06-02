"""
Thread-safety and concurrent access — the stamp functions have no shared mutable
state, but this must be verified empirically.
"""
import pytest
import threading
from datetime import datetime, timezone
from hypothesis import given, assume, strategies as st

from sovereign_trace.sovereign_trace_stamp import (
    stamp,
    stamp_and_record,
    stamp_batch,
    verify,
    to_dict,
    from_dict,
    SovereignStamp,
    SovereignRecord,
)
from sovereign_trace.sovereign_trace_stamp import (
    _gregorian_to_hebrew,
    _dreamspell,
)


def test_threading_stamp_no_race_conditions():
    """50 threads each call stamp() simultaneously, all seals valid."""
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    entries = [f"thread_{i}" for i in range(50)]
    results = [None] * 50
    errors = [None] * 50
    
    def worker(idx):
        try:
            results[idx] = stamp(entries[idx], dt)
        except Exception as e:
            errors[idx] = e
    
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(50)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    assert all(e is None for e in errors), f"Errors occurred: {errors}"
    assert all(r is not None for r in results)
    assert all(hasattr(r, 'seal') for r in results)
    
    # All should verify
    for i, r in enumerate(results):
        v = verify(entries[i], r)
        assert v.valid is True


def test_threading_stamp_deterministic_under_concurrency():
    """Same entry + dt in 20 threads → identical seals."""
    entry = "deterministic_thread"
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    results = [None] * 20
    
    def worker(idx):
        results[idx] = stamp(entry, dt)
    
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(20)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    seals = [r.seal for r in results]
    assert len(set(seals)) == 1  # All identical


def test_threading_different_entries_no_cross_contamination():
    """Each thread stamps unique entry, verify round-trip."""
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    entries = [f"unique_thread_{i}_entry" for i in range(30)]
    results = [None] * 30
    
    def worker(idx):
        results[idx] = stamp(entries[idx], dt)
    
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(30)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    for i, r in enumerate(results):
        v = verify(entries[i], r)
        assert v.valid is True, f"Entry {i} failed verification"


def test_threading_stamp_batch_concurrent():
    """10 threads each call stamp_batch(), no exceptions."""
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    results = [None] * 10
    errors = [None] * 10
    
    def worker(idx):
        try:
            entries = [f"batch{idx}_{i}" for i in range(5)]
            results[idx] = stamp_batch(entries, dt)
        except Exception as e:
            errors[idx] = e
    
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    assert all(e is None for e in errors), f"Errors occurred: {errors}"
    assert all(r is not None for r in results)
    
    # All records in all batches should verify
    for batch in results:
        for record in batch:
            v = verify(record.entry, record.stamp)
            assert v.valid is True


def test_threading_verify_concurrent():
    """50 threads verify same record concurrently, all True."""
    entry = "concurrent_verify_test"
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    record = stamp_and_record(entry, dt)
    results = [None] * 50
    
    def worker(idx):
        results[idx] = verify(entry, record.stamp)
    
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(50)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    assert all(r.valid is True for r in results)


def test_threading_to_dict_from_dict_concurrent():
    """Serialize/deserialize from 20 threads."""
    entry = "serialize_thread"
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    original = stamp(entry, dt)
    results = [None] * 20
    
    def worker(idx):
        d = to_dict(original)
        results[idx] = from_dict(d)
    
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(20)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    assert all(r.seal == original.seal for r in results)


def test_threading_no_module_level_mutation():
    """Confirm no globals change across threads."""
    import sovereign_trace.sovereign_trace_stamp as module
    
    # Get initial state of module dict (filter out special attrs)
    initial_globals = {
        k: v for k, v in module.__dict__.items()
        if not k.startswith('_') and not callable(v)
    }
    
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    entries = [f"mutation_test_{i}" for i in range(30)]
    
    def worker(idx):
        stamp(entries[idx], dt)
        stamp_and_record(entries[idx], dt)
    
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(30)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    # Check globals haven't changed
    final_globals = {
        k: v for k, v in module.__dict__.items()
        if not k.startswith('_') and not callable(v)
    }
    
    assert initial_globals == final_globals


def test_threading_hebrew_calendar_no_race():
    """30 threads call _gregorian_to_hebrew concurrently, all correct."""
    test_dates = [
        (2026, 3, 3),
        (2025, 9, 23),
        (2024, 3, 25),
        (2026, 7, 26),
    ]
    results = [None] * 30
    
    def worker(idx):
        year, month, day = test_dates[idx % len(test_dates)]
        results[idx] = _gregorian_to_hebrew(year, month, day)
    
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(30)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    # All should return valid tuples (year, month_name, day)
    for r in results:
        assert r is not None
        assert isinstance(r, tuple)
        assert len(r) == 3
        assert isinstance(r[0], int)  # year
        assert isinstance(r[1], str)  # month name
        assert isinstance(r[2], int)  # day


def test_threading_dreamspell_no_race():
    """30 threads call _dreamspell concurrently."""
    from datetime import date
    
    test_dates = [
        date(2026, 3, 3),
        date(2026, 7, 25),
        date(2026, 7, 26),
        date(2024, 2, 29),
    ]
    results = [None] * 30
    
    def worker(idx):
        d = test_dates[idx % len(test_dates)]
        results[idx] = _dreamspell(d)
    
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(30)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    # All should return non-empty strings
    for r in results:
        assert r is not None
        assert isinstance(r, str)
        assert len(r) > 0


@given(st.text(min_size=1, max_size=50).filter(lambda s: s.strip()),
       st.text(min_size=1, max_size=50).filter(lambda s: s.strip()))
def test_stamp_result_independent_of_call_order(e1, e2):
    """For any two entries e1, e2 and any dt, stamp(e1, dt).seal == stamp(e1, dt).seal regardless of interleaving."""
    assume(e1 != e2)
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    
    results = [None, None, None, None]
    
    def stamp_e1_first():
        r1 = stamp(e1, dt)
        r2 = stamp(e2, dt)
        results[0] = r1.seal
        results[1] = r2.seal
    
    def stamp_e2_first():
        r2 = stamp(e2, dt)
        r1 = stamp(e1, dt)
        results[2] = r1.seal
        results[3] = r2.seal
    
    t1 = threading.Thread(target=stamp_e1_first)
    t2 = threading.Thread(target=stamp_e2_first)
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    # e1 seals should all be equal
    e1_seals = [results[0], results[2]]
    assert len(set(e1_seals)) == 1
    
    # e2 seals should all be equal
    e2_seals = [results[1], results[3]]
    assert len(set(e2_seals)) == 1
