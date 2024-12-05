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
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])


last_line = -1
following = defaultdict(list)
before = defaultdict(list)

for i, l in enumerate(lines):
    if l == "":
        last_line = i
        break 
    before, after = l.split('|')
    following[before].append(after)
    
# for k in following:
#     for v in following[k]:
#         before[v].append(k)
    
def is_valid(ls):
    for i, n in enumerate(ls):
        for j in ls[i+1:]:
            if n in following[j]:
                return False 
    return True 
    
for l in lines[last_line+1:]:
    values = l.split(',')
    if is_valid(values):
        assert len(values)%2 == 1
        answer += int(values[len(values)//2])
    

print("Part 1", answer)
# 11842

def fix_values(ls):
    for i in range(len(ls)-1):
        for j in range(i+1, len(ls)):
            if ls[i] in following[ls[j]]:
                ls[i], ls[j] = ls[j], ls[i]
            
    return ls 


answer = 0
for l in lines[last_line+1:]:
    values = l.split(',')
    if not is_valid(values):
        values = fix_values(values)
        assert len(values)%2 == 1
        answer += int(values[len(values)//2])

print("Part 2", answer)