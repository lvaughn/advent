#!/usr/bin/env python3

from collections import defaultdict
import re

ops = {
    '<': lambda a, b: a < b,
    '>': lambda a, b: a > b,
    '>=': lambda a, b: a >= b,
    '<=': lambda a, b: a <= b,
    '==': lambda a, b: a == b,
    '!=': lambda a, b: a != b
}
highest_seen = -100000000
with open('input.txt', 'r') as f:
    inst_re = re.compile(r'(\w+) (dec|inc) ([0-9-]+) if (\w+) (\S+) ([0-9-]+)')
    registers = defaultdict(int)
    for line in f:
        m = inst_re.match(line)
        dest_reg = m[1]
        dest_value = int(m[3])
        if m[2] == 'dec':
            dest_value *= -1
        src_reg = m[4]
        op = m[5]
        src_value = int(m[6])
        if ops[op](registers[src_reg], src_value):
            registers[dest_reg] += dest_value
        highest_seen = max(highest_seen, max(registers.values()))

print('Highest at end', max(registers.values()))
print('Highest ever', highest_seen)