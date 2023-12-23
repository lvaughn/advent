#!/usr/bin/env python3
from collections import Counter, defaultdict, deque, namedtuple
import sys

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
height = len(lines)
width = len(lines[1])    
start = (0, 1)
end = (height-1, width-2)

def next_moves(row, col):
    global lines
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_r, new_c = row+dr, col + dc 
        if new_r < 0 or new_r >= height:
            continue 
        if new_c < 0 or new_c >= width:
            continue
        if lines[new_r][new_c] != '#':
            yield (new_r, new_c)
        
def find_reachable(loc, vertexes):
    def helper(l, last_loc):
        if l in vertexes:
            return (l, 1)
        next_step = [location for location in next_moves(l[0], l[1]) if location != last_loc]
        assert len(next_step) == 1, f"next steps for {l} {next_step} {last_loc} {l in vertexes}"
        vert, dist = helper(next_step[0], l)
        return (vert, dist+1)
    return [helper(l, loc) for l in next_moves(loc[0], loc[1])]
        
def find_longest(loc, so_far, total_dist, reachable):
    if loc == end:
        return total_dist
    new_so_far = so_far | {loc}
    longest = -1
    for other, dist in reachable[loc]:
        if other not in so_far:
            longest = max(longest, find_longest(other, new_so_far, total_dist + dist, reachable))
    return longest 
            
        
# Pass to find the vertices
vertices = {start, end}
print(vertices)
for row in range(height):
    for col in range(width):
        if len([(r, c) for (r, c) in next_moves(row, col) if lines[r][c] != '#']) > 2 and lines[row][col] != '#':
            vertices.add((row, col))
            
# print(len(vertices))

reachable = defaultdict(list) # (location, distance)
for v in vertices:
    reachable[v] = find_reachable(v, vertices)
    
print("Part 2", find_longest(start, {start}, 0, reachable))