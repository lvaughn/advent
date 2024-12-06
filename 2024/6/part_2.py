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
# print(height, width)

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
            board[r, c] = 0
# print(board)

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def loops(board, row, col, dir):
    blocks_seen = set()
    while 0 <= row < height and 0 <= col < width:
        dr, dc = moves[dir]
        new_row = row + dr
        new_col = col + dc 
        if 0 <= new_row < height and 0 <= new_col < width:
            ch = board[new_row, new_col]
            if ch == 100:
                key = (row, col, dir)
                if key in blocks_seen:
                    return True 
                blocks_seen.add(key)
                dir = (dir + 1) % 4
            else:
                row = new_row
                col = new_col 
        else:
            # print("Off the end", new_row, new_col)
            row = new_row
            col = new_col     
    return False       

b = board.copy()
b[6, 3] = 100
loops(b, row, col, dir)

print("Start", row, col, dir)
for r in range(height):
    for c in range(width):
        if r != row or c != col:
            b = board.copy()
            b[r, c] = 100
            if loops(b, row, col, dir):
                answer += 1 
    
print("Part 2", answer)
# 16641, 1578 
