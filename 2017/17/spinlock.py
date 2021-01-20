#!/usr/bin/env python3

skip = 343
target = 2017

loc = 0
buff = [0]

for i in range(1, target + 1):
    loc = ((loc + skip) % len(buff)) + 1
    buff.insert(loc, i)

print("Part 1", buff[loc + 1])

target = 50000000
loc = 0
buff = [0]
buff_one = None
buff_len = 1
for i in range(1, target + 1):
    loc = ((loc + skip) % buff_len) + 1
    if loc == 1:
        buff_one = i
    buff_len += 1

print("Part 2", buff_one)