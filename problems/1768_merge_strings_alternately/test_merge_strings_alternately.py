import itertools
import random
import unittest

from merge_strings_alternately import Solution, merge_alternately


def reference(word1, word2):
    """与 V1 等价的参照实现。"""
    return "".join(a + b for a, b in itertools.zip_longest(word1, word2, fillvalue=""))


class MyStr(str):
    pass


class TestMergeAlternately(unittest.TestCase):
    def test_examples(self):                                    # 基线
        self.assertEqual(merge_alternately("abc", "pqr"), "apbqcr")
        self.assertEqual(merge_alternately("ab", "pqrs"), "apbqrs")
        self.assertEqual(merge_alternately("abcd", "pq"), "apbqcd")

    def test_non_str_rejected_with_param_name(self):            # 第 1 轮
        cases = [((None, "pq"), "word1"), ((["a", "b"], "pq"), "word1"),
                 ((b"ab", "pq"), "word1"), (("ab", 123), "word2"), (("ab", ["p"]), "word2")]
        for args, name in cases:
            with self.subTest(args=args), self.assertRaisesRegex(TypeError, name):
                merge_alternately(*args)

    def test_str_subclass_returns_plain_str(self):              # 第 1 轮
        result = merge_alternately(MyStr("ab"), "pq")
        self.assertEqual(result, "apbq")
        self.assertIs(type(result), str)

    def test_empty_strings(self):                               # 第 2 轮
        self.assertEqual(merge_alternately("", "abc"), "abc")
        self.assertEqual(merge_alternately("abc", ""), "abc")
        self.assertEqual(merge_alternately("", ""), "")

    def test_code_point_semantics(self):                        # 第 3 轮
        self.assertEqual(merge_alternately("\u00e9a", "xy"), "\u00e9xay")      # 预组合 é：正常
        self.assertEqual(merge_alternately("e\u0301a", "xy"), "ex\u0301ya")    # 组合字符被拆开：文档化行为

    def test_large_input(self):                                 # 第 4 轮
        a, b = "a" * 10**6, "b" * (10**6 + 3)
        result = merge_alternately(a, b)
        self.assertEqual(len(result), 2 * 10**6 + 3)
        self.assertEqual(result[:4], "abab")
        self.assertEqual(result[-3:], "bbb")

    def test_adapter_matches(self):                             # 适配器
        self.assertEqual(Solution().mergeAlternately("ab", "pqrs"), "apbqrs")

    def test_randomized_against_reference(self):                # 整体正确性
        rng = random.Random(1768)
        for _ in range(3000):
            a = "".join(rng.choice("abc") for _ in range(rng.randint(0, 12)))
            b = "".join(rng.choice("xyz") for _ in range(rng.randint(0, 12)))
            self.assertEqual(merge_alternately(a, b), reference(a, b))


if __name__ == "__main__":
    unittest.main()