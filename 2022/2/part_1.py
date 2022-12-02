#!/usr/bin/env python3
import sys

score = 0

with open(sys.argv[1], 'r') as infile:
    for line in [l.strip() for l in infile]:
        elf, me = line.split(' ')
        if elf == 'A':
            if me == 'X':
                score += 4
            elif me == 'Y':
                score += 8
            else:
                score += 3
        elif elf == "B":
            if me == 'X':
                score += 1
            elif me == 'Y':
                score += 5
            else:
                score += 9
        else:  # elf == C
            if me == 'X':
                score += 7
            elif me == 'Y':
                score += 2
            else:
                score += 6

print("Part 1", score)
