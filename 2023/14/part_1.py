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

def move_to_top(grid, r, c):
    if grid[r, c] != 1:
        return 
    while r >= 1 and grid[r-1, c] == 0:
        grid[r-1, c] = 1
        grid[r, c] = 0
        r -= 1
        
def get_north_load(grid):
    answer = 0
    rows, cols = grid.shape
    for r in range(rows):
        points = rows - r 
        for c in range(cols):
            if grid[r, c] == 1:
                answer += points
    return answer


with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
rows = len(lines)
cols = len(lines[0])

grid = np.zeros((rows, cols), dtype=int)

for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == '#':
            grid[r, c] = 2
        elif ch == 'O':
            grid[r, c] = 1
            
# Move everyting up "north"
for r in range(rows):
    for c in range(cols):
        move_to_top(grid, r, c)
        

print("Part 1", get_north_load(grid))
