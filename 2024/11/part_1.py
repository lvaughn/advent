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
stones = [int(x) for x in lines[0].split()]

def process_stone(n):
    if n == 0:
        return [1]
    s = str(n)
    if len(s) % 2 == 0:
        split_pt = len(s) // 2
        return [int(s[:split_pt]), int(s[split_pt:])]
    return [n * 2024]
        
CACHE = {}
def turns_in_to(n, rounds):
    if rounds == 0:
        return 1
    key = (n, rounds)
    if key not in CACHE:
        total = 0
        for x in process_stone(n):
            total += turns_in_to(x, rounds - 1)
        CACHE[key] = total 
    return CACHE[key]

for s in stones:
    answer += turns_in_to(s, 25)

print("Part 1", answer)

answer = 0
for s in stones:
    answer += turns_in_to(s, 75)
print("Part 2", answer)