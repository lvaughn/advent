#!/usr/bin/env python3
#from string import ascii_uppercase, ascii_lowercase
from collections import Counter, defaultdict, deque, namedtuple
#from itertools import count, product, permutations, combinations, combinations_with_replacement
#from sortedcontainers import SortedSet, SortedDict, SortedList
#import numpy as np
import re
#import pprint
import sys
#import heapq

State = namedtuple('State', ['locations', 'time_left', 'flow_rate', 'flowed', 'open_valves'])

def get_key(state: State) -> tuple:
    return (state.locations, state.open_valves)

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

#queue = deque([State(('AA', 'AA'), 26, 0, 0, frozenset())])
start_state = State(('AA', 'AA'), 26, 0, 0, frozenset())
current_queue = defaultdict(list)
current_queue[get_key(start_state)].append(start_state)
max_rate = sum(flow_rates.values())
best_flow = -1
steps = 0
#visited = {get_key(queue[0]): 0}
new_queue = defaultdict(list)
while len(current_queue) > 0:
    for state in current_queue:
        steps += 1
        #print(state, current_queue[state])
        ls = sorted(current_queue[state], key=lambda x: x.flowed, reverse=True)
        locations, time_left, flow_rate, flowed, open_valves = ls[0]
        my_loc, e_loc = locations
        #print(open_valves, flow_rate)
        if steps % 100000 == 0:
            print("LGV", steps, time_left, best_flow, flow_rate, len(new_queue))
        if time_left == 0:
            if flowed > best_flow:
                best_flow = flowed
            continue
        if flow_rate == 0 and time_left < 20:
            continue
        if flow_rate < 40 and time_left < 15:
            continue
        if flow_rate < 80 and time_left < 10:
            continue
        if flow_rate < 100 and time_left < 7:
            continue

        flowed += flow_rate
        if flow_rate == max_rate: # Everything is open that can be
            result = (time_left - 1) * flow_rate + flowed
            if result > best_flow:
                best_flow = result
            # queue.append(State(loc, time_left - 1, flow_rate, flowed, open_valves))
            continue

        # If this can't do better than we've seen, give up now
        best_possible = flowed + (time_left-1) * max_rate
        if best_possible < best_flow:
            continue

        my_moves = []
        if my_loc not in open_valves and flow_rates[my_loc] > 0:
            new_flow_rate = flow_rate + flow_rates[my_loc]
            my_moves.append((my_loc, flow_rates[my_loc], frozenset([my_loc])))
        # Now check all moves
        for dest in connected[my_loc]:
            my_moves.append((dest, 0, frozenset()))
        if e_loc not in open_valves and flow_rates[e_loc] > 0:
            e_improve = flow_rates[e_loc]
            for new_my_loc, flow_imp, new_opens in my_moves:
                if e_loc in new_opens:
                    continue # WE both opened them
                new_flow = flow_rate + e_improve + flow_imp
                new_valves = open_valves | new_opens | frozenset([e_loc])
                locs = tuple(sorted([new_my_loc, e_loc]))
                new_state = State(locs, time_left - 1, new_flow, flowed, new_valves)
                key = get_key(new_state)
                new_queue[key].append(new_state)
                    # queue.append(new_state)
        for dest in connected[e_loc]:
            for new_my_loc, flow_imp, new_opens in my_moves:
                new_flow = flow_rate + flow_imp
                locs = tuple(sorted([new_my_loc, dest]))
                new_state = State(locs, time_left-1, new_flow, flowed, open_valves | new_opens)
                #print("Adding", State(-flowed, new_my_loc, dest, time_left-1, new_flow, flowed, open_valves + new_opens))
                key = get_key(new_state)
                new_queue[key].append(new_state)
    current_queue = new_queue
    new_queue = defaultdict(list)
    print("LOOPING", len(current_queue))
print("Part 2", best_flow)
