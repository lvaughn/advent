#!/usr/bin/env python3
#from string import ascii_uppercase, ascii_lowercase, digits
#from collections import Counter, defaultdict, deque, namedtuple
#from itertools import count, product, permutations, combinations, combinations_with_replacement
#from sortedcontainers import SortedSet, SortedDict, SortedList
#import numpy as np
#import re
#import pprint
import sys


# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

def validate(candiate: int) -> bool:
    n = [int(a) for a in f"{candiate}"]    
    
    has_double = False
    for a, b in zip(n[:-1], n[1:]):
        if b < a:
            return False 
        if a == b:
            has_double = True 
        
    return has_double 

def validate_2(candiate: int) -> bool:
    n = [int(a) for a in f"{candiate}"]    
    
    for a, b in zip(n[:-1], n[1:]):
        if b < a:
            return False 

    has_double = False
    for i in range(len(n)-1):
        if n[i] == n[i+1]:
            works = True
            if i > 0:
                if n[i-1] == n[i]:
                    works = False
            if i < len(n) - 2:
                if n[i] == n[i+2]:
                    works = False
            if works:
                has_double = True
        
    return has_double 

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

start, stop = lines[0].split('-')
for n in range(int(start), int(stop)+1):
    if validate(n):
        answer += 1
print("Part 1", answer)

answer = 0
start, stop = lines[0].split('-')
for n in range(int(start), int(stop)+1):
    if validate_2(n):
        answer += 1
print("Part 2", answer)