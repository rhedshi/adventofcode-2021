#!/usr/bin/env python3

from enum import Enum
from queue import LifoQueue
from typing import Optional, Tuple

PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


class Line(Enum):
    CORRECT = 1
    INCOMPLETE = 2
    CORRUPTED = 3


def parse(line: str) -> Tuple[Line, Optional[str]]:
    queue = LifoQueue()

    for character in line:
        if character in PAIRS.keys():
            queue.put(character)

        if character in PAIRS.values():
            open = queue.get()
            close = character

            if PAIRS[open] == close:
                continue
            else:
                return Line.CORRUPTED, close

    if queue.empty():
        return Line.CORRECT, None
    else:
        return Line.INCOMPLETE, None


syntax_error_score = 0

while True:
    try:
        line = input()

        error, character = parse(line)

        if error == Line.CORRUPTED:
            syntax_error_score += POINTS[character]

    except EOFError:
        break
 
print(syntax_error_score)

# Answer: 392139
