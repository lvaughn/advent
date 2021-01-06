#!/usr/bin/env python3

import re
from collections import namedtuple

Node = namedtuple('Node', ['name', 'size', 'used', 'avail'])

nodes = []
with open('input.txt', 'r') as f:
    f.readline() # Shell command
    f.readline() # Headers
    line_re = re.compile(r'([a-z0-9/-]+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+')
    for line in f:
        m = line_re.match(line)
        nodes.append(Node(m[1], int(m[2]), int(m[3]), int(m[4])))

viable_pairs = 0
for i, a in enumerate(nodes):
    for b in nodes[i+1:]:
        if 0 < a.used <= b.avail:
            viable_pairs += 1
        if 0 < b.used <= a.avail:
            viable_pairs += 1

print(viable_pairs)