#!/usr/bin/env python3

import sys, re
from itertools import product
from collections import defaultdict

# The output of prep.py
var_3 = [1, 1, 1, 1, 26, 26, 1, 1, 26, 26, 1, 26, 26, 26]
var_4 = [10, 11, 14, 13, -6, -14, 14, 13, -8, -15, 10, -11, -13, -4]
var_14 = [1, 9, 12, 6, 9, 15, 7, 12, 15, 3, 6, 2, 10, 12]

def get_possible_input_zs(vars, z_out, w):
    """ Find all the possible inputs for a block for a given output and w """
    v3, v4, v14 = vars
    possible_z_in = set()
    a = w - v3
    if 0 <= a < 26:
        possible_z_in.add(a + z_out * v14)
    x = z_out - w - v4
    if x % 26 == 0:
        possible_z_in.add(x // 26 * v14)

    print(f"     Possibles: vars={vars} z_out={z_out}, w={w}: {possible_z_in}")
    return possible_z_in

possible_ws = list(range(1, 10))
result_cache = defaultdict(list)
output_zs = set([0])
for vars in zip(reversed(var_3), reversed(var_4), reversed(var_14)):
    input_zs = set()
    print(vars)
    for w, z_out in product(possible_ws, output_zs):
        print(f"  w={w}, z_out={z_out}")
        zs_in = get_possible_input_zs(vars, z_out, w)
        input_zs = input_zs | zs_in
        for z_in in zs_in:
            result_cache[z_in].append(w)
    output_zs = input_zs

print(result_cache)


