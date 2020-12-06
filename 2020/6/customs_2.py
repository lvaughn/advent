#!/usr/bin/env python3

def intersect(lines):
    ans = set(lines[0])
    for l in lines[1:]:
        ans = ans.intersection(set(l))
    return ans


total = 0
with open('input.txt', 'r') as infile:
    lines = []
    for l in infile:
        l = l.strip()
        if len(l) == 0:
            total += len(intersect(lines))
            lines = []
        else:
            lines.append(l)

total += len(intersect(lines))
print(total)
