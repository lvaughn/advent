#!/usr/bin/env python3
import re
import sys

NUMBER_RE = re.compile(r'(\w+):\s+(\d+)')
OP_RE = re.compile(r'(\w+):\s+(\w+)\s+([+-/*])\s+(\w+)')
answer = 0
number_lookup = {}
op_lookup = {}
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

for l in lines:
    m = NUMBER_RE.match(l)
    if m is not None:
        number_lookup[m[1]] = int(m[2])
        continue
    m = OP_RE.match(l)
    if m is not None:
        op_lookup[m[1]] = (m[3], m[2], m[4])
    else:
        print(l)
        assert False

CACHE = {}


def find_value(s):
    if s in CACHE:
        return CACHE[s]
    if s in number_lookup:
        return number_lookup[s]
    assert s in op_lookup
    op, val_a, val_b = op_lookup[s]
    a = find_value(val_a)
    b = find_value(val_b)
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a // b
    else:
        print(s, op_lookup[s])
        assert False
    CACHE[s] = result
    return result


print("Part 1", find_value('root'))
