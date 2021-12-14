#!/usr/bin/env python3

import numpy as np
import re
from collections import Counter

CACHE = {}  # (s, layers) = counts


def expand(s, layers, rules):
    # print(s, layers)
    if layers == 0:
        return Counter(s)
    key = (s, layers)
    if key not in CACHE:
        result = Counter()
        for loc in range(len(s) - 1):
            result += expand(s[loc] + rules[s[loc:loc + 2]] + s[loc + 1], layers - 1, rules)
        # True up the middle
        for c in s[1:-1]:
            result[c] -= 1
        CACHE[key] = result
    return CACHE[key]


with open("input.txt", "r") as infile:
    lines = [line for line in infile]

rules = {}
rule_re = re.compile(r'(\w\w)\s+->\s*(\w)')
starting_pattern = lines[0].strip()
for l in lines[2:]:
    m = rule_re.match(l)
    rules[m[1]] = m[2]

counts = expand(starting_pattern, 10, rules)
common = counts.most_common()
delta = common[0][1] - common[-1][1]
print(f"Part 1: {delta}")

counts = expand(starting_pattern, 40, rules)
print(counts)
common = counts.most_common()
delta = common[0][1] - common[-1][1]
print(f"Part 2: {delta}")
