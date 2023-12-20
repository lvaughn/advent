#!/usr/bin/env python3
#from string import ascii_uppercase, ascii_lowercase, digits
from collections import Counter, defaultdict, deque, namedtuple
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

def flood_fill(grid, x, y):
    queue = deque()
    queue.append((x, y))
    while len(queue) > 0:
        x, y = queue.popleft()
        assert 0 <= x < grid.shape[0]
        assert 0 <= y < grid.shape[1]
        if grid[x, y] == 1:
            continue 
        grid[x, y] = 1
        if grid[x+1, y] == 0:
            queue.append((x+1, y))
        if grid[x-1, y] == 0:
            queue.append((x-1, y))
        if grid[x, y+1] == 0:
            queue.append((x, y+1))
        if grid[x, y-1] == 0:
            queue.append((x, y-1))

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
SIZE = 1000
start_x, start_y = x, y = SIZE//2, SIZE//2

grid = np.zeros((SIZE, SIZE), dtype=int)
grid[x, y] = 1
for l in lines:
    dir, amount, color = l.split(' ')
    amount = int(amount)
    if dir == 'L':
        x_start = x-amount 
        grid[x_start:x+1, y] = 1
        x = x_start
    elif dir == 'R': 
        x_end = x+amount
        grid[x:x_end+1, y] = 1
        x = x_end 
    elif dir == 'U':
        y_start = y - amount 
        grid[x, y_start:y+1] = 1
        y = y_start
    elif dir == 'D':
        y_end = y + amount 
        grid[x, y:y_end+1] = 1
        y = y_end 
        

flood_fill(grid, start_x - 4, start_y + 1)

print("Part 1", np.count_nonzero(grid))
