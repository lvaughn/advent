#!/usr/bin/env python3

from collections import defaultdict

amount = 150
# Load up the containers
with open('input.txt', 'r') as f:
    containers = [int(l) for l in f]

memo_cache = {}


def n_combos(remaining, starting_loc, so_far):
    if remaining == 0:
        return {so_far: 1}
    assert remaining > 0
    if starting_loc == len(containers):
        return {}
    key = (remaining, starting_loc, so_far)
    if key not in memo_cache:
        combos = defaultdict(int)
        if containers[starting_loc] <= remaining:
            result = n_combos(remaining - containers[starting_loc], starting_loc + 1, so_far + 1)
            for k in result:
                combos[k] += result[k]
        result = n_combos(remaining, starting_loc + 1, so_far)
        for k in result:
            combos[k] += result[k]
        memo_cache[key] = combos
    return memo_cache[key]


combos = n_combos(amount, 0, 0)
smallest = sorted(combos.keys())[0]
print(combos[smallest])
