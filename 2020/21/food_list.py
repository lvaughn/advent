#!/usr/bin/env python3

import re
from collections import defaultdict

allergen_sets = defaultdict(list) # allergen => list of sets of foods
good_foods = set() # Starts as all foods, then reduced as we figure out allergy info
total_list = [] # All foods mentioned, included the correct number of duplications
with open('input.txt', 'r') as infile:
    line_re = re.compile(r'((\w+\s+)+)\(contains(.*)\)')
    for line in infile:
        m = line_re.match(line)
        allergens = re.split(r',?\s', m[3].strip())
        foods = m[1].strip().split(" ")
        total_list.extend(foods)
        food_set = set(foods)
        good_foods = good_foods.union(food_set)
        for a in allergens:
            allergen_sets[a].append(food_set)

# For each allergen, figure out the possible foods containing it
# Just intersect all of the sets of foods from those products with the allergy
for a in allergen_sets:
    ls = allergen_sets[a]
    possible = ls[0]
    for s in ls[1:]:
        possible = possible.intersection(s)
    good_foods = good_foods - possible # Remove those from the known safe foods

print(len([a for a in total_list if a in good_foods]))
