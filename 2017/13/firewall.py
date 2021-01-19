#!/usr/bin/env python3

with open('input.txt') as f:
    walls = []
    for line in f:
        walls.append([int(a) for a in line.split(':')])

delay = 0
while True:
    total = 0
    hasHit = False
    for dist, length in walls:
        if (dist+delay) % (2*(length-1)) == 0:
            total += dist * length
            hasHit = True
    if delay == 0:
        print("Part 1:", total)
    if not hasHit:
        print("Delay:", delay)
        break
    delay += 1