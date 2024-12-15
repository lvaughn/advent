#!/usr/bin/env python3
import sys
import numpy as np
#import re
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
#
# directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

def do_move(board, ch, robot_loc) -> tuple:
    dr, dc = directions[ch]
    
    # See if we can move
    r, c = robot_loc
    can_move = False
    while True:
        r += dr
        c += dc
        if board[r, c] == 0: # a space to move in to 
            can_move = True
            break
        if board[r, c] == 1: # Wall
            return robot_loc # can't move
    assert can_move
    
    # Do the move
    r, c = robot_loc
    cell_type = 3
    board[r, c] = 0
    while True:
        next_r, next_c = r + dr, c + dc
        next_cell_type = board[next_r, next_c]
        board[next_r, next_c] = cell_type
        if next_cell_type == 0:
            return (robot_loc[0]+dr, robot_loc[1] + dc)
        cell_type = next_cell_type
        r = next_r
        c = next_c
        
    
        
answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])
for i, l in enumerate(lines):
    if l == "":
        break_line = i
board_lines = lines[:break_line]
moves = "".join(lines[break_line+1:])

# Make board 
# 0 = empty
# 1 = wall
# 2 = box
# 3 = robot

board = np.zeros((break_line, width), dtype=int)
for r, l in enumerate(board_lines):
    for c, ch in enumerate(l):
        if ch == '#':
            board[r, c] = 1
        elif ch == 'O':
            board[r, c] = 2
        elif ch == '@':
            board[r, c] = 3
            robot_location = (r, c)
        else:
            assert ch == '.'

for m in moves:
    robot_location = do_move(board, m, robot_location)
    
for r in range(board.shape[0]):
    for c in range(board.shape[1]):
        if board[r, c] == 2:
            answer += 100*r + c

print("Part 1", answer)
