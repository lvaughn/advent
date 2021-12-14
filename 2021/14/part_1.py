#!/usr/bin/env python3

import numpy as np
import re
from collections import Counter


def expand(s, rules):
    result = s[0]
    for loc in range(len(s) - 1):
        pair = s[loc:loc + 2]
        if pair in rules:
            result += rules[pair]
        result += s[loc + 1]
    return result


with open("input.txt", "r") as infile:
    lines = [line for line in infile]

rules = {}
rule_re = re.compile(r'(\w\w)\s+->\s*(\w)')
starting_pattern = lines[0].strip()
for l in lines[2:]:
    m = rule_re.match(l)
    rules[m[1]] = m[2]

poly = starting_pattern
for _ in range(10):
    poly = expand(poly, rules)

counts = Counter(poly)
common = counts.most_common()
delta = common[0][1] - common[-1][1]
print(f"Part 1: {delta}")
