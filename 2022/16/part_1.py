#!/usr/bin/env python3
#from string import ascii_uppercase, ascii_lowercase
from collections import Counter, defaultdict, deque, namedtuple
#from itertools import count, product, permutations, combinations, combinations_with_replacement
#from sortedcontainers import SortedSet, SortedDict, SortedList
#import numpy as np
import re
#import pprint
import sys
import heapq

State = namedtuple('State', ['priority', 'location', 'time_left', 'flow_rate', 'flowed', 'open_valves'])

# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

answer = 0
flow_rates = {}
connected = defaultdict(list)
DIGIT_RE = re.compile('(\d+)')
VALVE_RE = re.compile('leads? to valves? (.*)')
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    for l in lines:
        m = DIGIT_RE.search(l)
        valve = l[6:8]
        flow_rates[valve] = int(m[1])
        m = VALVE_RE.search(l)
        for dest in (s.strip() for s in m[1].split(',')):
            connected[valve].append(dest)

queue = [State(0, 'AA', 30, 0, 0, [])]
max_rate = sum(flow_rates.values())
best_flow = -1
steps = 0
while len(queue):
    steps += 1
    pri, loc, time_left, flow_rate, flowed, open_valves = heapq.heappop(queue)
    if steps % 10000 == 0:
        print("LGV", steps, len(queue), time_left, best_flow, flow_rate, max_rate)
    if time_left == 0:
        if flowed > best_flow:
            best_flow = flowed
        continue
    if flow_rate == 0 and time_left < 25:
        continue
    if flow_rate < 40 and time_left < 20:
        continue
    if flow_rate < 50 and time_left < 15:
        continue
    if flow_rate < 80 and time_left < 10:
        continue
    # if flow_rate < 70 and time_left < 5:
    #     continue
    flowed += flow_rate
    if flow_rate == max_rate: # Everything is open that can be
        result = (time_left - 1) * flow_rate + flowed
        if result > best_flow:
            best_flow = result
        # queue.append(State(loc, time_left - 1, flow_rate, flowed, open_valves))
        continue

    # If this can't to better than we've seen, give up now
    best_possible = flowed + (time_left-1) * max_rate
    if best_possible < best_flow:
        continue
    if loc not in open_valves:
        new_flow_rate = flow_rate + flow_rates[loc]
        heapq.heappush(queue, State(-flowed, loc, time_left-1, new_flow_rate, flowed, open_valves + [loc]))
    # Now check all moves
    for dest in connected[loc]:
        heapq.heappush(queue, State(-flowed, dest, time_left - 1, flow_rate, flowed, open_valves))


print("Part 1", best_flow)
