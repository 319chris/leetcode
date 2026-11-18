import itertools
import random
import time
import unittest

from is_subsequence import Solution, is_subsequence


def brute_force(s, t):
    """V1：枚举 t 中所有长度为 len(s) 的位置组合。"""
    return any(all(t[p] == ch for p, ch in zip(pos, s))
               for pos in itertools.combinations(range(len(t)), len(s)))


def two_pointers(s, t):
    """V2：逐字符双指针。"""
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


class TestIsSubsequence(unittest.TestCase):
    def test_examples(self):                                   # 基线
        self.assertTrue(is_subsequence("abc", "ahbgdc"))
        self.assertFalse(is_subsequence("axc", "ahbgdc"))

    def test_empty_and_repeated(self):                         # 边界
        self.assertTrue(is_subsequence("", ""))
        self.assertTrue(is_subsequence("", "abc"))
        self.assertFalse(is_subsequence("a", ""))
        self.assertTrue(is_subsequence("aa", "aba"))
        self.assertFalse(is_subsequence("aaa", "aa"))
        self.assertFalse(is_subsequence("ba", "ab"))           # 顺序不能颠倒

    def test_type_errors(self):                                # 第 1 轮
        cases = [((None, "abc"), "s"), ((["a", "b"], "ab"), "s"), ((b"ab", b"xab"), "s"),
                 (("ab", ["a", "x", "b"]), "t"), (("a", 5), "t"), (("ab", b"ab"), "t")]
        for args, name in cases:
            with self.subTest(args=args), self.assertRaisesRegex(TypeError, f"^{name} must"):
                is_subsequence(*args)

    def test_exact_code_point_semantics(self):                 # 第 2 轮
        self.assertFalse(is_subsequence("A", "abc"))
        self.assertFalse(is_subsequence("e\u0301", "\u00e9"))
        self.assertTrue(is_subsequence("e", "e\u0301"))
        self.assertTrue(is_subsequence("你好", "你们好"))

    def test_large_input_is_fast(self):                        # 第 3 轮
        t = "a" * 10**7 + "b"
        start = time.perf_counter()
        self.assertTrue(is_subsequence("ab", t))
        self.assertFalse(is_subsequence("c", t))
        self.assertLess(time.perf_counter() - start, 0.5)      # 宽松的上限，避免机器差异导致误报

    def test_against_brute_force(self):                        # 整体正确性（小规模）
        rng = random.Random(392)
        for _ in range(3000):
            t = "".join(rng.choice("ab") for _ in range(rng.randint(0, 10)))
            s = "".join(rng.choice("ab") for _ in range(rng.randint(0, 5)))
            self.assertEqual(is_subsequence(s, t), brute_force(s, t))

    def test_against_two_pointers(self):                       # 第 3 轮：改写前后行为一致
        rng = random.Random(3920)
        for _ in range(3000):
            t = "".join(rng.choice("abc") for _ in range(rng.randint(0, 200)))
            s = "".join(rng.choice("abc") for _ in range(rng.randint(0, 20)))
            self.assertEqual(is_subsequence(s, t), two_pointers(s, t))

    def test_adapter(self):                                    # 适配器
        self.assertTrue(Solution().isSubsequence("abc", "ahbgdc"))


if __name__ == "__main__":
    unittest.main()