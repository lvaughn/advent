#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    sizes = [int(a) for a in f.readline().strip().split(',')]

message = list(range(256))

skip = 0
loc = 0
for size in sizes:
    end = loc + size
    if end > len(message):
        at_start = loc + size - len(message)
        at_end = size - at_start
        to_reverse = message[loc:] + message[:at_start]
        rev_portion = list(reversed(to_reverse))
        message = rev_portion[-at_start:] + message[at_start:loc] + rev_portion[:at_end]
    else:
        to_reverse = message[loc:loc + size]
        message = message[:loc] + list(reversed(to_reverse)) + message[loc + size:]
    loc = (loc + size + skip) % len(message)
    skip += 1

print(message[0] * message[1])
