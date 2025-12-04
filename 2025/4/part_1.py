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

for r in range(height):
    for c in range(width):
        if lines[r][c] != '@':
            continue 
        adj = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                new_r = r + dr 
                new_c = c + dc
                if 0 <= new_r < height and 0 <= new_c < width: 
                    if lines[new_r][new_c] == '@':
                        adj += 1
        if adj <= 4: # add 1 for the roll in the center
            answer += 1
                


print("Part 1", answer)
