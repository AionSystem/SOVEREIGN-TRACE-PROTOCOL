#!/usr/bin/env python3
"""
STP Ledger Migration Script – Flat to Hierarchical

Run this script ONCE before deploying the new auto-seal workflow.
It reorganises existing ledger JSON files from:
    ledger/<file>.json
to:
    ledger/<template_type>/<YYYY>/<MM>/<file>.json

The script does not delete any files; it moves them.
It also prints a summary of what was moved.
"""

import os
import json
import shutil
import datetime
from pathlib import Path

LEDGER_ROOT = Path("ledger")
TARGET_ROOT = Path("ledger")   # same root, new subfolders

def parse_gregorian(date_str):
    """Convert 'Month DD, YYYY' to (year, month)."""
    try:
        dt = datetime.datetime.strptime(date_str, "%B %d, %Y")
        return dt.year, f"{dt.month:02d}"
    except ValueError:
        return None, None

def migrate():
    if not LEDGER_ROOT.exists():
        print("No ledger directory found. Nothing to migrate.")
        return

    # Find all JSON files directly under ledger/ (not already in subdirs)
    # We'll consider any file that is a direct child of ledger/ and ends with .json
    # as a flat file to migrate. We'll skip any file already in a subdirectory.
    flat_files = [f for f in LEDGER_ROOT.glob("*.json") if f.is_file()]

    if not flat_files:
        print("No flat JSON files found. Nothing to migrate.")
        return

    moved = 0
    skipped = 0
    for filepath in flat_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"⚠️ Skipping {filepath.name}: cannot read JSON ({e})")
            skipped += 1
            continue

        # Extract template_type
        ttype = data.get("template_type", "unknown")
        if not ttype or ttype == "unknown":
            print(f"⚠️ {filepath.name}: template_type missing or unknown, using 'unknown'")
            ttype = "unknown"

        # Extract Gregorian date from seal block
        seal = data.get("seal", {})
        greg_str = seal.get("gregorian", "")
        if not greg_str:
            print(f"⚠️ {filepath.name}: no gregorian date in seal, using 'unknown' folder")
            year, month = None, None
        else:
            year, month = parse_gregorian(greg_str)
            if year is None:
                print(f"⚠️ {filepath.name}: could not parse date '{greg_str}', using 'unknown' folder")
                year, month = None, None

        # Build target path
        target_dir = TARGET_ROOT / ttype
        if year and month:
            target_dir = target_dir / str(year) / str(month)
        else:
            target_dir = target_dir / "unknown"

        target_dir.mkdir(parents=True, exist_ok=True)
        target_path = target_dir / filepath.name

        # Move file
        shutil.move(str(filepath), str(target_path))
        print(f"✓ Moved {filepath.name} -> {target_path}")
        moved += 1

    print(f"\nMigration complete. Moved: {moved}, Skipped: {skipped}")

if __name__ == "__main__":
    migrate()
