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
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
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
        autocomplete = ""

        while not queue.empty():
            autocomplete += PAIRS[queue.get()]

        return Line.INCOMPLETE, autocomplete


completion_string_scores = []

while True:
    try:
        line = input()

        error, characters = parse(line)

        if error == Line.INCOMPLETE:
            completion_string_score = 0

            for character in characters:
                completion_string_score *= 5
                completion_string_score += POINTS[character]

            completion_string_scores.append(completion_string_score)

    except EOFError:
        break
 
middle_score = sorted(completion_string_scores)[len(completion_string_scores) // 2]

print(middle_score)

# Answer: 4001832844
