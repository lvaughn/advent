#!/usr/bin/env python3
import sys
#import numpy as np
import re
from collections import Counter, defaultdict, deque, namedtuple
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
    lines = [[int(a) for a in l.strip()] for l in infile]
height = len(lines)
width = len(lines[0])

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def find_all_9s(board, row, col): 
    locations = set()
    assert(board[row][col] == 0)
    queue = deque()
    queue.append((row, col, 0))
    while len(queue) > 0:
        r, c, h = queue.popleft()
        if h == 9:
            locations.add((r, c))
            continue
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc 
            if 0 <= new_r < width and 0 <= new_c < height and board[new_r][new_c] == h + 1:
                queue.append((new_r, new_c, h+1))
                
    return len(locations)

def find_all_trails(board, row, col): 
    n_trails = 0
    assert(board[row][col] == 0)
    queue = deque()
    queue.append((row, col, 0))
    while len(queue) > 0:
        r, c, h = queue.popleft()
        if h == 9:
            n_trails += 1
            continue
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc 
            if 0 <= new_r < width and 0 <= new_c < height and board[new_r][new_c] == h + 1:
                queue.append((new_r, new_c, h+1))
    return n_trails 
                
for r in range(width):
    for c in range(height):
        if lines[r][c] == 0:
            answer += find_all_9s(lines, r, c)
            
print("Part 1", answer)

answer = 0
for r in range(width):
    for c in range(height):
        if lines[r][c] == 0:
            answer += find_all_trails(lines, r, c)
print("Part 2", answer)