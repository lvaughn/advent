#!/usr/bin/env python3
from collections import Counter, defaultdict, deque, namedtuple
import re
import sys
import math 

Moon = namedtuple("Moon", ['x', 'y', 'z', 'x_vel', 'y_vel', 'z_vel'])

def total_energy(moon: Moon) -> int:
    return sum(abs(x) for x in moon[:3]) * sum(abs(x) for x in moon[3:])

def get_delta_v(a: int, b: int) -> int:
    if a > b:
        return 1
    if a < b: 
        return -1
    return 0

def hash_slice(moons, offset):
    values = []
    for moon in moons:
        values.append(moon[offset])
        values.append(moon[offset+3])
    return tuple(values)
        

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
moon_re = re.compile(r'-?\d+')
moons = []
for l in lines:
    x, y, z = [int(a) for a in moon_re.findall(l)]
    moons.append(Moon(x, y, z, 0, 0, 0))
    
ITERATIONS = 1000
for _ in range(ITERATIONS):
    # Find velocity change
    new_velocities = []
    for m in range(len(moons)):
        moon = moons[m]
        dx, dy, dz = 0, 0, 0
        for i in range(len(moons)):
            if i == m: 
                continue 
            dx += get_delta_v(moons[i].x, moon.x)
            dy += get_delta_v(moons[i].y, moon.y)
            dz += get_delta_v(moons[i].z, moon.z)
        new_velocities.append((dx + moon.x_vel, dy + moon.y_vel, dz + moon.z_vel))
                
    new_moons = []
    for moon, new_vel in zip(moons, new_velocities):
        dx, dy, dz = new_vel
        new_moons.append(Moon(moon.x + dx, moon.y + dy, moon.z + dz, dx, dy, dz))
    moons = new_moons
    
answer = sum(total_energy(m) for m in moons)
print("Part 1", answer)

# Reset for part 2
moons = []
start_locations = []
for l in lines:
    x, y, z = [int(a) for a in moon_re.findall(l)]
    moons.append(Moon(x, y, z, 0, 0, 0))
    start_locations.append(Moon(x, y, z, 0, 0, 0))
    
cycles = [dict(), dict(), dict()] # x, y, z
cycle_lengths = [None] * 3  # x, y, z
n_cycles = 0
while None in cycle_lengths:
    n_cycles += 1
    
    new_velocities = []
    for m in range(len(moons)):
        moon = moons[m]
        dx, dy, dz = 0, 0, 0
        for i in range(len(moons)):
            if i == m: 
                continue 
            dx += get_delta_v(moons[i].x, moon.x)
            dy += get_delta_v(moons[i].y, moon.y)
            dz += get_delta_v(moons[i].z, moon.z)
        new_velocities.append((dx + moon.x_vel, dy + moon.y_vel, dz + moon.z_vel))
                
    new_moons = []
    for moon, new_vel in zip(moons, new_velocities):
        dx, dy, dz = new_vel
        new_moons.append(Moon(moon.x + dx, moon.y + dy, moon.z + dz, dx, dy, dz))
    moons = new_moons
    
    for i in range(3):
        key = hash_slice(moons, i)
        if cycle_lengths[i] is None and key in cycles[i]:
            cycle_lengths[i] = n_cycles - cycles[i][key]
        else:
            cycles[i][key] = n_cycles
            
            
grand_cycle_length = 1
for n in cycle_lengths:
    grand_cycle_length = (grand_cycle_length*n)//math.gcd(n, grand_cycle_length)
    
print("Part 2", grand_cycle_length)