#!/usr/bin/env python3
#from string import ascii_uppercase, ascii_lowercase, digits
#from collections import Counter, defaultdict, deque, namedtuple
#from itertools import count, product, permutations, combinations, combinations_with_replacement
#from sortedcontainers import SortedSet, SortedDict, SortedList
import numpy as np
#import re
#import pprint
import sys


# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
def get_adjacent(r, c, shape):
    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
        new_r = r + dr 
        new_c = c + dc 
        if 0 <= new_r < shape[0] and 0 <= new_c < shape[1]:
            yield new_r, new_c
    
height = len(lines)
width = len(lines[0])

start_r = start_c = 0
grid = np.zeros((height, width), dtype=int)
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == 'S':
            start_r = r 
            start_c = c
            grid[r, c] = 1
        elif ch == '#':
            grid[r,c] = 2 

for _ in range(64):
    new_grid = np.zeros(grid.shape, dtype=int)
    new_grid[grid == 2] = 2
    for r in range(height):
        for c in range(width):
            if grid[r, c] == 1:
                for new_r, new_c in get_adjacent(r, c, grid.shape):
                    if new_grid[new_r, new_c] != 2:
                        new_grid[new_r, new_c] = 1 
    grid = new_grid
    

print("Part 1", np.count_nonzero(grid == 1))
