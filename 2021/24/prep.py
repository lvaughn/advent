#!/usr/bin/env python3

last_args = []

# Parses out the lines that change from the input program

with open('input.txt', 'r') as infile:
    loc = 0
    for line in infile:
        if line.startswith('inp'):
            loc = 0
            continue
        last_arg = line.strip().split()[-1]
        while loc + 1 > len(last_args):
            last_args.append([])
        last_args[loc].append(last_arg)
        loc += 1

for var_num, arg in enumerate(last_args):
    if any(arg[0] != x for x in arg[1:]):
        print(f"var_{var_num} = {[int(a) for a in arg]}")
        var_num += 1
