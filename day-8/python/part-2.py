#!/usr/bin/env python3

from typing import Dict, List, Set


def decode(signals: List[Set[str]]) -> Dict[int, Set[str]]:
    digits = {}

    for signal in sorted(signals, key=len):
        if len(signal) == 2:
            digits[1] = signal
            continue

        if len(signal) == 3:
            digits[7] = signal
            continue

        if len(signal) == 4:
            digits[4] = signal
            continue

        if len(signal) == 7:
            digits[8] = signal 
            continue

        if len(signal) == 5:
            if digits[7].issubset(signal):
                digits[3] = signal
                continue
            if len(digits[4].intersection(signal)) == 2:
                digits[2] = signal
                continue
            if len(digits[4].intersection(signal)) == 3:
                digits[5] = signal
                continue

        if len(signal) == 6:
            if digits[4].issubset(signal):
                digits[9] = signal
                continue
            if digits[5].issubset(signal):
                digits[6] = signal
                continue
            if digits[1].issubset(signal):
                digits[0] = signal
                continue

    return digits


def convert(digits: Dict[int, Set[str]], output: List[Set[str]]) -> int:
    value = 0

    for signal in output:
        value *= 10
        for index, digit in digits.items():
            if signal == digit:
                value += index

    return value


sum = 0

while True:
    try:
        signals, output = input().split(" | ")

        signals = list(map(set, signals.split(" ")))
        output = list(map(set, output.split(" ")))

        sum += convert(decode(signals), output)

    except EOFError:
        break

print(sum)

# Answer: 1097568
