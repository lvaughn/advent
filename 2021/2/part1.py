#!/usr/bin/env python3

import numpy as np

hor = 0
depth = 0
with open("input.txt", "r") as infile:
    for line in infile:
        op, amount = line.split()
        if op[0] == 'f':
            hor += int(amount)
        elif op[0] == 'u':
            depth -= int(amount)
        elif op[0] == 'd':
            depth += int(amount)

print(hor, depth, hor*depth)


