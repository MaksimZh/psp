from typing import Literal, Callable
from itertools import groupby

Dice = Literal[1, 2, 3, 4, 5, 6]
Category = Literal[
    "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes",
    "Pair", "Two pairs", "Three of a kind", "Four of a kind",
    "Small straight", "Large straight", "Full house",
    "Yahtzee", "Chance"]
Roll = list[Dice]
ScoreFunc = Callable[[Roll], int]


def score(roll: Roll, category: Category) -> int:
    return score_funcs[category](sorted(roll))


def score_func_value(value: Dice) -> ScoreFunc:

    def func(roll: Roll) -> int:
        return sum(v for v in roll if v == value)
    
    return func

def score_func_size(size: int) -> ScoreFunc:

    def func(roll: Roll) -> int:
        s = split_roll(roll)[size]
        if len(s) == 0:
            return 0
        return s[-1] * size

    return func

def score_two_pairs(roll: Roll) -> int:
    pairs = split_roll(roll)[2]
    if len(pairs) != 2:
        return 0
    return sum(pairs) * 2

def score_func_straight(start: Dice) -> ScoreFunc:

    def func(roll: Roll) -> int:
        singles = split_roll(roll)[1]
        if singles != list(range(start, start + 5)):
            return 0
        return sum(singles)

    return func

def score_full_house(roll: Roll) -> int:
    s = split_roll(roll)
    if len(s[2]) != 1 or len(s[3]) != 1:
        return 0
    return s[2][0] * 2 + s[3][0] * 3

def score_yahtzee(roll: Roll) -> int:
    s = split_roll(roll)
    if len(s[5]) != 1:
        return 0
    return 50

def score_chance(roll: Roll) -> int:
    return sum(roll)

score_funcs: dict[Category, ScoreFunc] = {
    "Ones": score_func_value(1),
    "Twos": score_func_value(2),
    "Threes": score_func_value(3),
    "Fours": score_func_value(4),
    "Fives": score_func_value(5),
    "Sixes": score_func_value(6),
    "Pair": score_func_size(2),
    "Two pairs": score_two_pairs,
    "Three of a kind": score_func_size(3),
    "Four of a kind": score_func_size(4),
    "Small straight": score_func_straight(1),
    "Large straight": score_func_straight(2),
    "Full house": score_full_house,
    "Yahtzee": score_yahtzee,
    "Chance": score_chance,
}

RollSplit = tuple[list[Dice], list[Dice], list[Dice], list[Dice], list[Dice], list[Dice]]

def split_roll(roll: Roll) -> RollSplit:
    result: RollSplit = ([], [], [], [], [], [])
    for k, g in groupby(roll):
        result[len(list(g))].append(k)
    return result
