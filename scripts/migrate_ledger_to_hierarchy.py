#!/usr/bin/env python3
"""
STP Ledger Migration Script – Flat to Hierarchical

Run this script ONCE before deploying the new auto-seal workflow.
It reorganises existing ledger JSON files from:
    ledger/<file>.json
to:
    ledger/<template_type>/<YYYY>/<MM>/<file>.json

Options:
    --dry-run   Print actions without moving files.
"""

import os
import json
import shutil
import datetime
import argparse
from pathlib import Path

LEDGER_ROOT = Path("ledger")
TARGET_ROOT = Path("ledger")

def parse_gregorian(date_str):
    """Convert 'Month DD, YYYY' to (year, month) or (None, None)."""
    try:
        dt = datetime.datetime.strptime(date_str, "%B %d, %Y")
        return dt.year, f"{dt.month:02d}"
    except ValueError:
        return None, None

def migrate(dry_run=False):
    if not LEDGER_ROOT.exists():
        print("No ledger directory found. Nothing to migrate.")
        return

    # Find all JSON files that are direct children of ledger/ (depth 1)
    flat_files = [f for f in LEDGER_ROOT.glob("*.json") if f.is_file()]

    if not flat_files:
        print("No flat JSON files found. Nothing to migrate.")
        return

    moved = 0
    skipped = 0
    for filepath in flat_files:
        # Check if file is already in a subdirectory (should not be, but safety)
        if filepath.parent != LEDGER_ROOT:
            print(f"⚠️ Skipping {filepath}: already in subdirectory?")
            skipped += 1
            continue

        # Parse JSON
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"⚠️ Skipping {filepath.name}: cannot read JSON ({e})")
            skipped += 1
            continue

        ttype = data.get("template_type", "unknown")
        if not ttype:
            ttype = "unknown"
            print(f"⚠️ {filepath.name}: template_type missing, using 'unknown'")

        seal = data.get("seal", {})
        greg_str = seal.get("gregorian", "")
        if greg_str:
            year, month = parse_gregorian(greg_str)
        else:
            year, month = None, None

        # Build target directory
        target_dir = TARGET_ROOT / ttype
        if year and month:
            target_dir = target_dir / str(year) / str(month)
        else:
            target_dir = target_dir / "unknown"
            print(f"⚠️ {filepath.name}: date missing/unparsable, moving to 'unknown'")

        target_path = target_dir / filepath.name

        # Check if target already exists
        if target_path.exists():
            print(f"⚠️ Target already exists: {target_path}. Skipping {filepath.name}")
            skipped += 1
            continue

        if dry_run:
            print(f"[DRY RUN] Would move {filepath.name} -> {target_path}")
            moved += 1
            continue

        # Actually move
        target_dir.mkdir(parents=True, exist_ok=True)
        # Copy then delete (safer than move in case of interruption)
        shutil.copy2(filepath, target_path)
        try:
            os.unlink(filepath)
        except OSError:
            # If deletion fails, leave copy and report error
            print(f"❌ Failed to delete original {filepath.name} after copy. Manual cleanup needed.")
            skipped += 1
            continue

        print(f"✓ Moved {filepath.name} -> {target_path}")
        moved += 1

    print(f"\nMigration complete. Moved: {moved}, Skipped: {skipped}")
    if dry_run:
        print("(Dry run – no files were actually moved.)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Migrate STP ledger from flat to hierarchical structure.")
    parser.add_argument("--dry-run", action="store_true", help="Preview actions without moving files.")
    args = parser.parse_args()
    migrate(dry_run=args.dry_run)
