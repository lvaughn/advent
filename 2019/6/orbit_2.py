#!/usr/bin/env python

class Planet:
    def __init__(self, name):
        self.orbits = []
        self.parent = None
        self.name = name
        
    def count_orbits(self, depth):
        total = depth
        for o in self.orbits:
            total += o.count_orbits(depth + 1)
        return total

    def transfers_needed(self, target, call_path):
        new_call_path = list(call_path)
        new_call_path.append(self.name)
        for child in self.orbits:
            if child.name in call_path:
                continue
            if child.name == target:
                return 0
            transfers = child.transfers_needed(target, new_call_path)
            if transfers is not None:
                print call_path
                return 1+transfers
        if self.parent.name not in call_path:
            transfers = self.parent.transfers_needed(target, new_call_path)
            if transfers is not None:
                print call_path
                return 1+transfers
        return None
            
        

name_to_planet = {}

with open('input.txt') as input:
    for line in input:
        aaron = line.index(')')
        center = line[:aaron]
        orbited_by = line[aaron+1:-1]
        if center not in name_to_planet:
            name_to_planet[center] = Planet(center)
        center_planet = name_to_planet[center]
        if orbited_by not in name_to_planet:
            name_to_planet[orbited_by] = Planet(orbited_by)
        outer_planet = name_to_planet[orbited_by]
        outer_planet.parent = center_planet
        center_planet.orbits.append(outer_planet)

you = name_to_planet['YOU']
print(you.parent.transfers_needed('SAN', ['YOU']))
            
        
        
