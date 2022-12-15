#!/usr/bin/env python3
# from string import ascii_uppercase, ascii_lowercase
# from collections import Counter, defaultdict, deque, namedtuple
# from itertools import count, product, permutations, combinations, combinations_with_replacement
# from sortedcontainers import SortedSet, SortedDict, SortedList
# import numpy as np
# import re
# import pprint
import re
import sys


# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

def man_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def remove_from_list(ls, lower, upper):
    #print("Remove", ls, lower, upper)
    if len(ls) == 0:
        return []
    cur_low, cur_high = ls[0]
    if upper < cur_low:
        return ls  # It's not in the list
    if lower > cur_high: # It's later in the list
        return [ls[0]] + remove_from_list(ls[1:], lower, upper)
    # Now there's an intersection
    if lower <= cur_low:
        if upper >= cur_high:
            # Kill this one, may keep going up
            return remove_from_list(ls[1:], lower, upper)
        else:
            return [(upper+1, cur_high)] + remove_from_list(ls[1:], lower, upper)
    else:
        if upper <= cur_high:
            # take out of the middle of the current batch
            return [(cur_low, lower-1), (upper+1, cur_high)] + ls[1:]
        else:
            return [(cur_low, lower-1)] + remove_from_list(ls[1:], lower, upper)
    assert(False)


def fix_list(ls):
    if len(ls) < 2:
        return ls
    if ls[0][1] >= ls[1][0]:
        return fix_list([(ls[0][0], ls[1][1])] + ls[2:])
    return [ls[0]] + fix_list(ls[1:])

def count(ls):
    if len(ls) == 0:
        return 0
    return (ls[0][1] - ls[0][0] + 1) + count(ls[1:])


answer = 0
max_size = 4000000
#max_size = 20

output_ls = []
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

possibles = []
for y in range(max_size+1):
    possibles.append([(0, max_size)])

in_row = set()
for l in lines:
    sx, sy, bx, by = map(int, re.findall(r'(-?\d+)', l))
    dist = man_dist(sx, sy, bx, by)
    print(l)
    print(f"dist={dist} sy={sx}")
    for y in range(sy - dist, sy + dist + 1):
        if y < 0 or y > max_size:
            continue
        avail = dist - abs(y - sy)
        # print(f"  To remove y={y} avail={avail}")
        # print(f"  Removing from {max(0, sx - avail)} to {min(sx + avail, max_size+1)}")
        # print(f"  Before: {possibles[y]}")
        possibles[y] = remove_from_list(possibles[y], max(0, sx - avail), min(sx + avail, max_size+1))
        # print(f"  After : {possibles[y]}")
# print(possibles[14])
#
for y, p in enumerate(possibles):
    if len(p) > 0:
        print(y, p)
        assert(len(p)==1)
        assert(p[0][0] == p[0][1])
        print("Part 2", 4000000*p[0][0]+y)

# for i in range(max_size):
#     for span in possibles[i]:
#         if span[1] > span[0] + 1:
#             print(i, span)

