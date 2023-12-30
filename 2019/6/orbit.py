#!/usr/bin/env python

class Planet:
    def __init__(self):
        self.orbits = []
        
    def count_orbits(self, depth):
        total = depth
        for o in self.orbits:
            total += o.count_orbits(depth + 1)
        return total

name_to_planet = {}

with open('input.txt') as input:
    for line in input:
        aaron = line.index(')')
        center = line[:aaron]
        orbited_by = line[aaron+1:-1]
        if center not in name_to_planet:
            name_to_planet[center] = Planet()
        center_planet = name_to_planet[center]
        if orbited_by not in name_to_planet:
            name_to_planet[orbited_by] = Planet()
        outer_planet = name_to_planet[orbited_by]
        center_planet.orbits.append(outer_planet)

com = name_to_planet['COM']
print(com.count_orbits(0))
            
        
        
