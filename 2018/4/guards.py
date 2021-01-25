#!/usr/bin/env python3

import re
from collections import defaultdict

with open('input.txt', 'r') as f:
    events = [l.strip() for l in f]
    events.sort()

guard_re = re.compile(r'Guard \#(\d+) begins')
time_re = re.compile(r'[^:]+:(\d+)\]')
current_guard = None
current_sleep = None
sleeps = defaultdict(list)
for e in events:
    m = guard_re.search(e)
    if m is not None:
        current_guard = m[1]
    else:
        m = time_re.match(e)
        if "asleep" in e:
            current_sleep = int(m[1])
        else:
            sleeps[current_guard].append((current_sleep, int(m[1])))

most_sleeping_guard = None
most_sleep = -1
most_sleeping_guard_minute = None

most_slept_minute_guard = None
most_slept_minute = None
most_slept_minute_amount = -1
for guard in sleeps:
    time_asleep = 0
    minutes = [0] * 60
    for sleep, awake in sleeps[guard]:
        time_asleep += awake - sleep
        for i in range(sleep, awake):
            minutes[i] += 1
    best_min = -1
    best = -1
    for minute, val in enumerate(minutes):
        if val > best:
            best_min = minute
            best = val

    if time_asleep > most_sleep:
        most_sleep = time_asleep
        most_sleeping_guard = guard
        most_sleeping_guard_minute = best_min

    if best > most_slept_minute_amount:
        most_slept_minute_guard = guard
        most_slept_minute = best_min
        most_slept_minute_amount = best


print("Part 1", most_sleeping_guard_minute * int(most_sleeping_guard))
print("Part 2", most_slept_minute * int(most_slept_minute_guard))
