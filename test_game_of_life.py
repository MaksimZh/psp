import unittest

import game_of_life as gol


class Test_Grid(unittest.TestCase):

    def test(self):
        image = [
            "....",
            "..*.",
            ".**.",
        ]
        grid = gol.Grid.from_image(image)
        self.assertEqual([[grid[y, x] for x in range(grid.width)] for y in range(grid.height)], [
            [gol.State.DEAD, gol.State.DEAD, gol.State.DEAD, gol.State.DEAD],
            [gol.State.DEAD, gol.State.DEAD, gol.State.LIVE, gol.State.DEAD],
            [gol.State.DEAD, gol.State.LIVE, gol.State.LIVE, gol.State.DEAD],
            ])
        grid[1, 2] = gol.State.DEAD
        grid[1, 3] = gol.State.LIVE
        self.assertEqual([[grid[y, x] for x in range(grid.width)] for y in range(grid.height)], [
            [gol.State.DEAD, gol.State.DEAD, gol.State.DEAD, gol.State.DEAD],
            [gol.State.DEAD, gol.State.DEAD, gol.State.DEAD, gol.State.LIVE],
            [gol.State.DEAD, gol.State.LIVE, gol.State.LIVE, gol.State.DEAD],
            ])
        self.assertEqual(grid.get_image(), [
            "....",
            "...*",
            ".**.",
        ])

    def test_count(self):
        grid = gol.Grid.from_image([
            "....",
            "..*.",
            ".**.",
        ])
        self.assertEqual([[grid.count_neighbors(y, x) for x in range(grid.width)] for y in range(grid.height)], [
            [0, 1, 1, 1],
            [1, 3, 2, 2],
            [1, 2, 2, 2],
            ])

        grid = gol.Grid.from_image([
            ".*..",
            "*.*.",
            ".**.",
        ])
        self.assertEqual([[grid.count_neighbors(y, x) for x in range(grid.width)] for y in range(grid.height)], [
            [2, 2, 2, 1],
            [2, 5, 3, 2],
            [2, 3, 2, 2],
            ])


class Test(unittest.TestCase):

    def test1(self):
        self.assertEqual(gol.next([
            "........",
            "....*...",
            "...**...",
            "........",
        ]), [
            "........",
            "...**...",
            "...**...",
            "........",
        ])

if __name__ == "__main__":
    unittest.main()
