#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    adjustments = [int(n) for n in f]
    print("Part 1:", sum(adjustments))

    seen = set()
    current = 0
    i = 0
    while current not in seen:
        seen.add(current)
        current += adjustments[i]
        i = (i+1) % len(adjustments)

    print("Part 2:", current)

