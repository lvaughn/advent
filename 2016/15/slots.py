#!/usr/bin/env python3

discs = [
    (17, 1),
    (7, 0),
    (19, 2),
    (5, 0),
    (3, 0),
    (13, 5)
]

# discs = ((5, 4), (2, 1)) # Test data

base_time = 0
skip = 1
for i, disc in enumerate(discs):
    slots, start = disc
    while (base_time+i+1+start) % slots != 0:
        base_time += skip
    skip *= slots

print("First run", base_time, skip)

discs.append((11, 0))
base_time = 0
skip = 1
for i, disc in enumerate(discs):
    slots, start = disc
    while (base_time+i+1+start) % slots != 0:
        base_time += skip
    skip *= slots

print("Second run", base_time, skip)

