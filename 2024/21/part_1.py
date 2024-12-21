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
import pprint
# import sympy as sym
from functools import cache


# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

# directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

@cache 
def numeric_paths(start, end):
    locations = {
        '7': (0, 0),
        '8': (0, 1),
        '9': (0, 2),
        '4': (1, 0),
        '5': (1, 1),
        '6': (1, 2),
        '1': (2, 0),
        '2': (2, 1),
        '3': (2, 2),
        ' ': (3, 0),
        '0': (3, 1),
        'A': (3, 2),
    }
    
    end_loc = locations[end]
    end_r, end_c = end_loc
    paths = []
    queue = deque()
    queue.append((locations[start], []))
    while len(queue) > 0: 
        loc, path = queue.popleft()
        if loc == end_loc:
            paths.append(path + ['A'])
            continue 
        if loc == locations[' ']:
            continue # avoid this cell 
        r, c = loc 
        if r > end_r:
            queue.append(((r-1, c), path + ['^']))
        if r < end_r:
            queue.append(((r+1, c), path + ['v']))
        if c > end_c: 
            queue.append(((r, c-1), path + ['<']))
        if c < end_c: 
            queue.append(((r, c+1), path + ['>']))
    return paths 

def all_numeric_paths(path):
    loc = 'A'
    paths = [[]]
    for dest in path: 
        new_paths = []
        for p in numeric_paths(loc, dest):
            for old_p in paths:
                new_paths.append(old_p + p)
        loc = dest 
        paths = new_paths
    return paths 

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

@cache
def direction_paths(start, end):
    locations = {
        ' ': (0, 0),
        '^': (0, 1),
        'A': (0, 2),
        '<': (1, 0),
        'v': (1, 1),
        '>': (1, 2)
    }
    end_loc = locations[end]
    end_r, end_c = end_loc
    paths = []
    queue = deque()
    queue.append((locations[start], []))
    while len(queue) > 0: 
        loc, path = queue.popleft()
        if loc == end_loc:
            paths.append(path + ['A'])
            continue 
        if loc == locations[' ']:
            continue # avoid this cell 
        r, c = loc 
        if r > end_r:
            queue.append(((r-1, c), path + ['^']))
        if r < end_r:
            queue.append(((r+1, c), path + ['v']))
        if c > end_c: 
            queue.append(((r, c-1), path + ['<']))
        if c < end_c: 
            queue.append(((r, c+1), path + ['>']))
    return paths 
 
def all_direction_paths(path):
    loc = 'A'
    paths = [[]]
    for dest in path: 
        new_paths = []
        for p in direction_paths(loc, dest):
            for old_p in paths:
                new_paths.append(old_p + p)
        loc = dest 
        paths = new_paths
    return paths   
    
def all_paths(code):
    start_path = [str(a) for a in code]
    # print(start_path)
    for n_path in all_numeric_paths(start_path):
        # print("  ", n_path)
        for d1_path in all_direction_paths(n_path):
            # print("       ", d1_path)
            for d2_path in all_direction_paths(d1_path):
                yield(d2_path)
                # print("          ", d2_path)
    
    
answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])

for l in lines:
    print(l)
    shortest_path = None
    for p in all_paths(l):
        if shortest_path is None or len(p) < len(shortest_path):
            shortest_path = p 
    path_len = len(shortest_path)
    mult = int(l[:-1])
    answer += mult * path_len
print("Part 1", answer)
