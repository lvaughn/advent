#!/usr/bin/env python3
import sys
#import numpy as np
import re
from collections import Counter, defaultdict, deque, namedtuple
# from string import ascii_uppercase, ascii_lowercase, digits
# from itertools import count, product, permutations, combinations, combinations_with_replacement
# from sortedcontainers import SortedSet, SortedDict, SortedList
# from z3 import Solver, BitVec, Distinct
# from networkx import networkx as nx  
# import pprint
# import sympy as sym
# from functools import cache


# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])

def find_route(start, end):
    # loc, path:
    queue = deque()
    queue.append((start, [start]))
    while len(queue) > 0:
        loc, path_so_far = queue.popleft()
        if loc == end:
            return path_so_far
        
        for dr, dc in directions:
            new_r, new_c = loc[0] + dr, loc[1]+dc 
            if (new_r, new_c) in path_so_far:
                continue 
            if 0 <= new_r < height and 0 <= new_c < width and lines[new_r][new_c] != '#':
                queue.append(((new_r, new_c), path_so_far + [(new_r, new_c)]))
            
for r, l in enumerate(lines):
    for c, ch in enumerate(l):
        if ch == 'S':
            start_loc = (r, c)
        elif ch == 'E':
            end_loc = (r, c) 
        
non_cheat_len = None
n_better_than = Counter()
needed_diff = 50
normal_route = find_route(start_loc, end_loc)

for loc, pt in enumerate(normal_route[:-1]):
    row, col = pt
    for new_loc, end_pt in enumerate(normal_route[loc+1:]):
        r, c = end_pt
        man_dist = abs(row - r) + abs(col - c)
        if man_dist <= 20:
            savings = new_loc + 1 - man_dist
            # print(f"Found {savings} from {pt} to {end_pt} loc={loc},new_loc={new_loc}")
            if savings >= needed_diff:
                n_better_than[savings] += 1
       
answer = 0     
for save, n in n_better_than.items():
    if save >= 100:
        answer += n         
        
print("Part 2", answer)
