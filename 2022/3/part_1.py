#!/usr/bin/env python3
from string import ascii_uppercase, ascii_lowercase
import sys

scores = {}
for i, l in enumerate(ascii_lowercase):
    scores[l] = i+1
for i, l in enumerate(ascii_uppercase):
    scores[l] = i+27

total = 0
with open(sys.argv[1], 'r') as infile:
    for line in [l.strip() for l in infile]:
        split = len(line) // 2
        a = set(line[:split])
        b = set(line[split:])
        total += scores[list(a & b)[0]]

print("Part 1", total)
