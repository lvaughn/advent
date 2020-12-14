#!/usr/bin/env python3

import re
from itertools import chain, combinations

MASK_RE = re.compile(r'mask\s*=\s*([01X]+)\s*$')
MEM_RE = re.compile(r'mem\[(\d+)\]\s*=\s*(\d+)\s*$')

zero_mask = 0
one_mask = 0
floating = []
mem = {}


def all_subsets(ls):
    return chain.from_iterable(combinations(ls, r) for r in range(len(ls) + 1))


with open('input.txt', 'r') as instructions:
    for inst in instructions:
        if inst.startswith('mask'):
            m = MASK_RE.match(inst)
            zero_mask = 0
            one_mask = 0
            floating = []
            for c in m[1]:
                if c == '0':
                    one_mask = one_mask * 2
                    zero_mask = zero_mask * 2 + 1
                    floating = [f * 2 for f in floating]
                elif c == '1':
                    one_mask = one_mask * 2 + 1
                    zero_mask = zero_mask * 2 + 1
                    floating = [f * 2 for f in floating]
                else:
                    if c != 'X':
                        print("Surprised character", c, inst)
                    floating = [f * 2 for f in floating]
                    floating.append(1)
                    one_mask = one_mask * 2
                    zero_mask = zero_mask * 2
        elif inst.startswith('mem'):
            m = MEM_RE.match(inst)
            loc = int(m[1])
            loc = loc | one_mask
            loc = loc & zero_mask
            value = int(m[2])
            for s in all_subsets(floating):
                mem[loc + sum(s)] = value
        else:
            print("UNKNOWN INSTRUCTION", inst)

print(sum(mem.values()))
