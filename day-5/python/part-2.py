#!/usr/bin/env python3

hydrothermal_vents = {}

while True:
    try:
        coordinates = input().split(" -> ") 

        A = tuple(map(int, coordinates[0].split(",")))
        B = tuple(map(int, coordinates[1].split(",")))

        delta = max(abs(A[0] - B[0]), abs(A[1] - B[1])) + 1

        x = 1 if A[0] < B[0] else -1 if A[0] > B[0] else 0
        y = 1 if A[1] < B[1] else -1 if A[1] > B[1] else 0

        for d in range(delta):
            i = d * x
            j = d * y
            hydrothermal_vents[A[0] + i] = hydrothermal_vents.get(A[0] + i, {})
            hydrothermal_vents[A[0] + i][A[1] + j] = hydrothermal_vents[A[0] + i].get(A[1] + j, 0)
            hydrothermal_vents[A[0] + i][A[1] + j] += 1

    except EOFError:
        break

points = 0

for x in hydrothermal_vents.keys():
    for y in hydrothermal_vents[x].keys():
        if hydrothermal_vents[x][y] > 1:
            points += 1

print(points)

# Answer: 21406
