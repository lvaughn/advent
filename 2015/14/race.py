#!/usr/bin/env python3

import re
from collections import defaultdict

speeds = {}
duration = {}
rest = {}
race_time = 2503


def get_distance(deer, time):
    dist = 0
    distances = []
    while time > 0:
        move_for = min(time, duration[deer])
        for _ in range(move_for):
            time -= 1
            dist += speeds[deer]
            distances.append(dist)
        for _ in range(rest[deer]):
            time -= 1
            distances.append(dist)
    return distances, dist


with open('input.txt', 'r') as f:
    input_re = re.compile(r'(\w+) can fly (\d+) km/s for (\d+).*for (\d+) seconds')
    for line in f:
        m = input_re.match(line)
        speeds[m[1]] = int(m[2])
        duration[m[1]] = int(m[3])
        rest[m[1]] = int(m[4])

best = -1
distances = {}
for deer in speeds:
    distances[deer], dist = get_distance(deer, race_time)
    best = max(best, dist)
scores = defaultdict(int)
for i in range(race_time):
    best = -1
    for deer in distances:
        best = max(distances[deer][i], best)
    for deer in distances:
        if best == distances[deer][i]:
            scores[deer] += 1

print(best)
print(max(scores.values()))
