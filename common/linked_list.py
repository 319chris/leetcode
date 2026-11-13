from __future__ import annotations

from typing import Iterable, List, Optional


class ListNode:
    """Singly-linked list node, same shape as LeetCode's definition."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({list_to_array(self)})"


def build_list(values: Iterable[int]) -> Optional[ListNode]:
    """[1, 2, 3] -> 1 -> 2 -> 3"""
    dummy = tail = ListNode()
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def list_to_array(head: Optional[ListNode]) -> List[int]:
    """1 -> 2 -> 3 -> [1, 2, 3]"""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out
