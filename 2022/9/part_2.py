#!/usr/bin/env python3
#from string import ascii_uppercase, ascii_lowercase
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
tail_seen = set()
rope = []
for _ in range(10):
    rope.append((0, 0))
for line in lines:
    dir, amt = line.split(" ")
    amt = int(amt)
    for _ in range(amt):
        hx, hy = rope[0]
        new_rope = []
        if dir == "U":
            hy += 1
        elif dir == "D":
            hy -= 1
        elif dir == "R":
            hx += 1
        elif dir == 'L':
            hx -= 1
        new_rope.append((hx, hy))
        for tx, ty in rope[1:]:
            hx, hy = new_rope[-1]
            # See if the tail needs to move
            if abs(hy - ty) > 1 or abs(hx - tx) > 1:
                if hy > ty:
                    ty += 1
                if hy < ty:
                    ty -= 1
                if hx > tx:
                    tx += 1
                if hx < tx:
                    tx -= 1
            new_rope.append((tx, ty))
        rope = new_rope
        tail_seen.add((rope[-1][0], rope[-1][1]))

print("Part 2", len(tail_seen))
