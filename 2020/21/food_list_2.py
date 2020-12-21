#!/usr/bin/env python3

import re
from collections import defaultdict
from pprint import pprint

allergen_sets = defaultdict(list) # allergen => list of sets of foods
with open('input.txt', 'r') as infile:
    line_re = re.compile(r'((\w+\s+)+)\(contains(.*)\)')
    for line in infile:
        m = line_re.match(line)
        allergens = re.split(r',?\s', m[3].strip())
        foods = m[1].strip().split(" ")
        food_set = set(foods)
        for a in allergens:
            allergen_sets[a].append(food_set)

possible_sources = {}
for a in allergen_sets:
    ls = allergen_sets[a]
    possible = ls[0]
    for s in ls[1:]:
        possible = possible.intersection(s)
    possible_sources[a] = possible

pprint(possible_sources)
allergen_sources = {}
while len(possible_sources) > 0:
    known = [a for a in possible_sources if len(possible_sources[a]) == 1]
    for allergen in known:
        food = list(possible_sources[allergen])[0] # HACK
        allergen_sources[food] = allergen
        # Remove food from all other allergens
        for a in possible_sources:
            possible_sources[a].discard(food)
    for a in known:
        del possible_sources[a]

ls = sorted(allergen_sources.keys(), key=lambda x: allergen_sources[x])
print(','.join(ls))