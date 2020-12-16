#!/usr/bin/env python3

starting_numbers = [14, 1, 17, 0, 3, 20]
turn = 1
last_used = {}
for n in starting_numbers[:-1]:
    last_used[n] = turn
    turn += 1

turn += 1
last = starting_numbers[-1]
for _ in range(30000000 - len(starting_numbers)):
    # print(last, turn, last in last_used, last_used.get(last, "N/A"))
    if last in last_used:
        spoken = (turn - 1) - last_used[last]
    else:
        spoken = 0
    last_used[last] = turn - 1
    last = spoken
    turn = turn + 1

print(spoken)
