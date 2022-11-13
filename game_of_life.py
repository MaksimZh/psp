from enum import Enum
from typing_extensions import Self

class State(Enum):
    DEAD = 0
    LIVE = 1

class Grid:

    data: list[list[State]]

    def __init__(self) -> None:
        self.data = []

    @classmethod
    def new_empty(cls, height: int, width: int) -> Self:
        grid = Grid()
        for _ in range(height + 2):
            grid.data.append([State.DEAD] * (width + 2))
        return grid

    @classmethod
    def from_image(cls, image: list[str]) -> Self:
        grid = Grid()
        grid.data = [[State.DEAD] + [
            State.LIVE if char == "*" else State.DEAD \
                for char in row] + [State.DEAD] \
                for row in image]
        width = len(grid.data[0])
        grid.data = [[State.DEAD] * width] + grid.data + [[State.DEAD] * width]
        return grid

    def get_image(self) -> list[str]:
        return ["".join([
            "*" if cell == State.LIVE else "." \
                for cell in row[1:-1]]) \
                for row in self.data[1:-1]]

    def __getitem__(self, yx: tuple[int, int]) -> State:
        y, x = yx
        return self.data[y + 1][x + 1]

    def __setitem__(self, yx: tuple[int, int], value: State) -> None:
        y, x = yx
        self.data[y + 1][x + 1] = value

    def count_neighbors(self, y: int, x: int) -> int:
        return sum([1 if self[i, j] == State.LIVE else 0 \
            for i, j in [
                (y - 1, x - 1),
                (y - 1, x),
                (y - 1, x + 1),
                (y, x - 1),
                (y, x + 1),
                (y + 1, x - 1),
                (y + 1, x),
                (y + 1, x + 1),
            ]])

    @property
    def height(self) -> int:
        return len(self.data) - 2

    @property
    def width(self) -> int:
        return len(self.data[0]) - 2


def next(image: list[str]):
    source = Grid.from_image(image)
    dest = Grid.new_empty(source.height, source.width)
    for y in range(source.height):
        for x in range(source.width):
            neighbors = source.count_neighbors(y, x)
            match source[y, x]:
                case State.LIVE:
                    match neighbors:
                        case 2 | 3:
                            dest[y, x] = State.LIVE
                        case _:
                            dest[y, x] = State.DEAD
                case State.DEAD:
                    match neighbors:
                        case 3:
                            dest[y, x] = State.LIVE
                        case _:
                            dest[y, x] = State.DEAD
    return dest.get_image()
