import unittest

import {module}


class TestSolution(unittest.TestCase):
    def test_examples(self):
        cases = [
            # ((arg1, arg2, ...), expected),
        ]
        if not cases:
            self.skipTest("no test cases yet")
        for args, expected in cases:
            with self.subTest(args=args):
                self.assertEqual({module}.Solution().solve(*args), expected)


if __name__ == "__main__":
    unittest.main()
