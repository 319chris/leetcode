#!/usr/bin/env python3
"""Scaffold a new problem.

Usage (any of these work — just paste the title from LeetCode):
    python3 scripts/new.py 2239.Find Closest Number to Zero
    python3 scripts/new.py "2239. Find Closest Number to Zero"
    python3 scripts/new.py 1 two-sum

Creates:
    problems/2239_find_closest_number_to_zero/find_closest_number_to_zero.py
    problems/2239_find_closest_number_to_zero/test_find_closest_number_to_zero.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = Path(__file__).resolve().parent / "templates"

USAGE = 'usage: python3 scripts/new.py <题号>.<题目名>   e.g. python3 scripts/new.py 2239.Find Closest Number to Zero'


def parse(text: str):
    """'2239.Find Closest Number to Zero' -> (2239, 'find-closest-number-to-zero', 'Find Closest Number to Zero')"""
    m = re.match(r"^\s*(\d+)\s*[.、:：-]?\s*(.+?)\s*$", text)
    if not m:
        return None
    pid, name = int(m.group(1)), m.group(2)
    if re.fullmatch(r"[a-z0-9-]+", name):  # already a slug, e.g. "two-sum"
        slug = name
        title = name.replace("-", " ").title()
    else:  # a title, e.g. "Pow(x, n)" -> "powx-n"
        title = name
        slug = re.sub(r"[^a-z0-9 -]", "", name.lower())
        slug = re.sub(r"[\s-]+", "-", slug).strip("-")
    return pid, slug, title


def main() -> int:
    parsed = parse(" ".join(sys.argv[1:]))
    if not parsed:
        print(USAGE, file=sys.stderr)
        return 1
    pid, slug, title = parsed

    module = slug.replace("-", "_")
    if not module.isidentifier():  # e.g. "3sum" -> "p3sum", must be importable
        module = f"p{module}"
    folder = ROOT / "problems" / f"{pid:04d}_{module}"

    if folder.exists():
        print(f"already exists: {folder.relative_to(ROOT)}", file=sys.stderr)
        return 1
    folder.mkdir(parents=True)

    ctx = {"id": pid, "slug": slug, "title": title, "module": module}
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
