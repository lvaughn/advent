#!/usr/bin/env python3
import sys

with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
def apply_mappings(mappings, seed_range):
    if len(mappings) == 0:
        return [seed_range]
    rng_start, rng_end = seed_range
    for dest_start, src_start, length in mappings:
        if src_start > rng_end:
            continue
        if src_start + length - 1 < rng_start:
            continue
        # We have a hit! 
        move = dest_start - src_start
        return_values = []
        if rng_start < src_start: # Do anything below that doesn't overlap
            return_values.extend(apply_mappings(mappings, (rng_start, src_start-1)))
        if rng_end > src_start + length - 1: # Do anything above that doesn't overlap
            return_values.extend(apply_mappings(mappings, (src_start + length, rng_end)))
        # Handle the overlap
        start_val = max(rng_start, src_start)
        end_val = min(rng_end, src_start + length - 1)
        return_values.append((start_val + move, end_val + move))
        return return_values
    return [seed_range]
    

seed_line = lines[0][len('seeds: '):]
seed_starts = [int(a) for a in seed_line.split(' ')]
current_locations = []
for i in range(len(seed_starts)//2):
    seed_starts[i] -= i
    start = seed_starts[i*2]
    length = seed_starts[i*2+1]
    current_locations.append((start, start + length-1))
        
loc = 3
while loc < len(lines):
    mappings = []
    while loc < len(lines) and lines[loc] != '':
        dest_start, src_start, length = lines[loc].split(' ')
        mappings.append((int(dest_start), int(src_start), int(length))) 
        loc += 1
    loc += 2
    
    new_current_locations = []
    for rng in current_locations:
        new_current_locations.extend(apply_mappings(mappings, rng))
    current_locations = new_current_locations

print("Part 2", min(s[0] for s in current_locations))
