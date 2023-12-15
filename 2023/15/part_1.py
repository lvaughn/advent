#!/usr/bin/env python3
from collections import defaultdict
import sys

def hash(s):
    answer = 0
    for ch in s:
        answer += ord(ch)
        answer *= 17
        answer = answer % 256
    return answer

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
steps = lines[0].split(',')
for st in steps:
    answer += hash(st)

print("Part 1", answer)

def add_box(move, boxes): 
    label, value = move
    box_no = hash(label)
    ls = boxes[box_no]
    for i in range(len(ls)):
        if label == ls[i][0]:
            ls[i] = move
            return 
    ls.append(move)
    
def remove_box(label, boxes):
    new_ls = []
    for item in boxes[hash(label)]:
        if label != item[0]:
            new_ls.append(item)
    boxes[hash(label)] = new_ls
    
boxes = defaultdict(list)

for step in steps:
    if '=' in step:
        label, value = step.split('=')
        add_box((label, int(value)), boxes)
    else:
        assert '-' in step 
        remove_box(step.strip('-'), boxes)
        
answer = 0
for box_no in range(1, 257):
    ls = boxes[box_no - 1]
    for slot, item in enumerate(ls):
        answer += box_no * (slot + 1) * item[1]
        
print("Part 2", answer)
