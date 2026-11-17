import itertools
import unittest

from roman_to_integer import Solution, romanToInt as roman_to_int


def int_to_roman(n):
    """测试用的参照实现：把 1~3999 转成标准罗马数字。"""
    table = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
             (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    parts = []
    for value, symbol in table:
        count, n = divmod(n, value)
        parts.append(symbol * count)
    return "".join(parts)


CANONICAL = {int_to_roman(n): n for n in range(1, 4000)}


class TestRomanToInt(unittest.TestCase):
    def test_examples(self):                                   # 基线
        self.assertEqual(roman_to_int("III"), 3)
        self.assertEqual(roman_to_int("LVIII"), 58)
        self.assertEqual(roman_to_int("MCMXCIV"), 1994)

    def test_all_canonical_numerals(self):                     # 全量：1~3999
        for text, n in CANONICAL.items():
            self.assertEqual(roman_to_int(text), n)

    def test_type_errors(self):                                # 第 1 轮
        for bad in (None, ["X", "I", "V"], b"XIV", 14):
            with self.subTest(bad=bad), self.assertRaises(TypeError):
                roman_to_int(bad)  # type: ignore[arg-type]  # intentionally wrong type

    def test_invalid_characters(self):                         # 第 2 轮
        for bad in ("XIZ", "xiv", " XIV", "\u216b"):
            with self.subTest(bad=bad), self.assertRaisesRegex(ValueError, "invalid character"):
                roman_to_int(bad)

    def test_non_canonical(self):                              # 第 3 轮
        for bad in ("IIII", "IC", "VX", "IIV", "MMMM", "IM", "XXC", "LL"):
            with self.subTest(bad=bad), self.assertRaisesRegex(ValueError, "not a valid"):
                roman_to_int(bad)

    def test_empty(self):                                      # 第 4 轮
        with self.assertRaisesRegex(ValueError, "empty"):
            roman_to_int("")

    def test_long_input(self):                                 # 第 5 轮
        with self.assertRaisesRegex(ValueError, "too long") as ctx:
            roman_to_int("M" * 10**6)
        self.assertLess(len(str(ctx.exception)), 100)
        self.assertEqual(roman_to_int("MMMDCCCLXXXVIII"), 3888)   # 恰好 15 个字符

    def test_exhaustive_short_strings(self):                   # 结构校验的完整性
        for length in range(1, 5):
            for chars in itertools.product("IVXLCDM", repeat=length):
                text = "".join(chars)
                if text in CANONICAL:
                    self.assertEqual(roman_to_int(text), CANONICAL[text])
                else:
                    with self.assertRaises(ValueError):
                        roman_to_int(text)

    def test_adapter(self):                                    # 适配器
        self.assertEqual(Solution().romanToInt("MCMXCIV"), 1994)


if __name__ == "__main__":
    unittest.main()