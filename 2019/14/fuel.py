#!/usr/bin/env python3

import sys
import re
import math
from collections import defaultdict, deque

requirements = defaultdict(list)
can_produce = defaultdict(list)
output_amounts = {}
with open(sys.argv[1], 'r') as infile:
    component_re = re.compile(r'\s*(\d+)\s+(\w+)')
    for l in infile:
        idx = l.index('=>')
        m = component_re.match(l[idx+2:])
        output_name = m[2]
        output_amounts[output_name] = int(m[1])
        for input in l[:idx].split(','):
            m = component_re.match(input)
            requirements[output_name].append((m[2], int(m[1])))
            can_produce[m[2]].append(output_name)

queue = deque(['ORE'])
production_order = []
while len(queue) > 0:
    input = queue.popleft()
    for output in can_produce[input]:
        if input in production_order:
            loc = production_order.index(input)
            production_order.insert(loc, output)
        else:
            production_order.append(input)
        if output not in queue:
            queue.append(output)

still_need = defaultdict(int)
still_need['FUEL'] = 1

print(production_order)
while len(still_need) > 1 or 'FUEL' in still_need:
    print(still_need)
    for output in reversed(production_order):
        if output == 'ORE':
            continue
        if output in still_need:
            # Figure out what we need to get this
            n_produced = output_amounts[output]
            needed = still_need[output]
            batches = math.ceil(needed/n_produced)
            for req in requirements[output]:
                still_need[req[0]] += batches * req[1]
            del still_need[output]
            break

print(still_need)
print(still_need['ORE'])