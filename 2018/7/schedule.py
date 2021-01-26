#!/usr/bin/env python3

import re
from collections import defaultdict
from string import ascii_uppercase
base_time = 61
input_file = 'input.txt'
n_workers = 5

# Get times for tasks
time_for_task = {}
for i, ch in enumerate(ascii_uppercase):
    time_for_task[ch] = base_time + i

pre_reqs = defaultdict(set)
done = set()
steps = set()
with open(input_file, 'r') as f:
    input_re = re.compile(r'Step (\w) must be finished before step (\w) can')
    for line in f:
        m = input_re.match(line)
        pre_reqs[m[2]].add(m[1])
        steps.add(m[1])
        steps.add(m[2])

n_steps = len(steps)
working_on = [''] * n_workers
time_left = [0] * n_workers
ticks = -1
while len(done) < n_steps:
    ticks += 1
    # Count down progress
    for i in range(n_workers):
        if time_left[i] > 0:
            time_left[i] -= 1
            if time_left[i] == 0:
                done.add(working_on[i])
                steps.remove(working_on[i])
                working_on[i] = ''

    # Start timers that can
    can_start = [step for step in steps if len(pre_reqs[step]-done) == 0 and step not in working_on]
    can_start.sort()
    for i in range(n_workers):
        if len(can_start) == 0:
            continue
        if working_on[i] == '':
            next_step = can_start[0]
            can_start = can_start[1:]
            time_left[i] = time_for_task[next_step]
            working_on[i] = next_step

print("Time taken", ticks)


