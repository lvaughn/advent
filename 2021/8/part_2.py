#!/usr/bin/env python3

import numpy as np
import re


def get_mapping(tests):
    mapping = {}
    tests = [frozenset(t) for t in tests]
    for t in tests:
        if len(t) == 2:
            one = t
            mapping[t] = 1
        elif len(t) == 3:
            seven = t
            mapping[t] = 7
        elif len(t) == 4:
            four = t
            mapping[t] = 4
        elif len(t) == 7:
            mapping[t] = 8

    # Now, back out the other 6
    # 6 seg = 0, 6, 9
    # 5 seg = 2, 3, 5
    for t in tests:
        if len(t) in [2, 3, 4, 7]:
            continue
        if len(t) == 6:
            if len(t & four) == 3 and len(t & one) == 2:
                mapping[t] = 0
            elif len(t & one) == 1:
                mapping[t] = 6
            else:
                mapping[t] = 9
        elif len(t) == 5:
            if len(t & one) == 2:
                mapping[t] = 3
            elif len(t & four) == 2:
                mapping[t] = 2
            else:
                mapping[t] = 5
        else:
            print(t)
            assert False
    return mapping


with open("input.txt", "r") as infile:
    lines = [l for l in infile]

output_total = 0
for line in lines:
    (seq, output) = line.split('|')
    mapping = get_mapping(seq.split())
    digits = [frozenset(w) for w in output.split()]
    total = 0
    for d in digits:
        total *= 10
        total += mapping[d]
    output_total += total

print(output_total)
