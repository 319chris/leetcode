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


def _iter_validated(nums:object) -> Iterator[int]:
    if nums is None or isinstance(nums, (str, bytes, bytearray, Mapping)):
        raise TypeError(f"nums must be an Iterable of ints, got {type(nums).__name__}")
    try:
        iterator = iter(nums)  # type: ignore[call-overload]
    except TypeError:
        raise TypeError(f"nums must be iterable, got {type(nums).__name__}") from None

    for index, value in enumerate(iterator):
        if isinstance(value, bool) or not isinstance(value, Integral):
            raise TypeError(f"nums[{index}] must be an int, got {type(value).__name__}")
        yield int(value)

def _closeness_key(x:int) -> tuple[int, int]:
    return (abs(x), -x)

def closest_to_zero(nums: Iterable[int]) ->int:
    closest = min(_iter_validated(nums), key=_closeness_key, default=None)
    if closest is None:
        raise ValueError("nums must contain at least one number")
    return closest 

class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        return closest_to_zero(nums)


if __name__ == "__main__":
    print(Solution().findClosestNumber([-4, -2, 1, 4, 8]))  # 1
    print(Solution().findClosestNumber([2, -1, 1]))  # 1


    