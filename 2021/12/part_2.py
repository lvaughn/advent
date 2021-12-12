#!/usr/bin/env python3

import numpy as np
import re
from collections import defaultdict

paths = []
connections = defaultdict(list)


def find_paths(path):
    for node in connections[path[-1]]:
        if node.islower() and node in path:
            # See if there is already a double path
            lower_list = [n for n in path if n.islower()]
            if len(lower_list) == len(set(lower_list)) and node != 'start':
                find_paths(path + [node])
        elif node == 'end':
            paths.append(path)
        else:
            find_paths(path + [node])


with open("input.txt", "r") as infile:
    for line in infile:
        a, b = line.strip().split('-')
        connections[a].append(b)
        connections[b].append(a)

find_paths(['start'])
print(len(paths))
