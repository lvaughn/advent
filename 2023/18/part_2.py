#!/usr/bin/env python3
from collections import Counter, defaultdict, deque, namedtuple
import pprint
import sys

class LineSegment:
    def __init__(self, direction, x_start, x_end, y_start, y_end, inside_dir):
        self.x_range = (x_start, x_end)
        self.y_range = (y_start, y_end)
        self.direction = direction
        self.inside_dir = inside_dir
        
    def __repr__(self):
        return f"LineSegment(dir={self.direction} x={self.x_range} y={self.y_range} inside={self.inside_dir})"

def get_vertical_crosses(y, vertical_lines):
    x_crosses = []
    for x in vertical_lines:
        for segment in vertical_lines[x]:
            start, end = segment.y_range
            if start <= y <= end:
                x_crosses.append(segment)
                
    return x_crosses

def get_area_for_y(y_min, y_max, vertical_lines):
    height = y_max - y_min + 1
    result = 0
    lines = sorted(get_vertical_crosses(y_min + 1, vertical_lines), key=lambda x: x.x_range)

    assert len(lines) % 2 == 0
    for i in range(len(lines)//2):
        first_line = lines[i*2]
        second_line = lines[i*2+1]
        assert first_line.inside_dir == 1
        assert second_line.inside_dir == -1
        width = second_line.x_range[0] - first_line.x_range[0] + 1
        result += width * height
    return result

def get_area_for_horizontal(y, horizontal_lines, vertical_lines):
    # print(f"Getting horizontal area for {y}")
    endpoint_lines = sorted(get_vertical_crosses(y, vertical_lines), key=lambda x: x.x_range)
    segments = horizontal_lines[y]
    result = 0
    in_area = False
    for v_line in endpoint_lines:
        # print(f"   in={in_area} {v_line}")
        if in_area:
            x_loc = v_line.x_range[0]
            segments_here = [s for s in segments if s.x_range[0] == x_loc]
            assert len(segments_here) < 2
            if v_line.inside_dir == 1 or len(segments_here) == 1:
                # print("       extending")
                pass # We keep going
            else: 
                in_area = False 
                x_end = v_line.x_range[0]
                # print(f"   end={x_end} start={x_start} adding={x_end - x_start + 1}")
                result += x_end - x_start + 1
        else:
            if v_line.inside_dir == 1:
                in_area = True 
                x_start = v_line.x_range[0]

    # print(f"Returning result {result}")
    return result 
    

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
x, y = 0, 0

horizontal_lines = defaultdict(list)
vertical_lines = defaultdict(list)

min_y =  min_x = 99999999999
max_x = max_y = -999999999
last_dir = '3' # Somewhat bogus
last_inside_dir = 1
for l in lines:
    min_x = min(x, min_x)
    min_y = min(y, min_y)
    max_x = max(x, max_x)
    max_y = max(y, max_y)
    dir, amount, color = l.split(' ')
    inst = color.strip('()#')
    dist = int(inst[:5], 16)
    dir = inst[-1]
    # print(f"LGV: dist={dist} dir={dir} x={x} y={y} last_dir={last_dir} last_inside={last_inside_dir}")
    # 0 means R, 1 means D, 2 means L, and 3 means U.
    if dir == '0':
        line_start = x 
        line_end = x+dist 
        if last_dir == '3': # up to right
            inside_dir = last_inside_dir
        else:  # came from "down"
            inside_dir = -1 * last_inside_dir
        segment = LineSegment(dir, line_start, line_end, y, y, inside_dir)
        horizontal_lines[y].append(segment)
        x = line_end
        last_dir = dir 
        last_inside_dir = inside_dir
    elif dir == '1': 
        line_start = y
        line_end = y + dist
        if last_dir == '2': # left to down 
            inside_dir = last_inside_dir
        else:
            inside_dir = -1 * last_inside_dir
        segment = LineSegment(dir, x, x, line_start, line_end, inside_dir)
        vertical_lines[x].append(segment)
        y = line_end 
        last_dir = dir 
        last_inside_dir = inside_dir
    elif dir == '2':
        line_start =  x - dist 
        line_end = x 
        if last_dir == '1': # down to left
            inside_dir = last_inside_dir
        else:  # came from "up"
            assert last_dir == '3'
            inside_dir = -1 * last_inside_dir
        segment = LineSegment(dir, line_start, line_end, y, y, inside_dir)
        horizontal_lines[y].append(segment)
        x = line_start
        last_dir = dir 
        last_inside_dir = inside_dir
    elif dir == '3':
        line_start = y - dist  
        line_end = y 
        if last_dir == '0': 
            inside_dir = last_inside_dir
        else:
            inside_dir = -1 * last_inside_dir
        segment = LineSegment(dir, x, x, line_start, line_end, inside_dir)
        vertical_lines[x].append(segment)
        y = line_start 
        last_dir = dir 
        last_inside_dir = inside_dir
    # print(last_dir, last_inside_dir, segment)
        
# print(min_x, max_x, min_x, max_y)
hor_lines = sorted(horizontal_lines.keys())

answer = 0

for i in range(len(hor_lines) - 1):
    # Handle horizontal line
    answer += get_area_for_y(hor_lines[i] + 1, hor_lines[i+1]-1, vertical_lines)
    answer += get_area_for_horizontal(hor_lines[i], horizontal_lines, vertical_lines)
    
    
# Handle last horizontal line
answer += get_area_for_horizontal(hor_lines[-1], horizontal_lines, vertical_lines)

print("Part 2", answer)