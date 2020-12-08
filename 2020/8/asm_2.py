#!/usr/bin/env python3

from collections import namedtuple

Instruction = namedtuple('Instruction', ['op', 'arg'])

original_memory = []
with open('input.txt', 'r') as program:
    for line in program:
        parsed = line.split()
        original_memory.append(Instruction(parsed[0], int(parsed[1])))


def test_program(memory):
    visited = set()
    acc = 0
    pc = 0

    while pc not in visited and pc < len(memory):
        visited.add(pc)
        inst = memory[pc]
        if inst.op == 'nop':
            pc += 1
        elif inst.op == 'acc':
            acc += inst.arg
            pc += 1
        elif inst.op == 'jmp':
            pc += inst.arg
    if pc == len(memory):
        return acc
    return None


for i in range(len(original_memory)):
    if original_memory[i].op == 'acc':
        continue
    memory = original_memory[:]
    if memory[i].op == 'jmp':
        memory[i] = Instruction('nop', memory[i].arg)
    elif memory[i].op == 'nop':
        memory[i] = Instruction('jmp', memory[i].arg)
    ans = test_program(memory)
    if ans is not None:
        print(ans)
