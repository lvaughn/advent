#!/usr/bin/env python3
import sys
import numpy as np
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

board = np.zeros((height, width), dtype=int)


dir_decode = {'^': 0, '>': 1, 'v': 2, '<': 3}
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == '#':
            board[r, c] = 100
        elif ch == '.':
            pass 
        else:
            row = r
            col = c
            dir = dir_decode[ch]
            board[r, c] = 1

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
while 0 <= row < height and 0 <= col < width:
    board[row, col] = 1
    dr, dc = moves[dir]
    new_row = row + dr
    new_col = col + dc 
    if 0 <= new_row < height and 0 <= new_col < width:
        ch = board[new_row, new_col]
        if ch == 100:
            dir = (dir + 1) % 4
        else:
            row = new_row
            col = new_col 
    else:
        row = new_row
        col = new_col           


unique, counts = np.unique(board, return_counts=True)
counts = dict(zip(unique, counts))
answer = counts[1]
print("Part 1", answer)
