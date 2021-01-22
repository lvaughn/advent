#!/usr/bin/env python3

import re

particles = []
with open('input.txt', 'r') as f:
    line_re = re.compile(r'p=<([^>]+)>, v=<([^>]+)>, a=<([^>]+)>')
    for line in f:
        m = line_re.match(line)
        pos = [int(a) for a in m[1].split(',')]
        vel = [int(a) for a in m[2].split(',')]
        acc = [int(a) for a in m[3].split(',')]
        particles.append([pos, vel, acc])

closest_particle = None
for _ in range(500):
    new_particles = []
    all_away = True
    closest_dist = 9999999999999
    n_smaller = 0
    for i, particle in enumerate(particles):
        pos, vel, acc = particle
        new_vel = [sum(x) for x in zip(vel, acc)]
        new_pos = [sum(x) for x in zip(pos, new_vel)]
        new_dist = sum(abs(x) for x in new_pos)
        if new_dist < closest_dist:
            closest_dist = new_dist
            closest_particle = i
        new_particles.append([new_pos, new_vel, acc])
    particles = new_particles

print(closest_particle)
