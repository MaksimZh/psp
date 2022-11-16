from typing import TypeVar, Any

T = TypeVar("T")

def evaluate(secret: list[T], guessing: list[T]) -> tuple[int, int]:
    assert(len(secret) > 0)
    assert(len(secret) == len(guessing))
    assert(isinstance(secret[0] == guessing[0], bool))
    assert(all_different(secret))
    assert(all_different(guessing))
    missed_secret = set[T]()
    missed_guessing = set[T]()
    well_placed_count = 0
    for s, g in zip(secret, guessing):
        if s == g:
            well_placed_count += 1
        else:
            missed_secret.add(s)
            missed_guessing.add(g)
    misplaced_count = len(missed_secret & missed_guessing)
    return (well_placed_count, misplaced_count)


def all_different(code: list[Any]) -> bool:
    assert(len(code) > 0)
    assert(isinstance(code[0] == code[0], bool))
    return len(set(code)) == len(code)
