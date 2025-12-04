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
from functools import cache


# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

# directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])

@cache
def max_for_line(l):
    result = -1
    for i in range(len(l)-2):
        for j in range(i+1, len(l)-1):
            val = 100*l[i]+10*l[j]+max(l[j+1:])
            result = max(result, val)
            if result == 999:
                return 999
    # print("        Max", result, l)
    return result 

@cache            
def max_6_for_line(l):
    result = -1
    best_first_half = -1
    for break_point in range(3, len(l) - 2):
        # print("  bp", break_point)
        first_half = max_for_line(tuple(l[:break_point]))
        if first_half > best_first_half:
            val = 1000 * first_half + max_for_line(tuple(l[break_point:]))   
            result = max(val, result)
            best_first_half = first_half
            if best_first_half == 999:
                return result # That's the best we're going to do
    # print("  Max 6:", result, l)
    return result 

def max_12_for_line(l):
    result = -1
    best_first_half = -1
    # print("Max 12", l)
    for break_point in range(6, len(l) - 5):
        # print(break_point)
        first_half = max_6_for_line(tuple(l[:break_point]))
        if first_half > best_first_half:
            val = 1000000 * first_half + max_6_for_line(tuple(l[break_point:]))   
            result = max(val, result)
            best_first_half = first_half
            if best_first_half == 999999:
                return result # That's the best we're going to do
    # print(result)
    return result              
            
answer = sum(max_12_for_line([int(a) for a in l]) for l in lines)
print("Part 2", answer)
# 176188773151005