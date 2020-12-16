#!/usr/bin/env python3

import numpy as np

rules = {}
tickets = []
max_num = -1
with open('input.txt', 'r') as input:
    l = input.readline().strip()
    while l != "":
        idx = l.index(':')
        name = l[:idx]
        rules_str = l[idx + 1:].split(' or ')
        ranges = []
        for r in rules_str:
            idx = r.index('-')
            ranges.append((int(r[:idx]), int(r[idx + 1:])))
        max_num = max(max_num, max(a[1] for a in ranges))
        rules[name] = ranges
        l = input.readline().strip()

    # my ticket
    assert input.readline().startswith('your')
    my_ticket = [int(a) for a in input.readline().split(',')]
    input.readline()  # burn empty line

    # Other tickets
    assert (input.readline().startswith('nearby'))
    for l in input:
        ticket = [int(a) for a in l.split(',')]
        tickets.append(ticket)
        max_num = max(max_num, max(ticket))

print("Max", max_num)
is_valid = np.zeros((max_num+2), dtype=bool)
# Put together list of valid ranges
for range_ls in rules.values():
    for pair in range_ls:
        is_valid[pair[0]:pair[1]+1] = True

total = 0
for ticket in tickets:
    for n in ticket:
        if not is_valid[n]:
            total += n

print(total)
