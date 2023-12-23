#!/usr/bin/env python3
#from string import ascii_uppercase, ascii_lowercase, digits
from collections import Counter, defaultdict, deque, namedtuple
#from itertools import count, product, permutations, combinations, combinations_with_replacement
#from sortedcontainers import SortedSet, SortedDict, SortedList
#import numpy as np
#import re
#import pprint
import sys


# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
height = len(lines)
width = len(lines[1])    
start = (0, 1)
end = (height-1, width-2)

def next_moves(row, col, current_value):
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if current_value == '<' and (dr, dc) != (0, -1):
            continue
        if current_value == '>' and (dr, dc) != (0, 1):
            continue
        if current_value == 'v' and (dr, dc) != (1, 0):
            continue
        if current_value == '^' and (dr, dc) != (-1, 0):
            continue
        new_r, new_c = row+dr, col + dc 
        if new_r < 0 or new_r >= height:
            continue 
        if new_c < 0 or new_c >= width:
            continue
        yield (new_r, new_c)

path = [start]
queue = deque([path])
longest_so_far = -1
while len(queue) > 0:
    path = queue.popleft()
    # print(path)
    loc = path[-1]
    if loc == end:
        if len(path) > longest_so_far:
            longest_so_far = len(path)
            print(f"{longest_so_far}: {path}")
        continue 
    for new_r, new_c in next_moves(loc[0], loc[1], lines[loc[0]][loc[1]]):
        if lines[new_r][new_c] != '#' and (new_r, new_c) not in path:
            new_path = path + [(new_r, new_c)]
            queue.append(new_path)
    

print("Part 1", longest_so_far - 1)
# 2439