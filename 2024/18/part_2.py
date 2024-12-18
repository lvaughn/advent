#!/usr/bin/env python3
import sys
import numpy as np
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
    
def is_reachable(board):
    queue = deque()
    queue.append((0, 0, 0))
    visited = set()
    visited.add((0, 0))
    while len(queue):
        row, col, length = queue.popleft()
        if row == 70 and col == 70:
            return True 
        for dr, dc in directions:
            new_r = row + dr
            new_c = col + dc 
            if 0 <= new_r < 71 and 0 <= new_c < 71 and board[new_r, new_c] == 0 and (new_r, new_c) not in visited:
                visited.add((new_r, new_c))
                queue.append((new_r, new_c, length+1))
    return False 

board = np.zeros((71, 71), dtype=int)
for l in lines:
    r, c = [int(n) for n in l.split(",")]
    board[r, c] = 1
    if not is_reachable(board):
        answer = f"{r},{c}"
        break 
    
print("Part 2", answer)
