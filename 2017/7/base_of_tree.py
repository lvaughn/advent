#!/usr/bin/env python3

import re

nodes = set()
children = set()

with open('input.txt', 'r') as f:
    line_re = re.compile(r'(\w+)\s+\((\d+)\)\s*(->)?(.*)')
    for line in f:
        m = line_re.match(line)
        name = m[1]
        rest = m[4]
        nodes.add(name)
        for child in (a.strip() for a in rest.split(',')):
            children.add(child)

print(nodes - children)