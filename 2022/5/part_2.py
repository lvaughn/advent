#!/usr/bin/env python3

import sys
import re

rows = []
for i in range(9):
    rows.append([])
lines = []
with open(sys.argv[1], 'r') as infile:
    lines = [l for l in infile]

loc = 0
l = lines[loc]
while not l.startswith(' 1 '):
    for i in range(9):
        if l[1+4*i] != ' ':
            rows[i].insert(0, l[1+4*i])
    loc += 1
    l = lines[loc]

INST_RE = re.compile(r'(\d+)\D+(\d+)\D+(\d+)')
for inst in lines[loc + 2:]:
    m = INST_RE.search(inst)
    if m is not None:
        src = int(m[2])
        dest = int(m[3])
        n = int(m[1])
        # print(src, dest, n, inst)
        to_move = rows[src-1][-n:]
        rows[src - 1] = rows[src-1][:-n]
        rows[dest - 1].extend(to_move)

s = ""
for r in rows:
    s += r[-1]
print(s)


