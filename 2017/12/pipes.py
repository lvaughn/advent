#!/usr/bin/env python3

import re

paths = {}

with open('input.txt', 'r') as f:
    input_re = re.compile(r'(\d+) <-> (.*)')
    for line in f:
        m = input_re.match(line)
        paths[m[1]] = [a.strip() for a in m[2].split(',')]


def find_group(root, seen):
    for dest in paths[root]:
        if dest not in seen:
            seen.add(dest)
            find_group(dest, seen)
    return seen


# Part 1
group_zero = find_group('0', set())
print("Group 0:", len(group_zero))

# Part 2
nodes = set(paths.keys())
n_groups = 0
while len(nodes) > 0:
    root = nodes.pop()
    in_group = find_group(root, set())
    n_groups += 1
    nodes = nodes - in_group

print("Number of groups:", n_groups)