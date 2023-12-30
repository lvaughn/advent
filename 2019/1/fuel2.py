#!/usr/bin/env python

def calc_fuel(mass):
    s = 0
    fuel = mass/3-2
    while fuel > 0:
        s += fuel
        fuel = fuel/3-2
    return s

with open('input.txt') as i:
    print sum([calc_fuel(int(a)) for a in i])

