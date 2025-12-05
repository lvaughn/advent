#!/usr/bin/env python3
import sys
#import numpy as np
import re
# from collections import Counter, defaultdict, deque, namedtuple
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

# directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])

dividing_line = lines.index('')
ranges = []
for l in lines[:dividing_line]:
    bottom, top = l.split('-')
    ranges.append((int(bottom), int(top)))
    
for l in lines[dividing_line+1:]:
    ing_id = int(l)
    for bottom, top in ranges:
        if bottom <= ing_id <= top:
            answer += 1
            break 
        
print("Part 1", answer)

ranges.sort()
n_ranges = len(ranges)
old_n_ranges = -1
while old_n_ranges != n_ranges:
    new_ranges = []
    old_n_ranges = n_ranges
    for r in ranges: 
        if len(new_ranges) == 0:
            new_ranges.append([r[0], r[1]])
        else: 
            if new_ranges[-1][1] >= r[0]:
                new_ranges[-1][0] = min(new_ranges[-1][0], r[0])
                new_ranges[-1][1] = max(new_ranges[-1][1], r[1])
            else: 
                new_ranges.append([r[0], r[1]])
    n_ranges = len(new_ranges)
    new_ranges.sort()
    ranges = new_ranges
    
    
part_2 = 0
for r in ranges: 
    part_2 += r[1] - r[0] + 1
    
print("Part 2", part_2)
