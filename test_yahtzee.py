import unittest

from yahtzee import score, split_roll


class Test_split(unittest.TestCase):

    def test(self):
        self.assertEqual(split_roll([1, 2, 3, 4, 5]), ([], [1, 2, 3, 4, 5], [], [], [], []))
        self.assertEqual(split_roll([1, 1, 3, 4, 5]), ([], [3, 4, 5], [1], [], [], []))
        self.assertEqual(split_roll([1, 1, 3, 4, 4]), ([], [3], [1, 4], [], [], []))
        self.assertEqual(split_roll([1, 1, 1, 4, 5]), ([], [4, 5], [], [1], [], []))
        self.assertEqual(split_roll([1, 1, 1, 4, 4]), ([], [], [4], [1], [], []))
        self.assertEqual(split_roll([1, 1, 1, 1, 4]), ([], [4], [], [], [1], []))
        self.assertEqual(split_roll([1, 1, 1, 1, 1]), ([], [], [], [], [], [1]))


class Test(unittest.TestCase):

    def test_ones(self):
        self.assertEqual(score([2, 3, 4, 5, 6], "Ones"), 0)
        self.assertEqual(score([2, 2, 4, 5, 6], "Ones"), 0)
        self.assertEqual(score([2, 2, 4, 4, 6], "Ones"), 0)
        self.assertEqual(score([2, 2, 2, 5, 6], "Ones"), 0)
        self.assertEqual(score([2, 2, 2, 5, 5], "Ones"), 0)
        self.assertEqual(score([2, 2, 2, 2, 6], "Ones"), 0)
        self.assertEqual(score([2, 2, 2, 2, 2], "Ones"), 0)

        self.assertEqual(score([1, 2, 3, 4, 5], "Ones"), 1)
        self.assertEqual(score([1, 2, 2, 4, 5], "Ones"), 1)
        self.assertEqual(score([1, 2, 2, 4, 4], "Ones"), 1)
        self.assertEqual(score([1, 2, 2, 2, 5], "Ones"), 1)
        self.assertEqual(score([1, 2, 2, 2, 2], "Ones"), 1)

        self.assertEqual(score([1, 1, 3, 4, 5], "Ones"), 2)
        self.assertEqual(score([1, 1, 3, 3, 5], "Ones"), 2)
        self.assertEqual(score([1, 1, 1, 4, 5], "Ones"), 3)
        self.assertEqual(score([1, 1, 1, 4, 4], "Ones"), 3)
        self.assertEqual(score([1, 1, 1, 1, 5], "Ones"), 4)
        self.assertEqual(score([1, 1, 1, 1, 1], "Ones"), 5)


    def test_twos(self):
        self.assertEqual(score([1, 3, 4, 5, 6], "Twos"), 0)
        self.assertEqual(score([1, 1, 4, 5, 6], "Twos"), 0)
        self.assertEqual(score([1, 1, 4, 4, 6], "Twos"), 0)
        self.assertEqual(score([1, 1, 1, 5, 6], "Twos"), 0)
        self.assertEqual(score([1, 1, 1, 5, 5], "Twos"), 0)
        self.assertEqual(score([1, 1, 1, 1, 6], "Twos"), 0)
        self.assertEqual(score([1, 1, 1, 1, 1], "Twos"), 0)

        self.assertEqual(score([1, 2, 4, 5, 6], "Twos"), 2)
        self.assertEqual(score([1, 2, 1, 5, 6], "Twos"), 2)
        self.assertEqual(score([1, 2, 1, 5, 5], "Twos"), 2)
        self.assertEqual(score([1, 2, 1, 1, 6], "Twos"), 2)
        self.assertEqual(score([1, 2, 1, 1, 1], "Twos"), 2)

        self.assertEqual(score([2, 2, 4, 5, 6], "Twos"), 4)
        self.assertEqual(score([2, 2, 4, 4, 6], "Twos"), 4)
        self.assertEqual(score([2, 2, 2, 5, 6], "Twos"), 6)
        self.assertEqual(score([2, 2, 2, 5, 5], "Twos"), 6)
        self.assertEqual(score([2, 2, 2, 2, 6], "Twos"), 8)
        self.assertEqual(score([2, 2, 2, 2, 2], "Twos"), 10)


    def test_threes(self):
        self.assertEqual(score([1, 2, 4, 5, 6], "Threes"), 0)
        self.assertEqual(score([1, 1, 4, 5, 6], "Threes"), 0)
        self.assertEqual(score([1, 1, 4, 4, 6], "Threes"), 0)
        self.assertEqual(score([1, 1, 1, 5, 6], "Threes"), 0)
        self.assertEqual(score([1, 1, 1, 5, 5], "Threes"), 0)
        self.assertEqual(score([1, 1, 1, 1, 6], "Threes"), 0)
        self.assertEqual(score([1, 1, 1, 1, 1], "Threes"), 0)

        self.assertEqual(score([1, 2, 3, 4, 5], "Threes"), 3)
        self.assertEqual(score([1, 1, 3, 4, 5], "Threes"), 3)
        self.assertEqual(score([1, 1, 3, 4, 4], "Threes"), 3)
        self.assertEqual(score([1, 1, 3, 1, 5], "Threes"), 3)
        self.assertEqual(score([1, 1, 3, 1, 1], "Threes"), 3)

        self.assertEqual(score([1, 3, 3, 4, 5], "Threes"), 6)
        self.assertEqual(score([1, 3, 3, 4, 4], "Threes"), 6)
        self.assertEqual(score([3, 3, 3, 4, 5], "Threes"), 9)
        self.assertEqual(score([3, 3, 3, 4, 4], "Threes"), 9)
        self.assertEqual(score([3, 3, 3, 3, 5], "Threes"), 12)
        self.assertEqual(score([3, 3, 3, 3, 3], "Threes"), 15)


    def test_fours(self):
        self.assertEqual(score([1, 2, 3, 5, 6], "Fours"), 0)
        self.assertEqual(score([1, 1, 3, 5, 6], "Fours"), 0)
        self.assertEqual(score([1, 1, 3, 3, 6], "Fours"), 0)
        self.assertEqual(score([1, 1, 1, 5, 6], "Fours"), 0)
        self.assertEqual(score([1, 1, 1, 5, 5], "Fours"), 0)
        self.assertEqual(score([1, 1, 1, 1, 6], "Fours"), 0)
        self.assertEqual(score([1, 1, 1, 1, 1], "Fours"), 0)

        self.assertEqual(score([1, 2, 3, 4, 5], "Fours"), 4)
        self.assertEqual(score([1, 1, 3, 4, 5], "Fours"), 4)
        self.assertEqual(score([1, 1, 3, 4, 3], "Fours"), 4)
        self.assertEqual(score([1, 1, 1, 4, 5], "Fours"), 4)
        self.assertEqual(score([1, 1, 1, 4, 1], "Fours"), 4)

        self.assertEqual(score([1, 2, 3, 4, 4], "Fours"), 8)
        self.assertEqual(score([1, 3, 3, 4, 4], "Fours"), 8)
        self.assertEqual(score([1, 2, 4, 4, 4], "Fours"), 12)
        self.assertEqual(score([1, 1, 4, 4, 4], "Fours"), 12)
        self.assertEqual(score([1, 4, 4, 4, 4], "Fours"), 16)
        self.assertEqual(score([4, 4, 4, 4, 4], "Fours"), 20)


    def test_fives(self):
        self.assertEqual(score([1, 2, 3, 4, 6], "Fives"), 0)
        self.assertEqual(score([1, 1, 3, 4, 6], "Fives"), 0)
        self.assertEqual(score([1, 1, 3, 3, 6], "Fives"), 0)
        self.assertEqual(score([1, 1, 1, 4, 6], "Fives"), 0)
        self.assertEqual(score([1, 1, 1, 4, 4], "Fives"), 0)
        self.assertEqual(score([1, 1, 1, 1, 6], "Fives"), 0)
        self.assertEqual(score([1, 1, 1, 1, 1], "Fives"), 0)

        self.assertEqual(score([1, 2, 3, 4, 5], "Fives"), 5)
        self.assertEqual(score([1, 1, 3, 4, 5], "Fives"), 5)
        self.assertEqual(score([1, 1, 3, 3, 5], "Fives"), 5)
        self.assertEqual(score([1, 1, 1, 4, 5], "Fives"), 5)
        self.assertEqual(score([1, 1, 1, 1, 5], "Fives"), 5)

        self.assertEqual(score([1, 2, 3, 5, 5], "Fives"), 10)
        self.assertEqual(score([1, 1, 3, 5, 5], "Fives"), 10)
        self.assertEqual(score([1, 2, 5, 5, 5], "Fives"), 15)
        self.assertEqual(score([1, 1, 5, 5, 5], "Fives"), 15)
        self.assertEqual(score([1, 5, 5, 5, 5], "Fives"), 20)
        self.assertEqual(score([5, 5, 5, 5, 5], "Fives"), 25)


    def test_sixes(self):
        self.assertEqual(score([1, 2, 3, 4, 5], "Sixes"), 0)
        self.assertEqual(score([1, 1, 3, 4, 5], "Sixes"), 0)
        self.assertEqual(score([1, 1, 3, 3, 5], "Sixes"), 0)
        self.assertEqual(score([1, 1, 1, 4, 5], "Sixes"), 0)
        self.assertEqual(score([1, 1, 1, 4, 4], "Sixes"), 0)
        self.assertEqual(score([1, 1, 1, 1, 5], "Sixes"), 0)
        self.assertEqual(score([1, 1, 1, 1, 1], "Sixes"), 0)

        self.assertEqual(score([1, 2, 3, 4, 6], "Sixes"), 6)
        self.assertEqual(score([1, 1, 3, 4, 6], "Sixes"), 6)
        self.assertEqual(score([1, 1, 3, 3, 6], "Sixes"), 6)
        self.assertEqual(score([1, 1, 1, 4, 6], "Sixes"), 6)
        self.assertEqual(score([1, 1, 1, 1, 6], "Sixes"), 6)

        self.assertEqual(score([1, 2, 3, 6, 6], "Sixes"), 12)
        self.assertEqual(score([1, 1, 3, 6, 6], "Sixes"), 12)
        self.assertEqual(score([1, 2, 6, 6, 6], "Sixes"), 18)
        self.assertEqual(score([1, 1, 6, 6, 6], "Sixes"), 18)
        self.assertEqual(score([1, 6, 6, 6, 6], "Sixes"), 24)
        self.assertEqual(score([6, 6, 6, 6, 6], "Sixes"), 30)


    def test_pair(self):
        self.assertEqual(score([2, 3, 4, 5, 6], "Pair"), 0)
        self.assertEqual(score([2, 2, 4, 5, 6], "Pair"), 4)
        self.assertEqual(score([2, 2, 4, 4, 6], "Pair"), 8)
        self.assertEqual(score([2, 2, 2, 5, 6], "Pair"), 0)
        self.assertEqual(score([2, 2, 2, 5, 5], "Pair"), 10)
        self.assertEqual(score([2, 2, 2, 2, 6], "Pair"), 0)
        self.assertEqual(score([2, 2, 2, 2, 2], "Pair"), 0)


    def test_two_pairs(self):
        self.assertEqual(score([2, 3, 4, 5, 6], "Two pairs"), 0)
        self.assertEqual(score([2, 2, 4, 5, 6], "Two pairs"), 0)
        self.assertEqual(score([2, 2, 4, 4, 6], "Two pairs"), 12)
        self.assertEqual(score([2, 2, 2, 5, 6], "Two pairs"), 0)
        self.assertEqual(score([2, 2, 2, 5, 5], "Two pairs"), 0)
        self.assertEqual(score([2, 2, 2, 2, 6], "Two pairs"), 0)
        self.assertEqual(score([2, 2, 2, 2, 2], "Two pairs"), 0)


    def test_three_of_a_kind(self):
        self.assertEqual(score([2, 3, 4, 5, 6], "Three of a kind"), 0)
        self.assertEqual(score([2, 2, 4, 5, 6], "Three of a kind"), 0)
        self.assertEqual(score([2, 2, 4, 4, 6], "Three of a kind"), 0)
        self.assertEqual(score([2, 2, 2, 5, 6], "Three of a kind"), 6)
        self.assertEqual(score([2, 2, 2, 5, 5], "Three of a kind"), 6)
        self.assertEqual(score([2, 2, 2, 2, 6], "Three of a kind"), 0)
        self.assertEqual(score([2, 2, 2, 2, 2], "Three of a kind"), 0)


    def test_four_of_a_kind(self):
        self.assertEqual(score([2, 3, 4, 5, 6], "Four of a kind"), 0)
        self.assertEqual(score([2, 2, 4, 5, 6], "Four of a kind"), 0)
        self.assertEqual(score([2, 2, 4, 4, 6], "Four of a kind"), 0)
        self.assertEqual(score([2, 2, 2, 5, 6], "Four of a kind"), 0)
        self.assertEqual(score([2, 2, 2, 5, 5], "Four of a kind"), 0)
        self.assertEqual(score([2, 2, 2, 2, 6], "Four of a kind"), 8)
        self.assertEqual(score([2, 2, 2, 2, 2], "Four of a kind"), 0)


    def test_small_straight(self):
        self.assertEqual(score([1, 2, 4, 5, 6], "Small straight"), 0)
        self.assertEqual(score([1, 2, 3, 4, 5], "Small straight"), 15)
        self.assertEqual(score([1, 1, 3, 4, 5], "Small straight"), 0)
        self.assertEqual(score([1, 1, 3, 3, 5], "Small straight"), 0)
        self.assertEqual(score([1, 1, 1, 4, 5], "Small straight"), 0)
        self.assertEqual(score([1, 1, 1, 4, 4], "Small straight"), 0)
        self.assertEqual(score([1, 1, 1, 1, 5], "Small straight"), 0)
        self.assertEqual(score([1, 1, 1, 1, 1], "Small straight"), 0)


    def test_large_straight(self):
        self.assertEqual(score([1, 2, 4, 5, 6], "Large straight"), 0)
        self.assertEqual(score([1, 2, 3, 4, 5], "Large straight"), 0)
        self.assertEqual(score([2, 3, 4, 5, 6], "Large straight"), 20)
        self.assertEqual(score([2, 2, 4, 5, 6], "Large straight"), 0)
        self.assertEqual(score([2, 2, 4, 4, 6], "Large straight"), 0)
        self.assertEqual(score([2, 2, 2, 5, 6], "Large straight"), 0)
        self.assertEqual(score([2, 2, 2, 5, 5], "Large straight"), 0)
        self.assertEqual(score([2, 2, 2, 2, 6], "Large straight"), 0)
        self.assertEqual(score([2, 2, 2, 2, 2], "Large straight"), 0)


    def test_full_house(self):
        self.assertEqual(score([2, 3, 4, 5, 6], "Full house"), 0)
        self.assertEqual(score([2, 2, 4, 5, 6], "Full house"), 0)
        self.assertEqual(score([2, 2, 4, 4, 6], "Full house"), 0)
        self.assertEqual(score([2, 2, 2, 5, 6], "Full house"), 0)
        self.assertEqual(score([2, 2, 2, 5, 5], "Full house"), 16)
        self.assertEqual(score([2, 2, 2, 2, 6], "Full house"), 0)
        self.assertEqual(score([2, 2, 2, 2, 2], "Full house"), 0)


    def test_yahtzee(self):
        self.assertEqual(score([2, 3, 4, 5, 6], "Yahtzee"), 0)
        self.assertEqual(score([2, 2, 4, 5, 6], "Yahtzee"), 0)
        self.assertEqual(score([2, 2, 4, 4, 6], "Yahtzee"), 0)
        self.assertEqual(score([2, 2, 2, 5, 6], "Yahtzee"), 0)
        self.assertEqual(score([2, 2, 2, 5, 5], "Yahtzee"), 0)
        self.assertEqual(score([2, 2, 2, 2, 6], "Yahtzee"), 0)
        self.assertEqual(score([2, 2, 2, 2, 2], "Yahtzee"), 50)


    def test_chance(self):
        self.assertEqual(score([2, 3, 4, 5, 6], "Chance"), 20)
        self.assertEqual(score([2, 2, 4, 5, 6], "Chance"), 19)
        self.assertEqual(score([2, 2, 4, 4, 6], "Chance"), 18)
        self.assertEqual(score([2, 2, 2, 5, 6], "Chance"), 17)
        self.assertEqual(score([2, 2, 2, 5, 5], "Chance"), 16)
        self.assertEqual(score([2, 2, 2, 2, 6], "Chance"), 14)
        self.assertEqual(score([2, 2, 2, 2, 2], "Chance"), 10)


if __name__ == "__main__":
    unittest.main()
