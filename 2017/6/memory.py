#!/usr/bin/env python3

starting_config = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6]

reconfigs = 0
when_seen = {}
current = list(starting_config)
while True:
    key = tuple(current)
    if key in when_seen:
        break
    when_seen[key] = reconfigs
    reconfigs += 1

    biggest = -1
    biggest_loc = -1
    for i, val in enumerate(current):
        if val > biggest:
            biggest = val
            biggest_loc = i

    n_left = current[biggest_loc]
    current[biggest_loc] = 0
    loc = (biggest_loc + 1) % len(current)
    while n_left:
        current[loc] += 1
        n_left -= 1
        loc = (loc + 1) % len(current)

print('Part 1', reconfigs)
print('Part 2', reconfigs - when_seen[key])