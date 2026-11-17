"""
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/

Difficulty: TODO
Tags: TODO

Approach:
    TODO

Complexity:
    Time O(?)  Space O(?)
"""
import re 
_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

_CANONICAL = re.compile(r"M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})")

_MAX_LENGTH = 15

def _validate_roman(s: str) -> None:

    if not isinstance(s, str):
        raise TypeError(f"s must be a str, got {type(s).__name__}")

    if not s:
        raise ValueError("s must not be empty")

    if len(s) > _MAX_LENGTH:
        raise ValueError(f"s is too long to be a Roman numeral (length {len(s)})")

    for index, ch, in enumerate(s):
        if ch not in _VALUES:
            raise ValueError(f"invalid character {ch!r} at index {index}")

    if _CANONICAL.fullmatch(s) is None:
        raise ValueError(f"{s!r} is not a valid Roman numeral")


def romanToInt(s: str) -> int:
    _validate_roman(s)
    total = 0
    for i in range(len(s)):
        value = _VALUES[s[i]]
        if i + 1 < len(s) and value < _VALUES[s[i + 1]]:
            total -= value
        else:
            total += value
    return total

class Solution:
    def romanToInt(self, s:str) -> int:
        return romanToInt(s)


if __name__ == "__main__":
    print(romanToInt("III"))  # 3
    print(romanToInt("LVIII"))  # 58
    print(romanToInt("MCMXCIV"))  # 1994
