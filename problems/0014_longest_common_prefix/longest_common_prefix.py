"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

Difficulty: TODO
Tags: TODO

Approach:
    TODO

Complexity:
    Time O(?)  Space O(?)
"""

def longest_common_prefix(strs: list[str]) -> str:
    if not isinstance(strs, list):
        raise TypeError(f"strs must be a list, got {type(strs).__name__}")

    if not strs:
        raise ValueError("strs must not be empty")

    for index, s in enumerate(strs):
        if not isinstance(s, str):
            raise TypeError(f"strs[{index}] must be a str, got {type(s).__name__}")

    smallest = min(strs)
    largest = max(strs)
    for i in range(len(smallest)):
        # largest[i] 不会越界：如果 smallest 是 largest 的前缀，循环会正常走完；
        # 否则在 smallest 结束之前一定会遇到不同的字符，提前 return
        if smallest[i] != largest[i]:
            return smallest[:i]
    return smallest


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        return longest_common_prefix(strs)


if __name__ == "__main__":
    print(longest_common_prefix(["flower", "flow", "flight"]))  # fl
    print(repr(longest_common_prefix(["dog", "racecar", "car"])))  # ''
