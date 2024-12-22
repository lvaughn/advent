#!/usr/bin/env python3
import sys
import numpy as np
# import re
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
    
def get_n(secret, n):
    for _ in range(n):
        secret = next_secret(secret)
    return secret 
    
    
def gen_2k(secret):
    result = [secret % 10]
    for _ in range(2000):
        secret = next_secret(secret)
        result.append(secret % 10)
    return result 

def get_diffs(values):
    v = np.array(values, dtype=np.int8) 
    diffs = np.zeros(v.shape, dtype=np.int8)
    diffs[1:] = v[1:] - v[:-1]
    return diffs 

def make_lookup_table(values, diffs):
    result = {}
    for i in range(len(diffs) - 4):
        key = tuple(diffs[i:i+4])
        if key not in result:
            result[key] = values[i+3]
    return result 

with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])


values = []
diffs = []
tables = []
best = -99999999
print("Generating prices")
for l in lines:
    values.append(gen_2k(int(l)))
    diffs.append(get_diffs(values[-1]))
    tables.append(make_lookup_table(values[-1], diffs[-1]))
    
print("Finding best")
tried = set()
for table in tables:
    for seq, value in table.items():
        if seq not in tried: 
            tried.add(seq)
            total = 0
            for t in tables: 
                total += t.get(seq, 0)
            if total > best: 
                print("New best", total, seq)
                best = total 
    
print("Part 2", best)
