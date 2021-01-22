#!/usr/bin/env python3

import re
from collections import defaultdict

particles = []
with open('input.txt', 'r') as f:
    line_re = re.compile(r'p=<([^>]+)>, v=<([^>]+)>, a=<([^>]+)>')
    for line in f:
        m = line_re.match(line)
        pos = [int(a) for a in m[1].split(',')]
        vel = [int(a) for a in m[2].split(',')]
        acc = [int(a) for a in m[3].split(',')]
        particles.append([pos, vel, acc])

for _ in range(100):
    new_particles = []
    all_away = True
    pos_counter = defaultdict(int)
    for i, particle in enumerate(particles):
        pos, vel, acc = particle
        new_vel = [sum(x) for x in zip(vel, acc)]
        new_pos = tuple(sum(x) for x in zip(pos, new_vel))
        new_dist = sum(abs(x) for x in new_pos)
        pos_counter[new_pos] += 1
        new_particles.append([new_pos, new_vel, acc])
    particles = []
    for p in new_particles:
        if pos_counter[p[0]] == 1:
            particles.append(p)
    print(len(particles))

