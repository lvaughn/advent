#!/usr/bin/env python3

from collections import defaultdict, deque
import sys

reverse_subs = {}
starting = ''
max_sub = -1
with open('input.txt', 'r') as f:
    for line in f:
        idx = line.find('=>')
        if idx > 0:
            start = line[:idx].strip()
            end = line[idx+2:].strip()
            assert end not in reverse_subs
            reverse_subs[end] = start
            max_sub = max(max_sub, len(end))
        else:
            striped = line.strip()
            if striped != '':
                starting = striped

queued = set([starting])
queue = deque([(starting, 0)])
while len(queue) > 0:
    next, steps = queue.popleft()
    for i in range(min(len(next), max_sub+5)):
        for j in range(min(max_sub, len(next)-i)):
            s = next[i:i+j+1]
            if s in reverse_subs:
                new_str = next[:i] + reverse_subs[s] + next[i+j+1:]
                if new_str == 'e':
                    print("Found it", steps + 1)
                    sys.exit(0)
                if new_str not in queued and 'e' not in new_str:
                    queued.add(new_str)
                    queue.append((new_str, steps + 1))

