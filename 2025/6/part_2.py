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
# from intervaltree import IntervalTree
# import pprint
# import sympy as sym
# from functools import cache
 

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

def all_spaces(loc):
    for l in lines[:-1]:
        if l[loc] != ' ':
            return False 
    return True 

def get_number(loc):
    val = ''
    for l in lines[:-1]:
        if l[loc] != ' ':
            val += l[loc]
    return int(val)

def get_result(op, nums):
    if op == '+':
        return sum(nums)
    else:
        assert op == '*'
        val = 1
        for n in nums:
            val *= n 
        return val 
            
op = None
numbers = []
for i in range(width):
    # print(i, ch)
    if i >= len(lines[-1]):
        ch = ' ' # We're off the end of the array
    else: 
        ch = lines[-1][i]
    if all_spaces(i):
        assert ch == ' '
        answer += get_result(op, numbers) 
    elif ch != ' ':
        op = ch 
        numbers = [get_number(i)]
    else:
        numbers.append(get_number(i))
        
answer += get_result(op, numbers) 

print("Part 2:", answer)
