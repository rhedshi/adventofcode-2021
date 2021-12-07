#!/usr/bin/env python3


def get_children(state: int = 0, day: int = 0, days: int = 0) -> int:
    if day > days:
        return 0

    children = 1

    while day < days:
        day += state + 1
        state = 6
        children += get_children(state=8, day=day, days=days)

    return children


while True:
    try:
        states = list(map(int, input().split(",")))
    except EOFError:
        break

children = 0
days = 80

for state in states:
    children += get_children(state=state, day=0, days=days)

print(children)

# Answer: 376194
