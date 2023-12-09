#!/usr/bin/env python3
import numpy as np
import sys


def extend_arr(a):
    if np.all(a == 0):
        return 0
    to_add = extend_arr(a[1:] - a[:-1])
    return to_add + a[-1]

def extend_back(a):
    if np.all(a == 0):
        return 0
    to_sub = extend_back(a[1:] - a[:-1])
    return a[0] - to_sub

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
for line in lines:
    values = [int(a) for a in line.split(' ')]
    values = np.array(values, dtype=int)
    answer += extend_arr(values)

print("Part 1", answer)

answer = 0
for line in lines:
    values = [int(a) for a in line.split(' ')]
    values = np.array(values, dtype=int)
    answer += extend_back(values)
    
print("Part 2", answer)
