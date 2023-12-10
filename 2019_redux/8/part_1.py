#!/usr/bin/env python3

import numpy as np
import sys


with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
answer = 0

n_numbers = len(lines[0])
width = 25
height = 6
depth = n_numbers // (width * height)
assert n_numbers % (width * height) == 0

values = [int(a) for a in lines[0]]
arr = np.array(values, dtype=int)
image = arr.reshape((depth, height, width))

fewest_zeros = width * height * depth + 1
for layer in range(depth):
    values, counts = np.unique(image[layer, :, :], return_counts=True)
    if counts[0] < fewest_zeros:
        fewest_zeros = counts[0]
        answer = counts[1] * counts[2]
        
print("Part 1", answer) 

def get_pixel(grid, r, c):
    for d in range(depth):
        if grid[d, r, c] != 2:
            return grid[d, r, c]
    assert False
    
answer = np.zeros((width, height), dtype=int)
for c in range(width):
    for r in range(height):
        answer[c, r] = get_pixel(image, r, c)
        
print("Part 2")
for r in range(height):
    s = ""
    for c in range(width):
        if answer[c, r] == 0:
            s += " "
        else:
            s += "*"
    print(s)