import unittest

from my_tetris import evaluate


class Test(unittest.TestCase):

    def test_1x1(self):

        self.assertEqual(evaluate([
            ".",
        ]), ([
            ".",
        ], 0))

        self.assertEqual(evaluate([
            "*",
        ]), ([
            ".",
        ], 1))


    def test_2x2(self):

        self.assertEqual(evaluate([
            "..",
            "..",
        ]), ([
            "..",
            "..",
        ], 0))

        self.assertEqual(evaluate([
            ".*",
            "*.",
        ]), ([
            ".*",
            "*.",
        ], 0))

        self.assertEqual(evaluate([
            ".*",
            "**",
        ]), ([
            "..",
            ".*",
        ], 1))


if __name__ == "__main__":
    unittest.main()