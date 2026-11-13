import unittest

from {module} import Solution


class TestSolution(unittest.TestCase):
    def test_examples(self):
        cases = [
            # ((arg1, arg2, ...), expected),
        ]
        if not cases:
            self.skipTest("no test cases yet")
        for args, expected in cases:
            with self.subTest(args=args):
                self.assertEqual(Solution().solve(*args), expected)


if __name__ == "__main__":
    unittest.main()
