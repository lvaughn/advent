#!/usr/bin/env python
from fractions import Fraction
from collections import defaultdict

# Load in the asteroids:
asteroids = set()
with open('input.txt') as df:
    row = 0
    for line in df:
        col = 0
        for c in line:
            if c == '#':
                asteroids.add((col, row))
            col += 1
        row += 1

most_seen = -1
best_loc = None
for a in asteroids:
    by_slope = defaultdict(list)
    for b in asteroids:
        if a == b:
            continue
        if a[0] == b[0]:
            by_slope['inf'].append(b)
        else:
            rise = a[1] - b[1]
            run = a[0] - b[0]
            by_slope[Fraction(rise, run)].append(b)
    can_see = 0
    for slope in by_slope.keys():
        other_asteroids = by_slope[slope]
        if slope == 'inf':
            # Find ones above
            for x in other_asteroids:
                if x[1] > a[1]:
                    can_see += 1
                    break
            # Find ones below
            for x in other_asteroids:
                if x[1] < a[1]:
                    can_see += 1
                    break
        else:
            # Find ones to the right
            for x in other_asteroids:
                if x[0] > a[0]:
                    can_see += 1
                    break
            for x in other_asteroids:
                if x[0] < a[0]:
                    can_see += 1
                    break
    print a, can_see
    if can_see > most_seen:
        most_seen = can_see
        best_loc = a

print "best", best_loc, most_seen

