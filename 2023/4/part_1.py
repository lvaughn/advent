#!/usr/bin/env python3

import re
import sys

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

line_re = re.compile(r'.*:\s*(.+)\|(.+)')
for line in lines:
    m = line_re.match(line)
    winning_numbers = re.split(r'\s+', m.group(1).strip())
    my_numbers = re.split(r'\s+', m.group(2).strip())
    matches = [m for m in my_numbers if m in winning_numbers]
    if len(matches) > 0:
        answer += 2**(len(matches)-1)

print("Part 1", answer)


