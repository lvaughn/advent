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

def gcd(a, b):
    a, b = max(a,b), min(a,b)
    while b > 0:
        a, b = b, a%b
    return a

moons = []
with open('input.txt') as i:
    for line in i:
        x,y,z = [int(a.strip()[2:]) for a in line.strip().strip('><').split(",")]
        moons.append(Moon(np.array((x,y,z), dtype=int), np.zeros((3), dtype=int)))

#for m in moons:
#    print m

seen = set()
seen.add(to_hash(moons))
cycles = 0
cycles_seen = [-1, -1, -1] 
moon_seen = [set(), set(), set()]
x_hist = {}
keep_going = True
while keep_going:
#for i in range(3000):
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

    x_bits = []
    y_bits = []
    z_bits = []
    for i in xrange(4):
        #if cycles_seen[i] != -1:
        #    continue
        moon = moons[i]
        x_bits.append(moon.loc[0])
        x_bits.append(moon.velocity[0])
        y_bits.append(moon.loc[1])
        y_bits.append(moon.velocity[1])
        z_bits.append(moon.loc[2])
        z_bits.append(moon.velocity[2])
        
    x_hash = tuple(x_bits)
    if cycles_seen[0] < 1 and x_hash in moon_seen[0]:
        cycles_seen[0] = cycles
    else:
        moon_seen[0].add(x_hash)

    y_hash = tuple(y_bits)
    if cycles_seen[1] < 1 and y_hash in moon_seen[1]:
        cycles_seen[1] = cycles
    else:
        moon_seen[1].add(y_hash)

    z_hash = tuple(z_bits)
    if cycles_seen[2] < 1 and z_hash in moon_seen[2]:
        cycles_seen[2] = cycles
    else:
        moon_seen[2].add(z_hash)        

    cycles += 1

    keep_going = cycles_seen[0] == -1 or cycles_seen[1] == -1 or cycles_seen[2] == -1

print cycles_seen
tmp = cycles_seen[0]*cycles_seen[1]/gcd(cycles_seen[0], cycles_seen[1])
print cycles_seen[2]*tmp/gcd(tmp, cycles_seen[2])
       
    



