#!/usr/bin/env python3

amount = 150
# Load up the containers
with open('input.txt', 'r') as f:
    containers = [int(l) for l in f]

memo_cache = {}


def n_combos(remaining, starting_loc):
    if remaining == 0:
        return 1
    assert remaining > 0
    if starting_loc == len(containers):
        return 0
    key = (remaining, starting_loc)
    if key not in memo_cache:
        combos = 0
        if containers[starting_loc] <= remaining:
            combos += n_combos(remaining - containers[starting_loc], starting_loc + 1)
        combos += n_combos(remaining, starting_loc + 1)
        memo_cache[key] = combos
    return memo_cache[key]


print(n_combos(amount, 0))
