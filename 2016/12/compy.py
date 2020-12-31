#!/usr/bin/env python3

foo = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0
}

memory = []
with open('input.txt', 'r') as f:
    for line in f:
        memory.append(line.strip().split())

def simulate(registers):
    pc = 0
    while 0 <= pc < len(memory):
        inst = memory[pc]
        if inst[0] == 'cpy':
            pc += 1
            if inst[1].isnumeric():
                registers[inst[2]] = int(inst[1])
            else:
                registers[inst[2]] = registers[inst[1]]
        elif inst[0] == 'inc':
            registers[inst[1]] += 1
            pc += 1
        elif inst[0] == 'dec':
            registers[inst[1]] -= 1
            pc += 1
        elif inst[0] == 'jnz':
            if inst[1].isnumeric():
                value = int(inst[1])
            else:
                value = registers[inst[1]]
            if value != 0:
                pc += int(inst[2])
            else:
                pc += 1
        else:
            print("We shouldn't get here", inst)
            assert False
    return registers

reg = simulate({'a': 0, 'b': 0,'c': 0, 'd': 0})
print("Part 1:", reg['a'])
reg = simulate({'a': 0, 'b': 0,'c': 1, 'd': 0})
print("Part 2:", reg['a'])


