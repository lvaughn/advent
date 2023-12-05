#!/usr/bin/env python3
import sys

with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
def get_mapping(mappings, current_loc):
    for dest_start, src_start, length in mappings:
        if current_loc >= src_start and current_loc < src_start + length:
            return dest_start + (current_loc - src_start)
    return current_loc
    

seed_line = lines[0][len('seeds: '):]
current_locations = [int(a) for a in seed_line.split(' ')]

loc = 3
while loc < len(lines):
    mapping = []
    while loc < len(lines) and lines[loc] != '':
        dest_start, src_start, length = lines[loc].split(' ')
        mapping.append((int(dest_start), int(src_start), int(length))) 
        loc += 1
    loc += 2
    
    new_current_locations = []
    for now in current_locations:
        new_current_locations.append(get_mapping(mapping, now))
    current_locations = new_current_locations


print("Part 1", min(current_locations))
