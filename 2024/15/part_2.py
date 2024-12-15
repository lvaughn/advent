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

def all_space(board, dr, to_move):
    for r, c in to_move:
        if (r+dr, c) in to_move:
            continue # We can ignore stuff already in the set
        if board[r+dr, c] != 0:
            return False 
    return True 

def any_wall(board, dr, to_move):
    for r, c in to_move:
        if board[r+dr, c] == 1:
            return True 
    return False 

def do_move(board, ch, robot_loc) -> tuple:
    dr, dc = directions[ch]
    
    if ch in ['<', '>']: # Left/Right works like part 1
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
        cell_type = 0
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
        assert(False)
     
    # Now have to do up/down
    # See if we can move, build up a set of places we need to move
    r, c = robot_loc
    to_move = set()
    to_move.add(robot_loc)
    while True: 
        if all_space(board, dr, to_move):
            can_move = True 
            break
        if any_wall(board, dr, to_move):
            return robot_loc # We can't move
        # Figure out what what moves now
        new_to_move = set()
        for r, c in to_move:
            new_to_move.add((r, c))
            assert board[r+dr, c] != 1
            if board[r+dr, c] == 2:
                new_to_move.add((r+dr, c))
                new_to_move.add((r+dr, c+1))
            if board[r+dr, c] == 3:
                new_to_move.add((r+dr, c))
                new_to_move.add((r+dr, c-1))
        to_move = new_to_move
                
    assert can_move
    
    # Do the move
    new_data  = {}
    for r, c in to_move:
        new_data[(r, c)] = board[r, c]
    for r, c in to_move:
        board[r, c] = 0
    for r, c in new_data:
        assert board[r+dr, c] == 0
        board[r+dr, c] = new_data[(r, c)]
    
    return (robot_loc[0]+dr, robot_loc[1]+dc)

def print_board(board, robot_loc):
    for r in range(board.shape[0]):
        s = ''
        for c in range(board.shape[1]):
            if (r, c) == robot_loc:
                s += '@'
            elif board[r, c] == 0:
                s += '.'
            elif board[r, c] == 1:
                s += '#'
            elif board[r, c] == 2:
                s += '['
            elif board[r, c] == 3:
                s += ']'
            else:
                assert(false)
        print(s)

         
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
# 2 = left_box
# 3 = right_box

board = np.zeros((break_line, 2*width), dtype=int)
for r, l in enumerate(board_lines):
    for c, ch in enumerate(l):
        if ch == '#':
            board[r, 2*c] = 1
            board[r, 2*c+1] = 1
        elif ch == 'O':
            board[r, 2*c] = 2
            board[r, 2*c+1] = 3
        elif ch == '@':
            robot_location = (r, 2*c)
        else:
            assert ch == '.'

# print_board(board, robot_location)
for m in moves:
    robot_location = do_move(board, m, robot_location)
    # print("Move", m)
    # print_board(board, robot_location)
    
for r in range(board.shape[0]):
    for c in range(board.shape[1]):
        if board[r, c] == 2:
            answer += 100*r + c

print("Part 2", answer)
# 1320569 too low
