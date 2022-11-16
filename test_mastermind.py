import unittest

import mastermind as mm

from enum import Enum


class Color(Enum):
    red = 1
    green = 2
    blue = 3
    black = 4


class Test(unittest.TestCase):

    def test_types(self):
        self.assertEqual(mm.evaluate([1], [1]), (1, 0))
        self.assertEqual(mm.evaluate([1, 2], [2, 1]), (0, 2))
        self.assertEqual(mm.evaluate(["red"], ["red"]), (1, 0))
        self.assertEqual(mm.evaluate(["red", "blue"], ["blue", "red"]), (0, 2))
        self.assertEqual(mm.evaluate([Color.red], [Color.red]), (1, 0))
        self.assertEqual(mm.evaluate([Color.red, Color.blue], [Color.blue, Color.red]), (0, 2))

    def test1(self):
        self.assertEqual(mm.evaluate([1], [1]), (1, 0))
        self.assertEqual(mm.evaluate([1], [2]), (0, 0))

    def test2(self):
        self.assertEqual(mm.evaluate([1, 2], [1, 2]), (2, 0))
        self.assertEqual(mm.evaluate([1, 2], [1, 3]), (1, 0))
        self.assertEqual(mm.evaluate([1, 2], [3, 1]), (0, 1))
        self.assertEqual(mm.evaluate([1, 2], [2, 1]), (0, 2))

    def test3(self):
        self.assertEqual(mm.evaluate([1, 2, 3], [1, 2, 3]), (3, 0))
        self.assertEqual(mm.evaluate([1, 2, 3], [1, 4, 3]), (2, 0))
        self.assertEqual(mm.evaluate([1, 2, 3], [5, 4, 3]), (1, 0))
        self.assertEqual(mm.evaluate([1, 2, 3], [2, 4, 3]), (1, 1))
        self.assertEqual(mm.evaluate([1, 2, 3], [2, 1, 3]), (1, 2))
        self.assertEqual(mm.evaluate([1, 2, 3], [4, 5, 6]), (0, 0))
        self.assertEqual(mm.evaluate([1, 2, 3], [4, 1, 6]), (0, 1))
        self.assertEqual(mm.evaluate([1, 2, 3], [2, 1, 6]), (0, 2))
        self.assertEqual(mm.evaluate([1, 2, 3], [3, 1, 2]), (0, 3))

    def test4(self):
        self.assertEqual(mm.evaluate([1, 2, 3, 4], [1, 2, 3, 4]), (4, 0))
        self.assertEqual(mm.evaluate([1, 2, 3, 4], [1, 2, 5, 4]), (3, 0))
        self.assertEqual(mm.evaluate([1, 2, 3, 4], [6, 2, 5, 4]), (2, 0))
        self.assertEqual(mm.evaluate([1, 2, 3, 4], [3, 2, 5, 4]), (2, 1))
        self.assertEqual(mm.evaluate([1, 2, 3, 4], [3, 2, 1, 4]), (2, 2))
        self.assertEqual(mm.evaluate([1, 2, 3, 4], [6, 2, 5, 7]), (1, 0))
        self.assertEqual(mm.evaluate([1, 2, 3, 4], [6, 2, 5, 3]), (1, 1))
        self.assertEqual(mm.evaluate([1, 2, 3, 4], [4, 2, 5, 3]), (1, 2))
        self.assertEqual(mm.evaluate([1, 2, 3, 4], [4, 2, 1, 3]), (1, 3))
        self.assertEqual(mm.evaluate([1, 2, 3, 4], [6, 8, 5, 7]), (0, 0))
        self.assertEqual(mm.evaluate([1, 2, 3, 4], [6, 8, 5, 1]), (0, 1))
        self.assertEqual(mm.evaluate([1, 2, 3, 4], [2, 8, 5, 1]), (0, 2))
        self.assertEqual(mm.evaluate([1, 2, 3, 4], [2, 3, 5, 1]), (0, 3))
        self.assertEqual(mm.evaluate([1, 2, 3, 4], [2, 3, 4, 1]), (0, 4))


class Test_aux(unittest.TestCase):

    def test_int(self):
        self.assertTrue(mm.all_different([1]))
        self.assertTrue(mm.all_different([1, 2]))
        self.assertTrue(mm.all_different([1, 2, 3]))
        self.assertFalse(mm.all_different([1, 1]))
        self.assertFalse(mm.all_different([1, 2, 1]))
        self.assertFalse(mm.all_different([1, 2, 3, 2]))

    def test_str(self):
        self.assertTrue(mm.all_different(["red"]))
        self.assertTrue(mm.all_different(["red", "green"]))
        self.assertTrue(mm.all_different(["red", "green", "blue"]))
        self.assertFalse(mm.all_different(["red", "red"]))
        self.assertFalse(mm.all_different(["red", "green", "red"]))
        self.assertFalse(mm.all_different(["red", "green", "blue", "green"]))

    def test_enum(self):
        self.assertTrue(mm.all_different([Color.red]))
        self.assertTrue(mm.all_different([Color.red, Color.green]))
        self.assertTrue(mm.all_different([Color.red, Color.green, Color.blue]))
        self.assertFalse(mm.all_different([Color.red, Color.red]))
        self.assertFalse(mm.all_different([Color.red, Color.green, Color.red]))
        self.assertFalse(mm.all_different([Color.red, Color.green, Color.blue, Color.green]))

if __name__ == "__main__":
    unittest.main()
