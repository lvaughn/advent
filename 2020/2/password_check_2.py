#!/usr/bin/env python3

import re

LINE_RE = re.compile(r'(\d+)-(\d+)\s+(\w):\s+(\w*)')


def is_valid(line):
    m = LINE_RE.search(line)
    if m is None:
        print("Bogus line: '{}'".format(line))
        return False
    pos_a = int(m[1]) - 1
    pos_b = int(m[2]) - 1
    c = m[3]
    password = m[4]

    return (password[pos_a] == c) != (password[pos_b] == c)


n_valid = 0
with open('input.txt', 'r') as infile:
    for line in infile:
        if is_valid(line):
            n_valid += 1
print(n_valid)
