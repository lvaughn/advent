#!/usr/bin/env python3

import sys
import numpy as np

with open(sys.argv[1], 'r') as infile:
    starting_fish = [int(f) for f in infile.readline().split(',')]

fish = np.zeros((9,), dtype=int)
for f in starting_fish:
    fish[f] += 1

for _ in range(int(sys.argv[2])):
    new_fish = np.zeros((9,), dtype=int)
    new_fish[:-1] = fish[1:]
    new_fish[-1] = fish[0]
    new_fish[6] += fish[0]
    fish = new_fish

print(fish)
print(sum(fish))