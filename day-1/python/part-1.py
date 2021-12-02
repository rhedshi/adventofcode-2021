#!/usr/bin/env python3

increase = 0
current = None

while True:
    try:
        depth = int(input())
    except EOFError:
        break

    if current is not None and depth > current:
        increase += 1

    current = depth
 
print(increase)

# Answer: 1553
