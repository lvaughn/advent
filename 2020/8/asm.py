#!/usr/bin/env python3

from collections import namedtuple

Instruction = namedtuple('Instruction', ['op', 'arg'])

memory = []
with open('input.txt', 'r') as program:
    for line in program:
        parsed = line.split()
        memory.append(Instruction(parsed[0], int(parsed[1])))

visited = set()
acc = 0
pc = 0

while pc not in visited:
    visited.add(pc)
    inst = memory[pc]
    if inst.op == 'nop':
        pc += 1
    elif inst.op == 'acc':
        acc += inst.arg
        pc += 1
    elif inst.op == 'jmp':
        pc += inst.arg

print(acc)