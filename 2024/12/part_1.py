#!/usr/bin/env python3
import sys
import numpy as np
import re
from collections import Counter, defaultdict, deque, namedtuple
#from string import ascii_uppercase, ascii_lowercase, digits
#from itertools import count, product, permutations, combinations, combinations_with_replacement
#from sortedcontainers import SortedSet, SortedDict, SortedList
# from z3 import Solver, BitVec, Distinct
# from networkx import networkx as nx  
#import pprint


# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


answer = 0
answer_2 = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])

def find_region(row, col, board, visited) -> np.array:
    # print("Find region", row, col )
    region = np.zeros(visited.shape, dtype=bool)
    target = board[row][col]
    region[row, col] = True
    visited[row, col] = True 
    queue = deque([(row, col)])
    while len(queue) > 0:
        r, c = queue.popleft()
        # print(" Starting", r, c)
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            # print(f"  Trying {new_r}, {new_c}")
            if 0 <= new_r < width and 0 <= new_c < height:
                if not visited[new_r, new_c] and board[new_r][new_c] == target:
                    if not region[new_r, new_c]:
                        queue.append((new_r, new_c))
                    visited[new_r, new_c] = True
                    region[new_r, new_c] = True 
                    
    return region 
    
    
def get_perm_area(region):
    area = 0
    perimeter = 0
    for r in range(width):
        for c in range(height):
            if region[r, c]:
                area += 1
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if new_r == -1 or new_r == width or new_c == -1 or new_c == height:
                        perimeter += 1
                    else: 
                        if not region[new_r, new_c]:
                            perimeter += 1
    return perimeter, area 

def get_side_type(a, b):
    if a == b:
        return 0
    if a:
        return 1
    return 2

def get_n_sides(region):
    n_sides = 0
    scratch_rgn = np.zeros((width+2, height+2), dtype=bool)
    scratch_rgn[1:-1,1:-1] = region
    # by row
    for r in range(width+1):
        side_type = 0 
        for c in range(1, height+1):
            new_side_type = get_side_type(scratch_rgn[r,c], scratch_rgn[r+1,c])
            if new_side_type != side_type:
                if new_side_type > 0: 
                    n_sides += 1
            side_type = new_side_type
            
    for c in range(height+1):
        side_type = 0 
        for r in range(1, width+1):
            new_side_type = get_side_type(scratch_rgn[r,c], scratch_rgn[r,c+1])
            if new_side_type != side_type:
                if new_side_type > 0: 
                    n_sides += 1
            side_type = new_side_type   
    return n_sides      
                 

visited = np.zeros((width, height), dtype=bool)
for r in range(width):
    for c in range(height):
        if not visited[r, c]:
            rgn = find_region(r, c, lines, visited)
            perimeter, area = get_perm_area(rgn)
            answer += perimeter * area 
            n_sides = get_n_sides(rgn)
            answer_2 += area * n_sides

print("Part 1", answer)
print("Part 2", answer_2)

