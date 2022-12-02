#!/usr/bin/env python3
import sys

score = 0
with open(sys.argv[1], 'r') as infile:
    for line in [l.strip() for l in infile]:
        elf, me = line.split(' ')
        if elf == 'A':
            if me == 'X':
                score += 3
            elif me == 'Y':
                score += 4
            else:
                score += 8
        elif elf == "B":
            if me == 'X':
                score += 1
            elif me == 'Y':
                score += 5
            else:
                score += 9
        else:  # elf == C
            if me == 'X':
                score += 2
            elif me == 'Y':
                score += 6
            else:
                score += 7


print("Part 2", score)
