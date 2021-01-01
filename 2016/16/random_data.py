#!/usr/bin/env python3

def iterate_fill(s):
    new_s = ''.join(reversed(s))
    new_s = new_s.replace('1', 'A').replace('0', '1').replace('A', '0')
    return s + '0' + new_s

def calulate_checksum(s):
    checksum = ''
    for i in range(len(s)//2):
        if s[2*i] == s[2*i+1]:
            checksum += '1'
        else:
            checksum += '0'
    if len(checksum) % 2 == 0:
        return calulate_checksum(checksum)
    return checksum


starting_data = '11110010111001001'
target_len = 272

s = starting_data
while len(s) < target_len:
    s = iterate_fill(s)
print("Part 1", calulate_checksum(s[:target_len]))

new_target_len = 35651584
s = starting_data
while len(s) < new_target_len:
    s = iterate_fill(s)
print("Part 2", calulate_checksum(s[:new_target_len]))