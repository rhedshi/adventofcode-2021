#!/usr/bin/env python3

from typing import List, Tuple


def check_lowest_point(heightmap: List[List[int]], i: int, j: int) -> Tuple[bool, int]:
    adjacent = []

    try:
        adjacent.append(heightmap[i - 1][j])
    except IndexError:
        pass

    try:
        adjacent.append(heightmap[i + 1][j])
    except IndexError:
        pass

    try:
        adjacent.append(heightmap[i][j - 1])
    except IndexError:
        pass

    try:
        adjacent.append(heightmap[i][j + 1])
    except IndexError:
        pass

    if heightmap[i][j] < min(adjacent):
        return True, 1 + heightmap[i][j]

    return False, 0


heightmap = []

while True:
    try:
        heightmap.append(list(map(int, input())))
    except EOFError:
        break
 
risk_level = 0

for i in range(len(heightmap)):
    for j in range(len(heightmap[i])):
        risk_level += check_lowest_point(heightmap, i, j)[1]

print(risk_level)

# Answer: 465
