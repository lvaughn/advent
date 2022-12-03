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
    lines = [l.strip() for l in infile]
    for i in range(len(lines)//3):
        a = set(lines[i*3])
        b = set(lines[i*3+1])
        c = set(lines[i*3+2])
        u = a & b & c
        total += scores[list(u)[0]]
print("Part 2", total)
