#!/usr/bin/env python3
import sys
#import numpy as np
import re
#from collections import Counter, defaultdict, deque, namedtuple
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

answer = 0

with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])

def is_xmas(r, c):
    if r == 0 or c == 0 or r == height - 1 or c == width - 1:
        return 0
   
    if lines[r][c] != "A":
        return 0
    if (lines[r-1][c-1] == "M" and lines[r+1][c+1] == "S") or \
        (lines[r-1][c-1] == "S" and lines[r+1][c+1] == "M"):
        if (lines[r-1][c+1] == "M" and lines[r+1][c-1] == "S") or \
            (lines[r-1][c+1] == "S" and lines[r+1][c-1] == "M"):
            return 1
    return 0
        
    
for r in range(height):
    for c in range(width):
        answer += is_xmas(r, c)

print("Part 1", answer)
