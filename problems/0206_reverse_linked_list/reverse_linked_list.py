"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Difficulty: Easy
Tags: Linked List, Recursion

思路:
    迭代，三指针 prev / cur / nxt，逐个把 cur.next 指回 prev。

复杂度:
    时间 O(n)  空间 O(1)
"""
import sys
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # repo root, for `common`
from common import ListNode, build_list, list_to_array  # noqa: E402


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev


if __name__ == "__main__":
    print(list_to_array(Solution().reverseList(build_list([1, 2, 3, 4, 5]))))  # [5, 4, 3, 2, 1]
