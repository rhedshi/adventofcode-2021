#!/usr/bin/env python3

position = 0
depth = 0

while True:
    try:
        command = input()
    except EOFError:
        break

    direction, distance = command.split(" ")

    if direction == "forward":
        position += int(distance)
    elif direction == "up":
        depth -= int(distance)
    elif direction == "down":
        depth += int(distance)
    else:
        pass

print(position * depth)

# Answer: 1714680
