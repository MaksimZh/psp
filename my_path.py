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


def lead(image: list[str]) -> list[str]:
    #field = Field(len(image), len(image[0]))
    return image
