#!/usr/bin/env python3
import sys

def get_distance(gal_a, gal_b, empty_rows, empty_cols, factor):
    min_row = min(gal_a[0], gal_b[0])
    max_row = max(gal_a[0], gal_b[0])
    min_col = min(gal_a[1], gal_b[1])
    max_col = max(gal_a[1], gal_b[1])
    
    extra_col = len([a for a in empty_cols if min_col < a < max_col])
    extra_row = len([a for a in empty_rows if min_row < a < max_row])
    
    return (max_col - min_col) + (extra_col*(factor-1)) + (max_row - min_row) + (extra_row*(factor-1))

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
empty_rows = []
empty_cols = []

for row, l in enumerate(lines):
    if '#' not in l:
        empty_rows.append(row)
        
for col in range(len(lines[0])):
    has_galaxy = False
    for l in lines:
        if l[col] == '#':
            has_galaxy = True
            break
    if not has_galaxy:
        empty_cols.append(col)
        
galaxies = []
for row, l in enumerate(lines):
    for col, ch in enumerate(l):
        if ch == '#':
            galaxies.append((row, col))
                             
for i in range(len(galaxies) - 1):
    a = galaxies[i]
    for b in galaxies[i+1:]:
        answer += get_distance(a, b, empty_rows, empty_cols, 2)
    

print("Part 1", answer)
# 13479249

answer = 0

for i in range(len(galaxies) - 1):
    a = galaxies[i]
    for b in galaxies[i+1:]:
        answer += get_distance(a, b, empty_rows, empty_cols, 1000000)
        
print("Part 2", answer)
# 850551794
