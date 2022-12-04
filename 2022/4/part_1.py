#!/usr/bin/env python3
#from string import ascii_uppercase, ascii_lowercase
#from collections import Counter, defaultdict, deque, namedtuple
#from itertools import count, product, permutations, combinations, combinations_with_replacement
from sortedcontainers import SortedSet, SortedDict, SortedList
import sys
#import numpy as np
#import re

# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

answer = 0
with open(sys.argv[1], 'r') as infile:
    for line in [l.strip() for l in infile]:
        elf_a, elf_b = line.split(",")
        a_lower, a_upper = map(int, elf_a.split("-"))
        b_lower, b_upper = map(int, elf_b.split("-"))
        if (a_lower <= b_lower and a_upper >= b_upper) or \
            (b_lower <= a_lower and b_upper >= a_upper):
            answer += 1

print("Part 1", answer)
