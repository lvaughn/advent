#!/usr/bin/env python3
from collections import Counter, defaultdict, deque, namedtuple
import sys
from fractions import Fraction
from dataclasses import dataclass
from z3 import Solver, BitVec, Distinct


with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
@dataclass
class Stone:
    x: int 
    y: int
    z: int 
    dx: int 
    dy: int
    dz: int 
    
stones = []
for line in lines:
    position, velocity = line.split("@")
    pos = tuple([int(i.strip()) for i in position.split(',')])
    vel = tuple([int(i.strip()) for i in velocity.split(',')])
    s = Stone(x=pos[0], y=pos[1], z=pos[2], dx=vel[0], dy=vel[1], dz=vel[2])
    stones.append(s)
    
s = Solver()
rock_x = BitVec("rock_x", 63)
rock_y = BitVec("rock_y", 63)
rock_z = BitVec("rock_z", 63)
rock_dx = BitVec("rock_dx", 63)
rock_dy = BitVec("rock_dy", 63)
rock_dz = BitVec("rock_dz", 63)

times = []
for i, stone in enumerate(stones[:50]): # Works fine with only 50, but tests ok with them all, just slow
    # Time they strike
    time = BitVec(f"time_{i}", 63)
    times.append(time)
    
    # Equations for the strike
    s.add(time > 0)
    s.add(stone.x + stone.dx * time == rock_x + rock_dx * time)
    s.add(stone.y + stone.dy * time == rock_y + rock_dy * time)
    s.add(stone.z + stone.dz * time == rock_z + rock_dz * time)
    
    
# All the times must be different
s.add(Distinct(times))

print(s.check())
m = s.model()
x_ans = m[rock_x].as_long()
y_ans = m[rock_y].as_long()
z_ans = m[rock_z].as_long()
print("Part 2", x_ans + y_ans + z_ans)
    



    
