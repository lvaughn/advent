#!/usr/bin/env python3
from collections import Counter, defaultdict, deque, namedtuple
import numpy as np
import sys

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
    
def trace_beams(x, y, dir, grid):
    global lines
    visited = set()
    
    queue = deque()
    queue.append((x, y, dir))
    while len(queue) > 0:
        key = queue.popleft()
        if key in visited:
            continue 
        visited.add(key)
        (x, y, dir) = key
        # print(x, y, dir, queue)
        if x < 0 or x >= grid.shape[1]:
            continue  
        if y < 0 or y >= grid.shape[1]:
            continue 
        grid[x, y] = True 
        ch = lines[y][x]
        if dir == 'r':
            if ch == '.' or ch == '-':
                queue.append((x+1, y, 'r'))
            elif ch == '/':
                queue.append((x, y-1, 'u'))
            elif ch == '\\': 
                queue.append((x, y+1, 'd'))
            else:
                assert ch == '|'
                queue.append((x, y-1, 'u'))
                queue.append((x, y+1, 'd'))
        if dir == 'l':
            if ch == '.' or ch == '-':
                queue.append((x-1, y, 'l'))
            elif ch == '\\':
                queue.append((x, y-1, 'u'))
            elif ch == '/': 
                queue.append((x, y+1, 'd'))
            else:
                assert ch == '|'
                queue.append((x, y-1, 'u'))
                queue.append((x, y+1, 'd'))   
        if dir == 'u':
            if ch == '.' or ch == '|':
                queue.append((x, y-1, 'u'))
            elif ch == '/':
                queue.append((x+1, y, 'r'))
            elif ch == '\\': 
                queue.append((x-1, y, 'l'))
            else:
                assert ch == '-'
                queue.append((x+1, y, 'r'))
                queue.append((x-1, y, 'l'))
        if dir == 'd':
            if ch == '.' or ch == '|':
                queue.append((x, y+1, 'd'))
            elif ch == '/':
                queue.append((x-1, y, 'l'))
            elif ch == '\\': 
                queue.append((x+1, y, 'r'))
            else:
                assert ch == '-'
                queue.append((x+1, y, 'r'))
                queue.append((x-1, y, 'l'))      
    

width = len(lines[0])
height = len(lines)

seen = np.zeros((width, height), dtype=bool)
trace_beams(0, 0, 'r', seen)

print("Part 1", np.count_nonzero(seen))

answer = -1
for x in range(width):
    seen = np.zeros((width, height), dtype=bool)
    trace_beams(x, 0, 'd', seen)
    answer = max(answer, np.count_nonzero(seen))
    
    seen = np.zeros((width, height), dtype=bool)
    trace_beams(x, height-1, 'u', seen)
    answer = max(answer, np.count_nonzero(seen))
    
for y in range(height):
    seen = np.zeros((width, height), dtype=bool)
    trace_beams(0, y, 'r', seen)
    answer = max(answer, np.count_nonzero(seen))    
    
    seen = np.zeros((width, height), dtype=bool)
    trace_beams(width-1, y, 'l', seen)
    answer = max(answer, np.count_nonzero(seen))  
    
print("Part 2", answer)