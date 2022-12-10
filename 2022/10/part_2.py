#!/usr/bin/env python3

import sys

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

rows = []
pos = 0
for r in range(6):
    row = ""
    for c in range(40):
        if abs((pos % 40) - values[pos]) < 2:
            row += '#'
        else:
            row += ' '
        pos += 1
    rows.append(row)

print("Part 2")
for r in rows:
    print(r)
