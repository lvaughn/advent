#!/usr/bin/env python3

import numpy as np
import re


grid = np.zeros((101, 101, 101), dtype=int)
line_re = re.compile(r'(\S+)\s(.*)')
var_re = re.compile(r'=(-?\d+)..(-?\d+)')

def parse_var(s):
    m = var_re.search(s)
    return (int(m[1]), int(m[2]))

commands = []
with open("input.txt", "r") as infile:
    for line in infile:
        m = line_re.match(line)
        cmd = m[1]
        x, y, z = m[2].split(',')
        command = (cmd, parse_var(x), parse_var(y), parse_var(z))
        commands.append(command)

for state, x, y, z in commands:
    if -50 <= x[0] <= 50:
        value = 0
        if state == 'on':
            value=1
        grid[x[0]+50:x[1]+51, y[0]+50:y[1]+51, z[0]+50:z[1]+51] = value

number_in = sum(sum(sum(grid)))
print(f"Part 1: {number_in}")

