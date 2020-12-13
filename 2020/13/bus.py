#!/usr/bin/env python3

with open('input.txt', 'r') as infile:
    depart_time = int(infile.readline())
    busses = infile.readline().split(",")

best_bus = None
shortest_wait = 10 * depart_time + 10000

for bus in busses:
    if bus == 'x':
        continue
    bus = int(bus)
    wait_time = bus - (depart_time % bus)
    if wait_time < shortest_wait:
        best_bus = bus
        shortest_wait = wait_time

print(best_bus, shortest_wait, shortest_wait*best_bus)