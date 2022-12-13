#!/usr/bin/env python3

import sys
import functools


def compare(a, b):
    if type(a) is int:
        if type(b) is int:
            if a < b:
                return 1
            elif b < a:
                return -1
            return 0
        else:
            return compare([a], b)
    assert (type(a) is list)
    if type(b) is int:
        return compare(a, [b])
    # Both are lists
    for i in range(min(len(a), len(b))):
        val = compare(a[i], b[i])
        if val != 0:
            return val
    if len(a) < len(b):
        return 1
    if len(b) < len(a):
        return -1
    return 0


answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

all_lines = []
for i in range((len(lines) // 3) + 1):
    a = eval(lines[i * 3])
    b = eval(lines[i * 3 + 1])
    all_lines.append(a)
    all_lines.append(b)
    if compare(a, b) > 0:
        answer += 1 + i

print("Part 1", answer)
all_lines.append([[2]])
all_lines.append([[6]])

sorted_ls = sorted(all_lines, key=functools.cmp_to_key(compare), reverse=True)
div_1 = sorted_ls.index([[2]])
div_2 = sorted_ls.index([[6]])

print("Part 2", (div_1 + 1) * (div_2 + 1))
