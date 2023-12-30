#!/usr/bin/env python

from collections import namedtuple
import numpy as np

#Location = namedtuple('Location', ['x', 'y', 'z'])
#Velocity = namedtuple('Velocity', ['x', 'y', 'z'])
Moon = namedtuple('Moon', ['loc', 'velocity'])

def energy_for_moon(moon):
    return sum(abs(moon.loc)) * sum(abs(moon.velocity))

def delta_v_pair(a, b):
    return (b.loc-a.loc).clip(-1, 1)

def to_hash(moons):
    foo = np.zeros((4,6), dtype=int)
    for i in xrange(4):
        foo[i,:3] = moons[i].loc
        foo[i,3:] = moons[i].velocity
    return tuple(map(tuple, foo))

moons = []
with open('test_1.txt') as i:
    for line in i:
        x,y,z = [int(a.strip()[2:]) for a in line.strip().strip('><').split(",")]
        moons.append(Moon(np.array((x,y,z), dtype=int), np.zeros((3), dtype=int)))

#for m in moons:
#    print m

seen = set()
seen.add(to_hash(moons))
print(to_hash(moons))
for _ in xrange(1000):
    new_v = np.zeros((4,3), dtype=int)
    for i in xrange(3):
        for j in xrange(i+1, 4):
            delta = delta_v_pair(moons[i], moons[j])
            new_v[i] += delta
            new_v[j] -= delta

    for i in xrange(4):
        new_vel = moons[i].velocity + new_v[i]
        new_loc = moons[i].loc + new_vel
        moons[i] = Moon(new_loc, new_vel)

for m in moons:
    print m
print "energy", sum([energy_for_moon(a) for a in moons])
                
        
    



