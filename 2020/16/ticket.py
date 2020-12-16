#!/usr/bin/env python3

rules = {}
tickets = []
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

ranges = []  # A sorted list of valid ranges
for range_ls in rules.values():
    ranges.extend(range_ls)
valid_ranges = []
for rng in sorted(ranges, key=lambda x: x[0]):
    if len(valid_ranges) == 0:
        valid_ranges.append(rng)
        continue
    last = valid_ranges[-1]
    if rng[0] <= last[1]:  # Merge
        valid_ranges[-1] = (min(rng[0], last[0]), max(rng[1], last[1]))
    else:  # Add it
        valid_ranges.append(rng)


def is_valid(n):
    for rng in valid_ranges:
        if n < rng[0]:
            return False
        if rng[0] <= n <= rng[1]:
            return True
    return False


total = 0
for ticket in tickets:
    for n in ticket:
        if not is_valid(n):
            total += n
print(total)
