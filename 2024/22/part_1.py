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

def next_secret(secret):
    secret = (secret ^ (secret * 64)) % 16777216 
    secret = (secret ^ (secret // 32)) % 16777216 
    secret = (secret ^ (secret * 2048)) % 16777216 
    return secret 
    
def make_gen(secret): 
    while True: 
        new_secret = next_secret(secret) 
        secret = new_secret
        yield secret    
        
def get_n(secret, n):
    for _ in range(n):
        secret = next_secret(secret)
    return secret 
    
answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])



for l in lines:
    answer += get_n(int(l), 2000)


print("Part 1", answer)
