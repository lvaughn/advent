#!/usr/bin/env python3

import re

known = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

modifiers = {
    'cats': 'gt',
    'trees': 'gt',
    'pomeranians': 'lt',
    'goldfish': 'lt',
}

with open('input.txt', 'r') as f:
    sue_re = re.compile(r'Sue\s+(\d+):\s+(.*)')
    attribute_re = re.compile(r'\s*(\w+):\s+(\d+)')
    for line in f:
        m = sue_re.match(line)
        sue_number = int(m[1])
        right_sue = True
        for attribute in m[2].split(','):
            am = attribute_re.match(attribute)
            at_name = am[1]
            mod = modifiers.get(at_name, 'eq')
            if mod == 'eq':
                if known[at_name] != int(am[2]):
                    right_sue = False
                    break
            elif mod == 'lt':
                if known[at_name] <= int(am[2]):
                    right_sue = False
                    break
            else:
                if known[at_name] >= int(am[2]):
                    right_sue = False
                    break
        if right_sue:
            print("Aunt Sue", sue_number)
            break
