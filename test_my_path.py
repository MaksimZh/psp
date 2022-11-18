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

    def test(self):
        lead()


if __name__ == "__main__":
    unittest.main()
