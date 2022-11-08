from typing import Literal, Union

Score = Literal["love", "15", "30", "40"]

Status = Union[
    tuple[Score, Score],
    Literal["deuce", "1:adv", "2:adv", "1:wins", "2:wins"]
]

class Game:
    status: Status

    def __init__(self) -> None:
        self.status = ("love", "love")
    
    def point1(self) -> None:
        match self.status:
            case ("40", s2):
                assert(s2 != "40")
                self.status = "1:wins"
            case ("30", "40"):
                self.status = "deuce"
            case (s1, s2):
                self.status = (up(s1), s2)
            case "deuce":
                self.status = "1:adv"
            case "1:adv":
                self.status = "1:wins"
            case "2:adv":
                self.status = "deuce"
            case "1:wins" | "2:wins":
                raise ValueError("Game over")
    
    def point2(self) -> None:
        match self.status:
            case (s1, "40"):
                assert(s1 != "40")
                self.status = "2:wins"
            case ("40", "30"):
                self.status = "deuce"
            case (s1, s2):
                self.status = (s1, up(s2))
            case "deuce":
                self.status = "2:adv"
            case "1:adv":
                self.status = "deuce"
            case "2:adv":
                self.status = "2:wins"
            case "1:wins" | "2:wins":
                raise ValueError("Game over")

def up(score: Score) -> Score:
    match score:
        case "love":
            return "15"
        case "15":
            return "30"
        case "30":
            return "40"
        case "40":
            assert(False)
