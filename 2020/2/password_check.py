#!/usr/bin/env python3

import re

LINE_RE = re.compile(r'(\d+)-(\d+)\s+(\w):\s+(\w*)')


def is_valid(line):
    m = LINE_RE.search(line)
    if m is None:
        print("Bogus line: '{}'".format(line))
        return False
    min_count = int(m[1])
    max_count = int(m[2])
    c = m[3]
    password = m[4]
    occurrences = password.count(c)
    return min_count <= occurrences <= max_count


n_valid = 0
with open('input.txt', 'r') as infile:
    for line in infile:
        if is_valid(line):
            n_valid += 1
print(n_valid)
