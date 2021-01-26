#!/usr/bin/env python3

import re
from collections import defaultdict

pre_reqs = defaultdict(set)
done = set()
steps = set()
with open('input.txt', 'r') as f:
    input_re = re.compile(r'Step (\w) must be finished before step (\w) can')
    for line in f:
        m = input_re.match(line)
        pre_reqs[m[2]].add(m[1])
        steps.add(m[1])
        steps.add(m[2])

steps_in_order = []
while len(steps) > 0:
    next_step = 'ZZ'
    for step in steps:
        if len(pre_reqs[step] - done) == 0 and step < next_step:
            next_step = step
    steps.remove(next_step)
    steps_in_order.append(next_step)
    done.add(next_step)

print(''.join(steps_in_order))
