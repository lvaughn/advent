#!/usr/bin/env python3

import re

MASK_RE = re.compile(r'mask\s*=\s*([01X]+)\s*$')
MEM_RE = re.compile(r'mem\[(\d+)\]\s*=\s*(\d+)\s*$')

zero_mask = 0
one_mask = 0
mem = {}

with open('input.txt', 'r') as instructions:
    for inst in instructions:
        if inst.startswith('mask'):
            m = MASK_RE.match(inst)
            zero_mask = 0
            one_mask = 0
            for c in m[1]:
                if c == '0':
                    zero_mask = zero_mask * 2
                    one_mask = one_mask * 2
                elif c == '1':
                    zero_mask = zero_mask * 2 + 1
                    one_mask = one_mask * 2 + 1
                else:
                    if c != 'X':
                        print("Surprised character", c, inst)
                    zero_mask = zero_mask * 2 + 1
                    one_mask = one_mask * 2
        elif inst.startswith('mem'):
            m = MEM_RE.match(inst)
            value = int(m[2])
            value = value | one_mask
            value = value & zero_mask
            print(m[2], hex(int(m[2])), hex(value))
            mem[int(m[1])] = value
        else:
            print("UNKNOWN INSTRUCTION", inst)
print(sum(mem.values()))