#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as infile:
    line = [l.strip() for l in infile][0]

pos = 4
while len(set(line[pos-4:pos])) != 4:
    pos += 1
print("Part 1", pos)
pos = 14
while len(set(line[pos-14:pos])) != 14:
    pos += 1
print("Part 2", pos)
