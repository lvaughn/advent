#!/usr/bin/env python3
import sys
#import numpy as np
import re
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

# directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def match(lock, key):
    for l, k in zip(lock, key):
        if l+k> 5:
            return False 
    return True 

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])

keys = []
locks = []

pos = 0
while pos < height:
    assert lines[pos] != ''
    if lines[pos][0] == '.': # Key
        key = [5] * 5
        for line in lines[pos+1:pos+6]:
            for i, ch in enumerate(line):
                if ch == '.':
                    key[i] -= 1
        keys.append(key) 
    else: # Lock
        lock = [0] * 5
        for line in lines[pos+1:pos+6]:
            for i, ch in enumerate(line):
                if ch == '#':
                    lock[i] += 1
        locks.append(lock)
    pos += 8
    
for l in locks:
    for k in keys: 
        if match(l, k):
            answer += 1

print("Part 1", answer)
