#!/usr/bin/env python3

from typing import Dict, List, Optional


def get_children(state: int = 0, day: int = 0, days: int = 0, memoize: Dict[int, List[Optional[int]]] = {}) -> int:
    if day > days:
        return 0

    if day in memoize and memoize[day][state] is not None:
        return memoize[day][state]

    day_ = day
    state_ = state
    children = 1

    while day_ < days:
        day_ += state_ + 1
        state_ = 6
        children += get_children(state=8, day=day_, days=days, memoize=memoize)

    memoize[day] = memoize.get(day, [None] * 9)
    memoize[day][state] = children

    return children


while True:
    try:
        states = list(map(int, input().split(",")))
    except EOFError:
        break

children = 0
days = 256
memoize = {}

for state in states:
    children += get_children(state=state, day=0, days=days, memoize=memoize)

print(children)

# Answer: 1693022481538
