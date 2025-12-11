#!/usr/bin/env python3
import sys
from collections import Counter, defaultdict, deque, namedtuple
# from string import ascii_uppercase, ascii_lowercase, digits
# from itertools import count, product, permutations, combinations, combinations_with_replacement
# from sortedcontainers import SortedSet, SortedDict, SortedList
from z3 import Int, Sum, sat, Optimize
# from networkx import networkx as nx  
# import sympy as sym
# from intervaltree import IntervalTree

# import pprint
# from functools import cache
# import numpy as np
import re

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

def n_presses(joltages, buttons) -> int:
    opt = Optimize()
    n_buttons = len(buttons)
    n_presses = [Int(f"n_presses_{i}") for i in range(n_buttons)]
    for np in n_presses:
        opt.add(np >= 0)
    for i, joltage_value in enumerate(joltages):
        presses = []
        for button_no, button in enumerate(buttons):
            if i in button:
                presses.append(n_presses[button_no])
        opt.add(Sum(presses) == joltage_value)
    total_presses = Int('total_presses')
    opt.add(Sum(n_presses) == total_presses)
    opt.minimize(total_presses)
    if opt.check() == sat:
        m = opt.model()
        value = m[total_presses]
        return value.as_long()
    else:
        print(buttons, joltages)
        assert False 
    

for l in lines: 
    right_bracket = l.index(']')
    # lights = tuple([{'.':0, '#': 1}[ch] for ch in l[1:right_bracket]])
    joltage_start = l.index('{')
    buttons = re.findall(r'\(([\d,]+)\)', l[right_bracket+1:joltage_start])
    button_ints = [[int(a) for a in b.split(',')] for b in buttons]
    joltage_end = l.index('}')
    joltages = [int(j) for j in l[joltage_start+1:joltage_end].split(",")]
    answer += n_presses(tuple(joltages), button_ints)
    # print(answer)

print("Part 2", answer)

