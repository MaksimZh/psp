from enum import Enum
from typing import NewType

class Land(Enum):
    free = 0
    wall = 1

Path = NewType("Path", int)

Cell = Land | Path


class Field:
    
    data: list[list[Cell]]
    
    def __init__(self, height: int, width: int) -> None:
        self.data = \
            [list[Cell]([Land.wall]) * (width + 2)] + \
            [list[Cell]([Land.wall] + [Land.free] * width + [Land.wall]) \
                for _ in range(height)] + \
            [list[Cell]([Land.wall]) * (width + 2)]

    @property
    def height(self) -> int:
        return len(self.data) - 2

    @property
    def width(self) -> int:
        return len(self.data[0]) - 2

    def __getitem__(self, yx: tuple[int, int]) -> Cell:
        y, x = yx
        return self.data[y + 1][x + 1]

    def __setitem__(self, yx: tuple[int, int], value: Cell) -> None:
        y, x = yx
        self.data[y + 1][x + 1] = value


def load_field(image: list[str]) -> tuple[Field, tuple[int, int], tuple[int, int]]:
    field = Field(len(image), len(image[0]))
    start = (-1, -1)
    finish = (-1, -1)
    for r in range(len(image)):
        assert(len(image[r]) == field.width)
        for c in range(len(image[r])):
            match image[r][c]:
                case "s":
                    start = (r, c)
                    field[r, c] = Land.free
                case "f":
                    finish = (r, c)
                    field[r, c] = Land.free
                case ".":
                    field[r, c] = Land.free
                case "*":
                    field[r, c] = Land.wall
                case _:
                    assert(False)
    return field, start, finish


def make_wave(field: Field, wave: int) -> None:
    for r in range(field.height):
        for c in range(field.width):
            if field[r, c] == Path(wave - 1):
                for y, x in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if field[y, x] == Land.free:
                        field[y, x] = Path(wave)


def lead(image: list[str]) -> list[str]:
    field, start, finish = load_field(image)
    field[start[0], start[1]] = Path(0)
    wave = 0
    while field[finish[0], finish[1]] == Land.free:
        wave += 1
        make_wave(field, wave)
    pt = finish
    dest = [[c for c in row] for row in image]
    for w in reversed(range(1, wave )):
        r, c = pt
        for y, x in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if field[y, x] == Path(w):
                dest[y][x] = "+"
                pt = (y, x)
                break
    return ["".join(row) for row in dest]
