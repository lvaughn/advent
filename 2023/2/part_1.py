#!/usr/bin/env python3

import re
import sys


part_1_answer = 0
part_2_answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

game_re = re.compile(r'Game\s+(\d+):\s*(.*)')
number_re = re.compile(r'\s*(\d+)\s+(\w)')
for l in lines:
    m = game_re.match(l)
    id = int(m.group(1))
    pulls = m.group(2).split(';')
    limits = {'g': 13, 'b': 14, 'r': 12}
    max_values = {'r': 0, 'g': 0, 'b': 0}
    possible = True
    for p in pulls:
        parts = p.split(',')
        for i in parts:
            m = number_re.match(i)
            max_values[m.group(2)] = max(int(m.group(1)), max_values[m.group(2)])
            if int(m.group(1)) > limits[m.group(2)]:
                possible = False
    if possible:
        part_1_answer += id
    power = max_values['r'] * max_values['g'] * max_values['b']
    part_2_answer += power

        
print(f"Part 1: {part_1_answer}")
print(f"Part 2: {part_2_answer}")