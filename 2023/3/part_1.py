#!/usr/bin/env python3

import re
import sys
from string import digits

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
def has_part(s):
    for letter in s:
        if letter != '.' and letter not in digits:
            return True
    return False

num_re = re.compile(r'(\d+)')
for row, line in enumerate(lines):
    m = num_re.search(line)
    while m is not None:
        is_part = False
        start, end = m.span()
        # See if it's a next to a part 
        if row > 0:
            is_part |= has_part(lines[row-1][max(0, start-1):end+1])
        is_part |= has_part(line[max(0, start-1):end+1])
        if row < len(lines)-1:
            is_part |= has_part(lines[row+1][max(0, start-1):end+1])
        if is_part:
            answer += int(m.group(1))
            
        m = num_re.search(line, end)
        
print(f"Part 1: {answer}")
    
