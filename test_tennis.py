import unittest

import tennis


class Test(unittest.TestCase):

    def test_ko1(self):
        game = tennis.Game()
        self.assertEqual(game.status, ("love", "love"))
        game.point1()
        self.assertEqual(game.status, ("15", "love"))
        game.point1()
        self.assertEqual(game.status, ("30", "love"))
        game.point1()
        self.assertEqual(game.status, ("40", "love"))
        game.point1()
        self.assertEqual(game.status, "1:wins")

    def test_ko2(self):
        game = tennis.Game()
        self.assertEqual(game.status, ("love", "love"))
        game.point2()
        self.assertEqual(game.status, ("love", "15"))
        game.point2()
        self.assertEqual(game.status, ("love", "30"))
        game.point2()
        self.assertEqual(game.status, ("love", "40"))
        game.point2()
        self.assertEqual(game.status, "2:wins")

    def test_deuce1(self):
        game = tennis.Game()
        self.assertEqual(game.status, ("love", "love"))
        game.point1()
        self.assertEqual(game.status, ("15", "love"))
        game.point2()
        self.assertEqual(game.status, ("15", "15"))
        game.point2()
        self.assertEqual(game.status, ("15", "30"))
        game.point2()
        self.assertEqual(game.status, ("15", "40"))
        game.point1()
        self.assertEqual(game.status, ("30", "40"))
        game.point1()
        self.assertEqual(game.status, "deuce")
        game.point1()
        self.assertEqual(game.status, "1:adv")
        game.point2()
        self.assertEqual(game.status, "deuce")
        game.point1()
        self.assertEqual(game.status, "1:adv")
        game.point1()
        self.assertEqual(game.status, "1:wins")

    def test_deuce2(self):
        game = tennis.Game()
        self.assertEqual(game.status, ("love", "love"))
        game.point1()
        self.assertEqual(game.status, ("15", "love"))
        game.point2()
        self.assertEqual(game.status, ("15", "15"))
        game.point1()
        self.assertEqual(game.status, ("30", "15"))
        game.point1()
        self.assertEqual(game.status, ("40", "15"))
        game.point2()
        self.assertEqual(game.status, ("40", "30"))
        game.point2()
        self.assertEqual(game.status, "deuce")
        game.point2()
        self.assertEqual(game.status, "2:adv")
        game.point1()
        self.assertEqual(game.status, "deuce")
        game.point2()
        self.assertEqual(game.status, "2:adv")
        game.point2()
        self.assertEqual(game.status, "2:wins")

    def test_over1(self):
        game = tennis.Game()
        game.point1()
        game.point1()
        game.point1()
        game.point1()
        with self.assertRaises(ValueError) as context:
            game.point1()
        self.assertTrue("Game over" in context.exception.args)
        with self.assertRaises(ValueError) as context:
            game.point2()
        self.assertTrue("Game over" in context.exception.args)

    def test_over2(self):
        game = tennis.Game()
        game.point2()
        game.point2()
        game.point2()
        game.point2()
        with self.assertRaises(ValueError) as context:
            game.point1()
        self.assertTrue("Game over" in context.exception.args)
        with self.assertRaises(ValueError) as context:
            game.point2()
        self.assertTrue("Game over" in context.exception.args)


if __name__ == "__main__":
    unittest.main()
