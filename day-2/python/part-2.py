#!/usr/bin/env python3

aim = 0
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
        depth += aim * int(distance)
    elif direction == "up":
        aim -= int(distance)
    elif direction == "down":
        aim += int(distance)
    else:
        pass

print(position * depth)

# Answer: 1963088820
