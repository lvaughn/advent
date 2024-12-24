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

class Gate:
    def __init__(self, func, id, a, b):
        self.a = a
        self.b = b 
        self.id = id 
        self.func = func 
        
    def eval(self, vars):
        if vars[self.a] is None or vars[self.b] is None:
            return None 
        if self.func == 'OR':
            return vars[self.a] or vars[self.b] 
        if self.func == 'XOR': 
            return vars[self.a] ^ vars[self.b]
        if self.func == 'AND':
            return vars[self.a] and vars[self.b]
        assert False, f"Bad func {self.func}"
        
def zs_set(vars):
    for k in vars:
        if k.startswith('z') and vars[k] is None:
            return False 
    return True 

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])

vars = {}
for no, l in enumerate(lines):
    if l == '':
        funcs_start = no+1
        break 
    var, value = l.split(':')
    if value.strip() == '1':
        vars[var] = True 
    else:
        vars[var] = False 
    
func_re = re.compile(r'(\S+) (\S+) (\S+) -> (\S+)')
gates = {}
for l in lines[funcs_start:]:
    m = func_re.match(l)
    f = Gate(m[2], m[4], m[1], m[3])
    gates[m[4]] = f 
    vars[m[4]] = None
    
while not zs_set(vars):
    for output in gates:
        if vars[output] is None:
            vars[output] = gates[output].eval(vars)
            

z_vars = [v for v in vars if v.startswith('z')]
z_vars.sort(reverse=True)
for v in z_vars:
    answer *= 2
    if vars[v]:
        answer += 1
    

print("Part 1", answer)
# 28445656832885