#!/usr/bin/env python3

import re
from collections import Counter
from operator import itemgetter
from string import ascii_lowercase


def is_valid_room(name, checksum):
    counts = Counter(name.replace('-', ''))
    in_order = sorted(sorted(counts.items(), key=itemgetter(0)), key=itemgetter(1), reverse=True)
    check = ''.join(a[0] for a in in_order[:5])
    return check == checksum

LETTER_TO_LOC = {}
for loc, letter in enumerate(ascii_lowercase):
    LETTER_TO_LOC[letter] = loc


def decrypt_name(name, sector):
    output = ''
    for c in name:
        if c == '-':
            output += ' '
        else:
            output += ascii_lowercase[(LETTER_TO_LOC[c]+sector)%26]
    return output.strip()


room_re = re.compile(r'([a-z-]+)(\d+)\[(\w{5})\]')
valid_rooms = []
sector_sum = 0
with open('input.txt', 'r') as f:
    for line in f:
        m = room_re.match(line)
        assert m
        if is_valid_room(m[1], m[3]):
            sector = int(m[2])
            sector_sum += int(sector)
            valid_rooms.append((decrypt_name(m[1], sector), sector))

print(sector_sum)
for room in valid_rooms:
    if 'north' in room[0]:
        print(room)