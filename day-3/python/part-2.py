#!/usr/bin/env python3

total = set()
common = {}

while True:
    try:
        binary = input()
    except EOFError:
        break

    decimal = int(binary, 2)

    for i in range(len(binary)):
        bit = int(binary[i])
        common[i] = common.get(i, {})
        common[i][bit] = common[i].get(bit, set())
        common[i][bit].add(decimal)

    total.add(decimal)

oxygen_generator_rating = total
co2_scrubber_rating = total

for i in range(len(common)):
    if len(oxygen_generator_rating) > 1:
        oxygen_generator_rating = oxygen_generator_rating.intersection(common[i][1]) if len(oxygen_generator_rating.intersection(common[i][1])) >= len(oxygen_generator_rating.intersection(common[i][0])) else oxygen_generator_rating.intersection(common[i][0])

    if len(co2_scrubber_rating) > 1:
        co2_scrubber_rating = co2_scrubber_rating.intersection(common[i][0]) if len(co2_scrubber_rating.intersection(common[i][0])) <= len(co2_scrubber_rating.intersection(common[i][1])) else co2_scrubber_rating.intersection(common[i][1])

life_support_rating = oxygen_generator_rating.pop() * co2_scrubber_rating.pop()

print(life_support_rating)

# Answer: 2135254
