#!/usr/bin/env python3

import sys

answer = 0
with open(sys.argv[1], 'r') as infile:
    instructions = [l.strip() for l in infile]
values = [1]

for inst in instructions:
    if inst == 'noop':
        values.append(values[-1])
    elif inst.startswith('addx'):
        values.append(values[-1])
        i, val = inst.split(' ')
        values.append(values[-1] + int(val))

for x in range(6):
    idx = 20 + (40*x)
    answer += idx * values[idx-1]

print("Part 1", answer)
