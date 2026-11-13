#!/usr/bin/env python3
"""Scaffold a new problem.

Usage:
    python scripts/new.py 1 two-sum
    python scripts/new.py 206 reverse-linked-list --title "Reverse Linked List"

Creates:
    problems/0001_two_sum/two_sum.py
    problems/0001_two_sum/test_two_sum.py
"""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = Path(__file__).resolve().parent / "templates"


def main() -> int:
    p = argparse.ArgumentParser(description="Create a new LeetCode problem skeleton.")
    p.add_argument("id", type=int, help="problem number, e.g. 1")
    p.add_argument("slug", help="LeetCode URL slug, e.g. two-sum")
    p.add_argument("--title", help="problem title (default: derived from slug)")
    a = p.parse_args()

    slug = a.slug.strip().lower()
    module = slug.replace("-", "_")
    if not module.isidentifier():  # e.g. "3sum" -> "p3sum", must be importable
        module = f"p{module}"
    title = a.title or slug.replace("-", " ").title()
    folder = ROOT / "problems" / f"{a.id:04d}_{module}"

    if folder.exists():
        print(f"already exists: {folder.relative_to(ROOT)}", file=sys.stderr)
        return 1
    folder.mkdir(parents=True)

    ctx = {"id": a.id, "slug": slug, "title": title, "module": module}
    files = {
        folder / f"{module}.py": "solution.py.tpl",
        folder / f"test_{module}.py": "test.py.tpl",
    }
    for dest, tpl in files.items():
        dest.write_text((TEMPLATES / tpl).read_text(encoding="utf-8").format(**ctx), encoding="utf-8")
        print(f"created {dest.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
