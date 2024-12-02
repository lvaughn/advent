#!/usr/bin/env python3
import sys
import numpy as np
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

with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])

answer = 0

def test_values(values):
    diffs =  values[1:] - values[:-1]
    if not (all(diffs < 0) or all(diffs>0)):
        return False
    diffs = abs(diffs)
    if (diffs < 1).any():
        return False 
    if (diffs > 3).any():
        return False 
    return True 
    
for l in lines:
    values = np.array([int(x) for x in l.split()], dtype=int)
    if test_values(values):
        answer += 1

print("Part 1", answer)

answer = 0
for l in lines:
    numbers = [int(x) for x in l.split()]
    if test_values(np.array(numbers, dtype=int)):
        answer += 1
    else:
        for loc in range(len(numbers)):
            new_numbers = numbers[:loc] + numbers[loc+1:]
            values = np.array(new_numbers, dtype=int)
            if test_values(values):
                answer += 1
                break
    
print("Part 2", answer)
