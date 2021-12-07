#!/usr/bin/env python3

while True:
    try:
        positions = list(map(int, input().split(",")))
    except EOFError:
        break
 
destination = sorted(positions)[len(positions) // 2]

fuel = 0

for position in positions:
    fuel += abs(destination - position)

print(fuel)

# Answer: 355150
