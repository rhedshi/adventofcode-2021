#!/usr/bin/env python3

common = {}

while True:
    try:
        binary = input()
    except EOFError:
        break

    for i in range(len(binary)):
        bit = int(binary[i])
        common[i] = common.get(i, {})
        common[i][bit] = common[i].get(bit, 0) + 1

gamma_rate = 0
epsilon_rate = 0

for i in range(len(common)):
    gamma_rate *= 2
    epsilon_rate *= 2

    gamma_rate += 0 if common[i][0] > common[i][1] else 1
    epsilon_rate += 1 if common[i][0] > common[i][1] else 0

power_consumption = gamma_rate * epsilon_rate

print(power_consumption)

# Answer: 2595824
