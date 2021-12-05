#!/usr/bin/env python3

hydrothermal_vents = {}

while True:
    try:
        coordinates = input().split(" -> ") 

        A = tuple(map(int, coordinates[0].split(",")))
        B = tuple(map(int, coordinates[1].split(",")))

        A, B = sorted([A, B])

        if A[0] == B[0]:
            for y in range(A[1], B[1] + 1):
                hydrothermal_vents[A[0]] = hydrothermal_vents.get(A[0], {})
                hydrothermal_vents[A[0]][y] = hydrothermal_vents[A[0]].get(y, 0)
                hydrothermal_vents[A[0]][y] += 1

        if A[1] == B[1]:
            for x in range(A[0], B[0] + 1):
                hydrothermal_vents[x] = hydrothermal_vents.get(x, {})
                hydrothermal_vents[x][A[1]] = hydrothermal_vents[x].get(A[1], 0)
                hydrothermal_vents[x][A[1]] += 1

    except EOFError:
        break

points = 0

for x in hydrothermal_vents.keys():
    for y in hydrothermal_vents[x].keys():
        if hydrothermal_vents[x][y] > 1:
            points += 1

print(points)

# Answer: 7438
