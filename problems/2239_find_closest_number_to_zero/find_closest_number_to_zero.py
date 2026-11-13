"""
2239. Find Closest Number to Zero
https://leetcode.com/problems/find-closest-number-to-zero/

Difficulty: Easy
Tags: Array

思路:
    一次遍历，用排序键 (abs(x), -x) 取最小值：先比离 0 的距离（越小越好），
    距离相同再比数值（越大越好）。额外做了输入校验，接受任意可迭代对象。

复杂度:
    时间 O(n)  空间 O(1)
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator, Mapping
from numbers import Integral
from typing import List


def _iter_validated(nums: object) -> Iterator[int]:
    """逐个校验元素并产出 Python int。注意：这是生成器，开始迭代时才执行检查。"""
    if nums is None or isinstance(nums, (str, bytes, bytearray, Mapping)):
        raise TypeError(f"nums must be an iterable of ints, got {type(nums).__name__}")
    try:
        iterator = iter(nums)  # type: ignore[call-overload]
    except TypeError:
        raise TypeError(f"nums must be iterable, got {type(nums).__name__}") from None

    for index, value in enumerate(iterator):
        # 先检查类型再参与计算；bool 是 int 的子类，必须单独排除
        if isinstance(value, bool) or not isinstance(value, Integral):
            raise TypeError(f"nums[{index}] must be an int, got {type(value).__name__}")
        yield int(value)


def _closeness_key(x: int) -> tuple[int, int]:
    """排序键：先比离 0 的距离（越小越好），距离相同再比数值（越大越好）。"""
    return (abs(x), -x)


def closest_to_zero(nums: Iterable[int]) -> int:
    """
    返回 nums 中离 0 最近的数；距离相同时返回较大的那个。

    接受任意可迭代对象（list、tuple、set、生成器等），只遍历一次，额外空间 O(1)。
    异常：TypeError（容器或元素类型非法）、ValueError（nums 为空）。
    """
    closest = min(_iter_validated(nums), key=_closeness_key, default=None)
    if closest is None:
        raise ValueError("nums must contain at least one number")
    return closest


class Solution:
    """LeetCode 提交用的入口。"""

    def findClosestNumber(self, nums: List[int]) -> int:
        return closest_to_zero(nums)


if __name__ == "__main__":
    print(Solution().findClosestNumber([-4, -2, 1, 4, 8]))  # 1
    print(Solution().findClosestNumber([2, -1, 1]))  # 1
