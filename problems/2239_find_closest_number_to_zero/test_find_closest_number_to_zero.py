import random
import unittest

import numpy as np

from find_closest_number_to_zero import closest_to_zero


def v1(nums):
    min_dist = min(abs(x) for x in nums)
    return max(x for x in nums if abs(x) == min_dist)


class TestClosestToZero(unittest.TestCase):
    def test_examples(self):                                   # 基线
        self.assertEqual(closest_to_zero([-4, -2, 1, 4, 8]), 1)
        self.assertEqual(closest_to_zero([2, -1, 1]), 1)

    def test_tie_is_order_independent(self):                   # 平局规则
        self.assertEqual(closest_to_zero([1, -1]), 1)
        self.assertEqual(closest_to_zero([-1, 1]), 1)

    def test_simple_boundaries(self):                          # 最小规模与特殊值
        self.assertEqual(closest_to_zero([-7]), -7)
        self.assertEqual(closest_to_zero([-5, -3]), -3)
        self.assertEqual(closest_to_zero([3, 0, -3]), 0)
        self.assertEqual(closest_to_zero([-10**30, 10**30]), 10**30)

    def test_empty(self):                                      # 第 1、3 轮
        for empty in ([], (), set(), (x for x in [])):
            with self.subTest(empty=type(empty).__name__), self.assertRaises(ValueError):
                closest_to_zero(empty)

    def test_bad_elements(self):                               # 第 2 轮
        for bad in ([True, -1], [False, 3], [0.5, 1], [float("nan"), 1], [1, float("nan")],
                    ["a"], [None, 1]):
            with self.subTest(bad=bad), self.assertRaises(TypeError):
                closest_to_zero(bad)

    def test_bad_containers(self):                             # 第 3 轮
        for bad in (None, "12", b"12", {0: 5, 1: 9}, 42):
            with self.subTest(bad=bad), self.assertRaises(TypeError):
                closest_to_zero(bad)

    def test_other_iterables(self):                            # 第 3 轮
        data = [2, -1, 1]
        for src in ((x for x in data), tuple(data), set(data), np.array(data)):
            with self.subTest(src=type(src).__name__):
                result = closest_to_zero(src)
                self.assertEqual(result, 1)
                self.assertIs(type(result), int)

    def test_validation_is_complete(self):                     # 第 4 轮
        with self.assertRaises(TypeError):
            closest_to_zero([0, "a"])

    def test_randomized_against_v1(self):                      # 整体正确性
        rng = random.Random(2239)
        for _ in range(3000):
            nums = [rng.randint(-20, 20) for _ in range(rng.randint(1, 30))]
            self.assertEqual(closest_to_zero(nums), v1(nums))
            self.assertEqual(closest_to_zero(reversed(nums)), v1(nums))


if __name__ == "__main__":
    unittest.main()
