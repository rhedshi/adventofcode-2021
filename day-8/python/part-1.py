#!/usr/bin/env python3

unique = 0

while True:
    try:
        _, output = input().split(" | ")

        output = output.split(" ")

        for signal in output:
            unique += len(signal) == 2 or len(signal) == 3 or len(signal) == 4 or len(signal) == 7

    except EOFError:
        break

print(unique)

# Answer: 473
