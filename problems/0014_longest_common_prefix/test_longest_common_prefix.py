import random
import time
import unittest

from longest_common_prefix import Solution, longest_common_prefix


def brute_force(strs):
    """V1：从最长的候选前缀开始尝试。"""
    first = strs[0]
    for length in range(len(first), -1, -1):
        prefix = first[:length]
        if all(s.startswith(prefix) for s in strs):
            return prefix
    return ""


def vertical_scan(strs):
    """V2：逐列比较。"""
    first = strs[0]
    for i in range(len(first)):
        for s in strs[1:]:
            if i >= len(s) or s[i] != first[i]:
                return first[:i]
    return first


class TestLongestCommonPrefix(unittest.TestCase):
    def test_examples(self):                                    # 基线
        self.assertEqual(longest_common_prefix(["flower", "flow", "flight"]), "fl")
        self.assertEqual(longest_common_prefix(["dog", "racecar", "car"]), "")

    def test_boundaries(self):                                  # 边界
        self.assertEqual(longest_common_prefix(["alone"]), "alone")
        self.assertEqual(longest_common_prefix(["", "abc"]), "")
        self.assertEqual(longest_common_prefix(["", ""]), "")
        self.assertEqual(longest_common_prefix(["ab", "a"]), "a")
        self.assertEqual(longest_common_prefix(["same", "same"]), "same")

    def test_empty_list(self):                                  # 第 1 轮
        with self.assertRaisesRegex(ValueError, "empty"):
            longest_common_prefix([])

    def test_bad_containers(self):                              # 第 2 轮
        for bad in (None, "flower", ("flower", "flow"), (x for x in ["ab", "ac"])):
            with self.subTest(bad=bad), self.assertRaisesRegex(TypeError, "^strs must be a list"):
                longest_common_prefix(bad)  # type: ignore[arg-type]  # intentionally wrong type

    def test_bad_elements(self):                                # 第 3 轮
        for bad, index in ((["ab", None], 1), (["ab", 3], 1), (["ab", b"ab"], 1),
                           (["ab", ["a", "b"]], 1), ([["a", "b"], "ab"], 0)):
            with self.subTest(bad=bad), self.assertRaisesRegex(TypeError, rf"strs\[{index}\]"):
                longest_common_prefix(bad)

    def test_code_point_semantics(self):                        # 第 4 轮
        self.assertEqual(longest_common_prefix(["e\u0301x", "e\u0300y"]), "e")
        self.assertEqual(longest_common_prefix(["Flow", "flow"]), "")

    def test_many_long_strings_fast(self):                      # 第 5 轮
        strs = ["a" * 10**4 for _ in range(1000)]
        start = time.perf_counter()
        self.assertEqual(longest_common_prefix(strs), "a" * 10**4)
        self.assertLess(time.perf_counter() - start, 0.2)        # 宽松上限，实测约 2 ms

    def test_input_not_mutated(self):                           # 输入安全
        strs = ["flower", "flow", "flight"]
        longest_common_prefix(strs)
        self.assertEqual(strs, ["flower", "flow", "flight"])

    def test_randomized_against_v1_and_v2(self):                # 整体正确性
        rng = random.Random(14)
        for _ in range(5000):
            strs = ["".join(rng.choice("ab") for _ in range(rng.randint(0, 6)))
                    for _ in range(rng.randint(1, 5))]
            expected = brute_force(strs)
            self.assertEqual(vertical_scan(strs), expected)
            self.assertEqual(longest_common_prefix(strs), expected)

    def test_adapter(self):                                     # 适配器
        self.assertEqual(Solution().longestCommonPrefix(["flower", "flow", "flight"]), "fl")


if __name__ == "__main__":
    unittest.main()