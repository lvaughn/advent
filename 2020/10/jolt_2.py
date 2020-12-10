#!/usr/bin/env python3

with open('input.txt') as infile:
    adaptors = [int(n) for n in infile]

ordered = [0] + sorted(adaptors)
ordered.append(ordered[-1] + 3)

CACHE = {
    len(ordered) - 1: 1
}


def ways_to_end(position):
    if position in CACHE:
        return CACHE[position]
    ans = 0
    current = ordered[position]
    i = 1
    while position+i < len(ordered) and ordered[position + i] <= current + 3:
        ans += ways_to_end(position + i)
        i += 1
    CACHE[position] = ans
    return ans


print(ways_to_end(0))
