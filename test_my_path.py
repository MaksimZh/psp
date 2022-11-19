import unittest

from my_path import Land, Path, Field, lead

class Test_Field(unittest.TestCase):

    def test(self):
        f = Field(3, 2)
        self.assertEqual(f.height, 3)
        self.assertEqual(f.width, 2)
        self.assertEqual([[f[y, x] for x in range(-1, f.width + 1)] \
            for y in range(-1, f.height + 1)],
            [
                [Land.wall, Land.wall, Land.wall, Land.wall],
                [Land.wall, Land.free, Land.free, Land.wall],
                [Land.wall, Land.free, Land.free, Land.wall],
                [Land.wall, Land.free, Land.free, Land.wall],
                [Land.wall, Land.wall, Land.wall, Land.wall],
            ])
        f[0, 1] = Land.wall
        f[0, 0] = Path(0)
        f[1, 0] = Path(1)
        f[1, 1] = Path(2)
        self.assertEqual([[f[y, x] for x in range(-1, f.width + 1)] \
            for y in range(-1, f.height + 1)],
            [
                [Land.wall, Land.wall, Land.wall, Land.wall],
                [Land.wall, Path(0), Land.wall, Land.wall],
                [Land.wall, Path(1), Path(2), Land.wall],
                [Land.wall, Land.free, Land.free, Land.wall],
                [Land.wall, Land.wall, Land.wall, Land.wall],
            ])


class Test(unittest.TestCase):

    def check_path(self, field: list[str], path: list[str], length: int):
        self.assertTrue(len(field) == len(path))
        p: list[tuple[int, int]] = []
        s: tuple[int, int] = (-1, -1)
        f: tuple[int, int] = (-1, -1)
        for r in range(len(field)):
            self.assertTrue(len(field[r]) == len(field[0]))
            self.assertTrue(len(field[r]) == len(path[r]))
            for c in range(len(field[r])):
                match path[r][c]:
                    case "s":
                        self.assertEqual(field[r][c], "s")
                        s = (r, c)
                    case "f":
                        self.assertEqual(field[r][c], "f")
                        f = (r, c)
                    case "+":
                        self.assertEqual(field[r][c], ".")
                        p.append((r, c))
                    case _:
                        self.assertEqual(field[r][c], path[r][c])
        self.assertEqual(len(p) + 2, length)
        self.assertNotEqual(s, (-1, -1))
        self.assertNotEqual(f, (-1, -1))
        points = set(p)
        pt = s
        while len(points) > 0:
            neighbors = set([(pt[0] + 1, pt[1]), (pt[0] - 1, pt[1]),
                (pt[0], pt[1] + 1), (pt[0], pt[1] - 1)])
            next = neighbors & points
            self.assertEqual(len(next), 1)
            pt = next.pop()
            points.remove(pt)
        self.assertEqual(abs(pt[0] - f[0]) + abs(pt[1] - f[1]), 1)


    def test_check_path(self):
        self.check_path([
            ".s**.f*",
            "*..*...",
            ".*....*",
        ], [
            ".s**.f*",
            "*++*.+.",
            ".*++++*",
        ], 9)

    def test1(self):
        src = [
            ".s..f.",
        ]
        self.check_path(src, lead(src), 4)
        src = [
            ".s....",
            "......",
            "....f.",
        ]
        self.check_path(src, lead(src), 6)

    def test2(self):
        src = [
            ".s**.f*",
            "*..*...",
            ".*....*",
        ]
        self.check_path(src, lead(src), 9)
        src = [
            ".s**f..",
            "*..***.",
            ".......",
        ]
        self.check_path(src, lead(src), 12)
        src = [
            "......f",
            "s.****.",
            ".......",
        ]
        self.check_path(src, lead(src), 8)


if __name__ == "__main__":
    unittest.main()
