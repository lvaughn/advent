#!/usr/bin/env python3
import re
import sys


def man_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def insert_in_list(ls, y_min, y_max):
    if len(ls) == 0:
        return [(y_min, y_max)]
    if y_max < ls[0][0]:
        return [(y_min, y_max)] + ls
    if y_min < ls[0][1]:
        # Overlap!
        return [(min(y_min, ls[0][0]), max(y_max, ls[0][1]))] + ls[1:]
    return [ls[0]] + insert_in_list(ls[1:], y_min, y_max)


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
y_row = 2000000
# y_row = 10

output_ls = []
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

in_row = set()
for l in lines:
    sx, sy, bx, by = map(int, re.findall(r'(-?\d+)', l))
    dist = man_dist(sx, sy, bx, by)
    avail_x = dist - abs(y_row - sy)
    if avail_x > 0:
        output_ls = fix_list(insert_in_list(output_ls, sx - avail_x, sx + avail_x))
        if by == y_row:
            in_row.add(bx)
print("Part 1", count(output_ls) - len(in_row), output_ls)
