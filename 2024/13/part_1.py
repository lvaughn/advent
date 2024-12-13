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

def get_cost(Ax, Ay, Bx, By, X, Y):
    possible_costs = []
    for na in range(100):
        needed_x = X - (na*Ax)
        if needed_x >= 0 and needed_x % Bx == 0:
            nb = needed_x // Bx 
            if Ay * na + By * nb == Y:
                cost = 3*na + nb 
                possible_costs.append(cost)
    if len(possible_costs) > 0:
        print(possible_costs)
        return min(possible_costs)          
    return 0

loc = 0
int_re = re.compile('(\d+)')
while loc < len(lines):
    ax, ay = [int(n) for n in int_re.findall(lines[loc])]
    bx, by = [int(n) for n in int_re.findall(lines[loc+1])]
    x, y = [int(n) for n in int_re.findall(lines[loc+2])]
    answer += get_cost(ax, ay, bx, by, x, y)
    loc += 4

print("Part 1", answer)
