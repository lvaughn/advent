#!/usr/bin/env python3
import sys
#import numpy as np
import re
import heapq 
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

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

facing_dirs = ['e', 'n', 'w', 's']

moves = {
    'e': (0, 1),
    'n': (-1, 0),
    'w': (0, -1),
    's': (1, 0)
}

def shortest_path(board, start_point, end_point):
    visited = set()
    
    # Score, location, facing
    queue = [(0, start_point, 0)]
    heapq.heapify(queue)
    while len(queue) > 0:
        points, loc, facing = heapq.heappop(queue)
        if (loc, facing) in visited: 
            continue 
        visited.add((loc, facing))
        if loc == end_point:
            return points 
        # We can turn
        left_turn = (facing - 1) % 4
        # print(loc, left_turn)
        if (loc, left_turn) not in visited:
            heapq.heappush(queue, (points+1000, loc, left_turn))
            
        right_turn = (facing + 1) % 4
        # print(loc, right_turn)
        if (loc, right_turn) not in visited:
            heapq.heappush(queue, (points+1000, loc, right_turn))
            
        # We can (maybe) move one forward 
        dr, dc = moves[facing_dirs[facing]]
        r, c = loc 
        new_r = r + dr 
        new_c = c + dc
        if board[new_r][new_c] != "#":
            new_loc = new_r, new_c 
            if (new_loc, facing) not in visited:
                heapq.heappush(queue, (points + 1, new_loc, facing))
                
        # print(queue)
    assert False 
        
        
answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])

for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == 'S':
            start_loc = r, c 
        elif ch == 'E':
            end_loc = r, c 
            
answer = shortest_path(lines, start_loc, end_loc)


print("Part 1", answer)
