#!/usr/bin/env python3

while True:
    try:
        positions = list(map(int, input().split(",")))
    except EOFError:
        break
 
destination = sum(positions) // len(positions)

fuel = 0

for position in positions:
    distance = abs(destination - position)
    fuel += distance * (distance + 1) // 2

print(fuel)

# Answer: 98368490
