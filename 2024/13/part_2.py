#!/usr/bin/env python3
import sys
#import numpy as np
import re
#from collections import Counter, defaultdict, deque, namedtuple
#from string import ascii_uppercase, ascii_lowercase, digits
#from itertools import count, product, permutations, combinations, combinations_with_replacement
#from sortedcontainers import SortedSet, SortedDict, SortedList
# from z3 import Solver, BitVec
# from dataclasses import dataclass
# from networkx import networkx as nx  
#import pprint
import sympy as sym


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

def get_cost(Ax, Ay, Bx, By, X, Y):
    na, nb = sym.symbols('na nb')
    x_eqn = sym.Eq(Ax*na + Bx*nb, X)
    y_eqn = sym.Eq(Ay*na + By*nb, Y)
    sol = sym.solve([x_eqn, y_eqn], (na, nb))
    if isinstance(sol[na], sym.core.numbers.Integer) and \
        isinstance(sol[nb], sym.core.numbers.Integer):
        return 3 * sol[na] + sol[nb]
    return 0
        
    
    

loc = 0
int_re = re.compile('(\d+)')
while loc < len(lines):
    ax, ay = [int(n) for n in int_re.findall(lines[loc])]
    bx, by = [int(n) for n in int_re.findall(lines[loc+1])]
    x, y = [int(n) for n in int_re.findall(lines[loc+2])]
    answer += get_cost(ax, ay, bx, by, x+10000000000000, y+10000000000000)
    loc += 4

print("Part 2", answer)
# 2793657622064839119712
