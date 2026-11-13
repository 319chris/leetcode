"""
{id}. {title}
https://leetcode.com/problems/{slug}/

Difficulty: TODO
Tags: TODO

Approach:
    TODO

Complexity:
    Time O(?)  Space O(?)
"""
import sys
from pathlib import Path
from typing import List, Optional

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # repo root, for `common`
from common import ListNode, TreeNode, build_list, build_tree  # noqa: E402,F401


class Solution:
    def solve(self):
        raise NotImplementedError


if __name__ == "__main__":
    print(Solution().solve())
