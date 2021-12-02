#!/usr/bin/env python3

increase = 0

N = 3
i = 0
window = [None] * N

while True:
    try:
        depth = int(input())
    except EOFError:
        break

    if window[i] is not None and depth > window[i]:
        increase += 1

    window[i] = depth
    i += 1
    i %= N
 

print(increase)

# Answer: 1597
