#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    memory = [int(a) for a in f]

steps, pc = 0, 0
while 0 <= pc < len(memory):
    to_move = memory[pc]
    memory[pc] += 1
    steps += 1
    pc += to_move

print('Part 1', steps)

with open('input.txt', 'r') as f:
    memory = [int(a) for a in f]

steps, pc = 0, 0
while 0 <= pc < len(memory):
    to_move = memory[pc]
    if to_move >= 3:
        memory[pc] -= 1
    else:
        memory[pc] += 1
    steps += 1
    pc += to_move

print('Part 2', steps)