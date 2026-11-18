"""
392. Is Subsequence
https://leetcode.com/problems/is-subsequence/

Difficulty: TODO
Tags: TODO

Approach:
    TODO

Complexity:
    Time O(?)  Space O(?)
"""

def is_subsequence(s: str, t: str) -> bool:
    if not isinstance(s, str):
        raise TypeError(f"s must be a str, got {type(s).__name__}")
    if not isinstance(t, str):
        raise TypeError(f"t must be a str, got {type(t).__name__}")
    pos = 0
    for i in range(len(s)):
        pos = t.find(s[i], pos)
        if pos == -1:
            return False
        pos += 1
    return True


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return is_subsequence(s, t)


if __name__ == "__main__":
    print(is_subsequence("abc", "ahbgdc"))  # True
    print(is_subsequence("axc", "ahbgdc"))  # False
