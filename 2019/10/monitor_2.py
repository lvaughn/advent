#!/usr/bin/env python
from fractions import Fraction
from collections import defaultdict
from math import sqrt

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
best_by_slope = None
for a in asteroids:
    by_slope = defaultdict(list)
    for b in asteroids:
        if a == b:
            continue
        if a[0] == b[0]:
            by_slope['inf'].append(b)
        else:
            rise = a[1] - b[1]
            run = b[0] - a[0]
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
    #print a, can_see
    if can_see > most_seen:
        most_seen = can_see
        best_loc = a
        best_by_slope = by_slope

print "best", best_loc, most_seen
#print best_by_slope
north = []
north_east = defaultdict(list)
east = []
south_east = defaultdict(list)
south = []
south_west = defaultdict(list)
west = []
north_west = defaultdict(list)

for slope in best_by_slope.keys():
    if slope == 'inf':
        for a in best_by_slope['inf']:
            if a[1] < best_loc[1]:
                north.append(a)
            else:
                south.append(a)
    elif slope < 0:
        for a in best_by_slope[slope]:
            if a[0] > best_loc[0]:
                south_east[slope].append(a)
            else:
                north_west[slope].append(a)
    elif slope > 0:
        for a in best_by_slope[slope]:
            if a[0] > best_loc[0]:
                north_east[slope].append(a)
            else:
                south_west[slope].append(a)
    else: # slope == 0
        for a in best_by_slope[0]:
            if a[0] > best_loc[0]:
                east.append(a)
            else:
                west.append(a)

print north_east
dist_func = lambda a: sqrt((a[0]-best_loc[0])**2 + (a[1]-best_loc[1])**2)
nuked = []
to_nuke = []
to_nuke.append(sorted(north, key=dist_func))
print north, south
for s in reversed(sorted(north_east.keys())):
    #print "ne", s
    to_nuke.append(sorted(north_east[s], key=dist_func))
to_nuke.append(sorted(east, key=dist_func))
for s in reversed(sorted(south_east.keys())):
    #print "se", s
    to_nuke.append(sorted(south_east[s], key=dist_func))
to_nuke.append(sorted(south, key=dist_func))
for s in reversed(sorted(south_west.keys())):
    #print "sw", s
    to_nuke.append(sorted(south_west[s], key=dist_func))
to_nuke.append(sorted(west, key=dist_func))
for s in reversed(sorted(north_west.keys())):
    #print "nw", s
    to_nuke.append(sorted(north_west[s], key=dist_func))

while len(nuked) < len(asteroids) - 1:
    for i in range(len(to_nuke)):
        if len(to_nuke[i]) > 0:
            nuked.append(to_nuke[i][0])
            to_nuke[i] = to_nuke[i][1:]

print nuked
print nuked[198:201]
target =nuked[199]
print 100*target[0]+target[1]
