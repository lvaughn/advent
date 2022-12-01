#!/usr/bin/env python3

import sys

elves = []
most = -1
current = 0
with open(sys.argv[1], 'r') as infile:
    for line in infile:
        if line.strip() == '':
            elves.append(current)
            if current > most:
                most = current
            current = 0
        else:
            current += int(line)
elves.append(current)
if current > most:
    most = current

elves.sort()
print("Part 1", most)
print("Part 2", sum(elves[-3:]))