#!/usr/bin/env python

from operator import itemgetter

blocked = [] # Sorted list of blocked ranges

with open('input.txt', 'r') as f:
    for line in f:
        low, high = (int(x) for x in line.split('-'))
        blocked.append([low, high])

blocked.sort(key=itemgetter(0))

new_blocked = [blocked[0]]
for item in blocked[1:]:
    last = new_blocked[-1]
    if item[0] <= last[1] + 1:
        new_blocked[-1] = [min(item[0], last[0]), max(item[1], last[1])]
    else:
        new_blocked.append(item)

print("Lowest open", new_blocked[0][1] + 1)

# Figure out the total number of IPs
total = 2**32
for block in new_blocked:
    n_blocked = block[1]-block[0] + 1 # They're inclusive
    total -= n_blocked

print("Total allowed", total)