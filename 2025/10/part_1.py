#!/usr/bin/env python3
import sys
from collections import Counter, defaultdict, deque, namedtuple
# from string import ascii_uppercase, ascii_lowercase, digits
# from itertools import count, product, permutations, combinations, combinations_with_replacement
# from sortedcontainers import SortedSet, SortedDict, SortedList
# from z3 import Solver, BitVec, Distinct
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

def apply_button(start: tuple[int], button: list[int]) -> tuple[int]:
    result = []
    for i, num in enumerate(start):
        if i in button:
            result.append(1 - num)
        else: 
            result.append(num)
    return tuple(result)

def find_shortest_path(goal: tuple[int], buttons: list[list[int]]) -> int:
    queue = deque()
    queue.append((tuple([0] * len(goal)), 0))
    visited = set()
    while len(queue) > 0:
        current_state, so_far = queue.popleft()
        if current_state in visited:
            continue 
        visited.add(current_state)
        for b in buttons:
            new_state = apply_button(current_state, b)
            # print(current_state, so_far, b, new_state)
            if new_state == goal:
                return so_far + 1
            queue.append((new_state, so_far + 1))
    assert False 
    

for l in lines: 
    right_bracket = l.index(']')
    lights = tuple([{'.':0, '#': 1}[ch] for ch in l[1:right_bracket]])
    joltage_start = l.index('{')
    buttons = re.findall(r'\(([\d,]+)\)', l[right_bracket+1:joltage_start])
    button_ints = [[int(a) for a in b.split(',')] for b in buttons]
    answer += find_shortest_path(lights, button_ints)

print("Part 1", answer)
