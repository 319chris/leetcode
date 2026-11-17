# LeetCode (Python)

A personal collection of LeetCode solutions in Python.

Each problem lives in its own folder with two files:

- a **standalone solution script** you can run directly, and
- a **unit test** that checks the solution.

The goal is to cover as many LeetCode problems as possible, with every solution tested and runnable on its own.

## Project layout

```
problems/
  0013_roman_to_integer/
    roman_to_integer.py         # solution (run it directly)
    test_roman_to_integer.py    # tests
  ...
common/                         # shared helpers: ListNode, TreeNode, build_list, build_tree
scripts/new.py                  # creates a new problem folder from templates
scripts/templates/              # templates for new solution and test files
```

## Setup

Requires Python 3.9+.

```bash
pip install -r requirements.txt
```

## Usage

### 1. Create a new problem

Paste the problem number and title from LeetCode:

```bash
python3 scripts/new.py 13. Roman to Integer
```

This creates `problems/0013_roman_to_integer/` with a solution file and a test file.

### 2. Write the solution and tests

- Write your code in the solution file. Keep LeetCode's `class Solution` method so the code can be submitted as-is.
- Add test cases to the test file.

### 3. Run

```bash
# Run one solution
python3 problems/0013_roman_to_integer/roman_to_integer.py

# Run one problem's tests
python3 -m pytest problems/0013_roman_to_integer

# Run all tests
python3 -m pytest
```

## Linked lists and binary trees

For linked list or tree problems, add these lines at the top of the solution file to use the shared helpers:

```python
import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from common import ListNode, TreeNode, build_list, build_tree
```
