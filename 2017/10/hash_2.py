#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    sizes = [ord(a) for a in f.readline().strip()]
sizes += [17, 31, 73, 47, 23]

message = list(range(256))

skip = 0
loc = 0
for _ in range(64):
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

output_binary = []
for i in range(16):
    value = 0
    for j in range(16):
        value ^= message[i*16+j]
    output_binary.append(value)

print(''.join(['{:x}'.format(a) for a in output_binary]))
