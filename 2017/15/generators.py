#!/usr/bin/env python3


def make_gen(start, factor, mod):
    current = start
    while True:
        current = (current * factor) % mod
        yield current


mask = 0xffff

gen_a = make_gen(883, 16807, 2147483647)
gen_b = make_gen(879, 48271, 2147483647)

n_same = 0
for _ in range(40000000):
    if (next(gen_a) & mask) == (next(gen_b) & mask):
        n_same += 1

print(n_same)
