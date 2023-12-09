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

with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
answer = sum((int(l)//3) - 2 for l in lines)

print("Part 1", answer)

def total_fuel(mass):
    fuel = mass//3 - 2
    new_fuel = fuel//3 - 2
    while new_fuel > 0:
        fuel += new_fuel
        new_fuel = new_fuel // 3 - 2
    return fuel 

print("Part 2", sum(total_fuel(int(l)) for l in lines))
