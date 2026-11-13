from __future__ import annotations

from collections import deque
from typing import List, Optional, Sequence


class TreeNode:
    """Binary tree node, same shape as LeetCode's definition."""

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({tree_to_array(self)})"


def build_tree(values: Sequence[Optional[int]]) -> Optional[TreeNode]:
    """Build a tree from LeetCode's level-order format, e.g. [3, 9, 20, None, None, 15, 7]."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to_array(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Serialize a tree to LeetCode's level-order format (trailing Nones trimmed)."""
    if not root:
        return []
    out: List[Optional[int]] = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out
