#!/usr/bin/env python3

def union(lines):
    ans = set()
    for l in lines:
        for c in l:
            ans.add(c)
    return ans


total = 0
with open('input.txt', 'r') as infile:
    lines = []
    for l in infile:
        l = l.strip()
        if len(l) == 0:
            total += len(union(lines))
            lines = []
        else:
            lines.append(l)

total += len(union(lines))
print(total)
