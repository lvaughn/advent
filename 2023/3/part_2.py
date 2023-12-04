#!/usr/bin/env python3

import re
import pprint
import sys
from string import digits

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
# Get the parts and their locations
part_numbers = []
num_re = re.compile(r'(\d+)')
for row, line in enumerate(lines):
    m = num_re.search(line)
    while m is not None:
        is_part = False
        start, end = m.span()
        part_numbers.append((row, start, end, int(m.group(1))))
        
        m = num_re.search(line, end)

for row, line in enumerate(lines):
    for col, ch in enumerate(line):
        if ch != '*':
            continue
        # How many parts is it near
        next_to_parts = []
        for p_row, start, end, value in part_numbers:
            if p_row < row - 1 or p_row > row + 1:
                continue
            if p_row == row:
                if col == start - 1 or col == end:
                    next_to_parts.append(value)
            else:
                if col >= start-1 and col <= end:
                    next_to_parts.append(value)
        if len(next_to_parts) == 2:
            answer += next_to_parts[0] * next_to_parts[1]
    
print(f"Part 1: {answer}")