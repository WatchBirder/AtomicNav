#!/usr/bin/env python3
"""Print a compact report for the curated AtomicNav development table."""

from __future__ import annotations

import csv
import sys
from pathlib import Path


def main() -> int:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "results/ablation_dev100.csv")
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise SystemExit("No result rows found")
    print(f"{path}: {len(rows)} completed variants")
    print(f"{'variant':<24} {'SR':>7} {'SPL':>7} {'OSR':>7} {'NE (m)':>8}")
    print("-" * 58)
    for row in rows:
        print(
            f"{row['variant']:<24} {float(row['sr_percent']):6.2f}% "
            f"{float(row['spl_percent']):6.2f}% "
            f"{float(row['osr_percent']):6.2f}% "
            f"{float(row['ne_m']):8.4f}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
