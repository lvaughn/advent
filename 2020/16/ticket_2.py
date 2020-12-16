#!/usr/bin/env python3

import numpy as np
from collections import defaultdict

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

is_valid = np.zeros((max_num + 2), dtype=bool)
# Put together list of valid ranges
for range_ls in rules.values():
    for pair in range_ls:
        is_valid[pair[0]:pair[1] + 1] = True

total = 0
valid_tickets = []
for ticket in tickets:
    if all(is_valid[n] for n in ticket):
        valid_tickets.append(ticket)


# valid_tickets.append(my_ticket)

def all_valid(pos, ranges):
    for ticket in valid_tickets:
        value = ticket[pos]
        valid = False
        for rng in ranges:
            if rng[0] <= value <= rng[1]:
                valid = True
                break
        if not valid:
            return False
    return True


valid_positions = defaultdict(list)
for name in rules:
    for n in range(len(valid_tickets[0])):
        if all_valid(n, rules[name]):
            valid_positions[name].append(n)


def find_working_mapping(fields, already_used):
    if len(fields) == 0:
        return {}
    name = fields[0]
    for col in valid_positions[name]:
        if col not in already_used:
            used = set(already_used)
            used.add(col)
            mapping = find_working_mapping(fields[1:], used)
            if mapping is not None:
                mapping[fields[0]] = col
                return mapping
    return None


# Sorting these really speeds things up
rule_names = sorted(rules.keys(), key=lambda x: len(valid_positions[x]))
mapping = find_working_mapping(rule_names, set())
product = 1
for name in rule_names:
    if name.startswith('departure'):
        product *= my_ticket[mapping[name]]
print(product)
