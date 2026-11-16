"""
1768. Merge Strings Alternately
https://leetcode.com/problems/merge-strings-alternately/

Difficulty: TODO
Tags: TODO

Approach:
    TODO

Complexity:
    Time O(?)  Space O(?)
"""
def merge_alternately(word1: str, word2: str) -> str:
    if not isinstance(word1, str):
        raise TypeError(f"word1 must be a str, got {type(word1).__name__}")
    if not isinstance(word2, str):
        raise TypeError(f"word2 must be a str, got {type(word2).__name__}")


    result = []
    n = len(word1)
    m = len(word2)
    Min = min(n,m)
    for i in range(Min):
        result.append(word1[i])
        result.append(word2[i])
    if n < m:
        result.append(word2[Min:])
    else:
        result.append(word1[Min:])
    return "".join(result)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return merge_alternately(word1, word2)