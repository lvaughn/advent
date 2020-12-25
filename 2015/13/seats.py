#!/usr/bin/env python3

import re
from itertools import permutations

happiness = {}  # tuple(a, b) => int
names = set('m')
with open('input.txt', 'r') as f:
    input_re = re.compile(r'(\w+) would (\w+) (\d+).*\s(\w+)\.')
    for line in f:
        m = input_re.match(line)
        amount = int(m[3])
        if m[2] == 'lose':
            amount = -amount
        happiness[(m[1], m[4])] = amount
        names.add(m[1])

best = -999999999
for order in permutations(names):
    happy = 0
    for i in range(len(order)):
        happy += happiness.get((order[i], order[(i+1)%len(order)]), 0)
        happy += happiness.get((order[(i+1)%len(order)], order[i]), 0)
    best = max(best, happy)

print(best)
