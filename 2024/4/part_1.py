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

def xmases_at(r, c):
    if lines[r][c] != 'X':
        return 0
   
    total = 0
    if lines[r][c:].startswith("XMAS"):  # going right
        total += 1
    if c >= 3 and lines[r][c-3:].startswith("SAMX"): # Go left
        total += 1
    if r >= 3 and c >= 3 and lines[r-1][c-1] == "M" and \
        lines[r-2][c-2] == "A" and lines[r-3][c-3] == "S": #left and up
        total += 1 
    if r >= 3 and c <= width - 4 and lines[r-1][c+1] == "M" and \
        lines[r-2][c+2] == "A" and lines[r-3][c+3] == "S": # right and up
        total += 1
    if r >= 3 and lines[r-1][c] == "M" and lines[r-2][c] == "A" and \
        lines[r-3][c] == "S": # up
        total += 1
    if r <= height - 4 and lines[r+1][c] == "M" and lines[r+2][c] == "A" and \
        lines[r+3][c] == "S": # down
        total += 1
    if r <= height - 4 and c <= width - 4 and lines[r+1][c+1] == "M" and \
        lines[r+2][c+2] == "A" and lines[r+3][c+3] == "S": # down and right
        total += 1
    if r <= height - 4 and c >= 3 and lines[r+1][c-1] == "M" and \
        lines[r+2][c-2] == "A" and lines[r+3][c-3] == "S": # down and left
        total += 1
    # print(f"{r},{c}: {total}")
    return total 
        
    
for r in range(height):
    for c in range(width):
        answer += xmases_at(r, c)


print("Part 1", answer)
# 2884, 2453