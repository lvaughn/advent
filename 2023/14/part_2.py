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

def move_to_north(grid):
    row, cols = grid.shape
    for r in range(row):
        for c in range(cols):
            if grid[r, c] != 1:
                continue 
            current_r = r 
            while (current_r >= 1) and grid[current_r-1, c] == 0:
                grid[current_r-1, c] = 1
                grid[current_r, c] = 0
                current_r -= 1
                
def move_to_south(grid):
    rows, cols = grid.shape
    for r in range(rows-1, -1, -1):
        for c in range(cols):
            if grid[r, c] != 1:
                continue 
            current_r = r 
            while (current_r < rows -1) and grid[current_r+1, c] == 0:
                grid[current_r+1, c] = 1
                grid[current_r, c] = 0
                current_r += 1          
                
def move_to_west(grid):
    rows, cols = grid.shape
    for c in range(cols):
        for r in range(rows):
            if grid[r, c] != 1:
                continue
            current_c = c 
            while (current_c >= 1) and grid[r, current_c - 1] == 0:
                grid[r, current_c - 1] = 1
                grid[r, current_c] = 0
                current_c -= 1
 
def move_to_east(grid):
    rows, cols = grid.shape
    for c in range(cols-1, -1, -1):
        for r in range(rows):
            if grid[r, c] != 1:
                continue
            current_c = c 
            while (current_c < rows - 1) and grid[r, current_c + 1] == 0:
                grid[r, current_c + 1] = 1
                grid[r, current_c] = 0
                current_c += 1               
                
        
        
def spin_cycle(grid):
    move_to_north(grid)
    move_to_west(grid)
    move_to_south(grid)
    move_to_east(grid)
    
        
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
loads = [get_north_load(grid)]
while True:
    spin_cycle(grid)
    loads.append(get_north_load(grid))
    
    # See if we have a cycle
    cycle_len = None
    for possible_cycle in range(1, len(loads) // 5):
        a = len(loads) - 1
        b = a - possible_cycle
        c = b - possible_cycle
        if loads[a] == loads[b] and loads[b] == loads[c]:
            cycle_len = possible_cycle
            break 
    if cycle_len is not None:
        break 

        
cycle_array = np.array(loads, dtype=int)

print("Looking for a cycle")
base_loc = len(cycle_array) - 2 * cycle_len


print("Cycle length", cycle_len)

TARGET = 1000000000
mod_value = (TARGET - base_loc) % cycle_len
n = base_loc
while (TARGET - n) % cycle_len != 0:
    n += 1

print("Part 2", cycle_array[n])


