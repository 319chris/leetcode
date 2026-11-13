"""
1. Two Sum
https://leetcode.com/problems/two-sum/

Difficulty: Easy
Tags: Array, Hash Table

思路:
    一次遍历，用哈希表记录 值 -> 下标。对每个 num，先查 target - num 是否出现过。

复杂度:
    时间 O(n)  空间 O(n)
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))  # [0, 1]
