"""
Timing benchmarks — marked @pytest.mark.slow. Excluded from CI fast pass.
These are not correctness tests — they establish a performance baseline.
"""
import pytest
import time
from datetime import datetime, timezone, date

from sovereign_trace.sovereign_trace_stamp import (
    stamp,
    stamp_and_record,
    stamp_batch,
    verify,
    to_dict,
    from_dict,
    display,
    display_ascii,
    _gregorian_to_hebrew,
    _dreamspell,
    _jd_from_gregorian,
)


@pytest.mark.slow
def test_stamp_single_call_under_10ms():
    """Single stamp() call completes under 10ms."""
    entry = "Performance test single"
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    
    start = time.perf_counter()
    stamp(entry, dt)
    elapsed = time.perf_counter() - start
    
    assert elapsed < 0.010, f"stamp() took {elapsed*1000:.2f}ms, expected < 10ms"


@pytest.mark.slow
def test_stamp_100_calls_under_1s():
    """100 stamp() calls complete under 1s."""
    entry = "Performance test 100"
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    
    start = time.perf_counter()
    for i in range(100):
        stamp(f"{entry}_{i}", dt)
    elapsed = time.perf_counter() - start
    
    assert elapsed < 1.0, f"100 stamp() calls took {elapsed:.2f}s, expected < 1s"


@pytest.mark.slow
def test_stamp_1000_calls_under_10s():
    """1000 stamp() calls complete under 10s."""
    entry = "Performance test 1000"
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    
    start = time.perf_counter()
    for i in range(1000):
        stamp(f"{entry}_{i}", dt)
    elapsed = time.perf_counter() - start
    
    assert elapsed < 10.0, f"1000 stamp() calls took {elapsed:.2f}s, expected < 10s"


@pytest.mark.slow
def test_stamp_batch_100_entries_under_1s():
    """stamp_batch() with 100 entries completes under 1s."""
    entries = [f"batch_perf_{i}" for i in range(100)]
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    
    start = time.perf_counter()
    stamp_batch(entries, dt)
    elapsed = time.perf_counter() - start
    
    assert elapsed < 1.0, f"stamp_batch(100) took {elapsed:.2f}s, expected < 1s"


@pytest.mark.slow
def test_stamp_batch_1000_entries_under_10s():
    """stamp_batch() with 1000 entries completes under 10s."""
    entries = [f"batch_perf_{i}" for i in range(1000)]
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    
    start = time.perf_counter()
    stamp_batch(entries, dt)
    elapsed = time.perf_counter() - start
    
    assert elapsed < 10.0, f"stamp_batch(1000) took {elapsed:.2f}s, expected < 10s"


@pytest.mark.slow
def test_verify_100_calls_under_500ms():
    """100 verify() calls complete under 500ms."""
    entry = "Performance verify"
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    record = stamp_and_record(entry, dt)
    
    start = time.perf_counter()
    for _ in range(100):
        verify(entry, record.stamp)
    elapsed = time.perf_counter() - start
    
    assert elapsed < 0.500, f"100 verify() calls took {elapsed*1000:.2f}ms, expected < 500ms"


@pytest.mark.slow
def test_to_dict_from_dict_1000_round_trips_under_5s():
    """1000 to_dict/from_dict round trips complete under 5s."""
    entry = "Performance roundtrip"
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    original = stamp(entry, dt)
    
    start = time.perf_counter()
    for _ in range(1000):
        d = to_dict(original)
        reconstructed = from_dict(d)
        assert reconstructed.seal == original.seal
    elapsed = time.perf_counter() - start
    
    assert elapsed < 5.0, f"1000 round trips took {elapsed:.2f}s, expected < 5s"


@pytest.mark.slow
def test_hebrew_calendar_1000_dates_under_2s():
    """1000 Hebrew calendar conversions complete under 2s."""
    # Generate valid dates as tuples (year, month, day)
    test_args = []
    for i in range(1000):
        year = 2020 + (i % 10)
        month = 1 + (i % 12)
        day = 1 + (i % 28)
        try:
            date(year, month, day)  # validate
            test_args.append((year, month, day))
        except ValueError:
            test_args.append((year, month, 1))
    
    start = time.perf_counter()
    for year, month, day in test_args:
        _gregorian_to_hebrew(year, month, day)
    elapsed = time.perf_counter() - start
    
    assert elapsed < 2.0, f"1000 Hebrew conversions took {elapsed:.2f}s, expected < 2s"


@pytest.mark.slow
def test_dreamspell_1000_dates_under_1s():
    """1000 Dreamspell conversions complete under 1s."""
    test_dates = []
    for i in range(1000):
        year = 2020 + (i % 10)
        month = 1 + (i % 12)
        day = 1 + (i % 28)
        try:
            test_dates.append(date(year, month, day))
        except ValueError:
            test_dates.append(date(year, month, 1))
    
    start = time.perf_counter()
    for d in test_dates:
        _dreamspell(d)
    elapsed = time.perf_counter() - start
    
    assert elapsed < 1.0, f"1000 Dreamspell conversions took {elapsed:.2f}s, expected < 1s"


@pytest.mark.slow
def test_jd_bridge_10000_calls_under_1s():
    """10000 Julian Day calculations complete under 1s."""
    test_dates = []
    for i in range(10000):
        year = 1600 + (i % 400)
        month = 1 + (i % 12)
        day = 1 + (i % 28)
        try:
            test_dates.append((year, month, day))
        except ValueError:
            test_dates.append((year, month, 1))
    
    start = time.perf_counter()
    for year, month, day in test_dates:
        _jd_from_gregorian(year, month, day)
    elapsed = time.perf_counter() - start
    
    assert elapsed < 1.0, f"10000 JD calculations took {elapsed:.2f}s, expected < 1s"


@pytest.mark.slow
def test_self_test_runner_under_5s():
    """Embedded self-test runner completes under 5s."""
    from sovereign_trace.sovereign_trace_stamp import _run_self_test
    
    start = time.perf_counter()
    _run_self_test(verbose=False)
    elapsed = time.perf_counter() - start
    
    assert elapsed < 5.0, f"Self-test runner took {elapsed:.2f}s, expected < 5s"


@pytest.mark.slow
def test_display_1000_calls_under_500ms():
    """1000 display() calls complete under 500ms."""
    entry = "Performance display"
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    s = stamp(entry, dt)
    
    start = time.perf_counter()
    for _ in range(1000):
        display(s)
    elapsed = time.perf_counter() - start
    
    assert elapsed < 0.500, f"1000 display() calls took {elapsed*1000:.2f}ms, expected < 500ms"


@pytest.mark.slow
def test_display_ascii_1000_calls_under_500ms():
    """1000 display_ascii() calls complete under 500ms."""
    entry = "Performance display ascii"
    dt = datetime(2026, 3, 3, 15, 0, 0, tzinfo=timezone.utc)
    s = stamp(entry, dt)
    
    start = time.perf_counter()
    for _ in range(1000):
        display_ascii(s)
    elapsed = time.perf_counter() - start
    
    assert elapsed < 0.500, f"1000 display_ascii() calls took {elapsed*1000:.2f}ms, expected < 500ms"
