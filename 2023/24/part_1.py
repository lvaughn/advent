#!/usr/bin/env python3
from collections import Counter, defaultdict, deque, namedtuple
import sys
from fractions import Fraction


def get_eqn(stone):
    dx,dy, dz = stone.vel
    x, y, z = stone.pos 
    
    slope = Fraction(dy, dx)
    intercept = y - (x * slope)
    
    return (slope, intercept)
    
def get_intersection(a, b):
    a_m, a_b = get_eqn(a)
    b_m, b_b = get_eqn(b)
    if a_m == b_m:  # Parallel
        return None, None  
    
    x = Fraction(b_b-a_b, a_m - b_m)
    y = a_m*x + a_b 
    
    a_inc = y- a.pos[1]> 0
    if (a_inc and a.vel[1] < 0) or (not a_inc and a.vel[1] > 0):
        return None, None # In a's past 
    
    b_inc = y - b.pos[1]> 0
    if (b_inc and b.vel[1] < 0) or (not b_inc and b.vel[1] > 0):
        return None, None # In b's past 
    
    return x, y

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
Stone = namedtuple("Stone", ["pos", "vel"])
stones = []
for line in lines:
    position, velocity = line.split("@")
    pos = tuple([int(i.strip()) for i in position.split(',')])
    vel = tuple([int(i.strip()) for i in velocity.split(',')])
    stones.append(Stone(pos, vel))
    
low_target = 7
high_target = 27

low_target = 200000000000000
high_target = 400000000000000

for i in range(len(stones)-1):
    for j in range(i+1, len(stones)):
        a = stones[i]
        b = stones[j]
        x, y = get_intersection(a, b)
        if x != None:
            if low_target <= x <= high_target and low_target <= y <= high_target:
                answer += 1
        
       
print("Part 1", answer)


