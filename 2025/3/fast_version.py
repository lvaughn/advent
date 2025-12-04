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


with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

def add_number(input_num: str, digit: str):
    biggest_val = int(input_num)
    biggest_str = input_num
    for delete_digit in range(len(input_num)):
        new_str = input_num[0:delete_digit] + input_num[delete_digit+1:] + digit
        val = int(new_str)
        if val > biggest_val:
            biggest_val = val
            biggest_str = new_str
    return biggest_str
            
def get_best_joltage(input_num: str, size: int):
    start = input_num[:size]
    for new_digit in input_num[size:]:
        start = add_number(start, new_digit)
    return start           
            
answer_1 = 0
answer_2 = 0
for l in lines: 
    answer_1 += int(get_best_joltage(l, 2))
    answer_2 += int(get_best_joltage(l, 12))
    
print(f"Part 1 {answer_1}")
print(f"Part 2 {answer_2}")
