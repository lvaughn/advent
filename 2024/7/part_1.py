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

def can_reach(target, values):
    def helper(values, results):
        if len(values) == 1:
            return results.add(values[0])
        helper([values[0] + values[1]] + values[2:], results)
        helper([values[0] * values[1]] + values[2:], results)
    possibles = set()
    helper(values, possibles)
    return target in possibles
        
    
def can_reach_part_2(target, values):
    def helper(values, results):
        if values[0] > target:
            return 
        if len(values) == 1:
            return results.add(values[0])
        helper([values[0] + values[1]] + values[2:], results)
        helper([values[0] * values[1]] + values[2:], results)
        helper([int(str(values[0]) + str(values[1]))] + values[2:], results)
    possibles = set()
    helper(values, possibles)
    return target in possibles

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])

eqn = []
for l in lines:
    target, values = l.split(':')
    eqn.append((int(target), [int(x) for x in values.split()]))
    
for target, values in eqn:
    if can_reach(target, values):
        answer += target 


print("Part 1", answer)

answer = 0
for target, values in eqn:
    if can_reach_part_2(target, values):
        answer += target 
        
print("Part 2", answer)