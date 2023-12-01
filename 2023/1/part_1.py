#!/usr/bin/env python3
import sys
from string import digits

def get_number(s):
    first = None
    for d in s:
        if d in digits:
            if first is None:
                first = d
            last = d
    return int(f"{first}{last}")

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
answer = sum(get_number(l) for l in lines)

print("Part 1", answer)
