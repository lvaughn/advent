#!/usr/bin/env python3

memory = []
with open('input.txt', 'r') as f:
    for line in f:
        memory.append(line.strip().split())
        memory[-1].append(False)

toggle_map = {
    'cpy': 'jnz',
    'inc': 'dec',
    'dec': 'inc',
    'jnz': 'cpy',
    'tgl': 'inc'
}


def isNumber(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def simulate(registers):
    pc = 0
    while 0 <= pc < len(memory):
        inst = memory[pc]
        cmd = inst[0]
        if inst[-1]:
            cmd = toggle_map[cmd]
        #print(pc, cmd, inst, registers)
        if cmd == 'cpy':
            pc += 1
            if isNumber(inst[2]):
                continue
            if isNumber(inst[1]):
                registers[inst[2]] = int(inst[1])
            else:
                registers[inst[2]] = registers[inst[1]]
        elif cmd == 'inc':
            registers[inst[1]] += 1
            pc += 1
        elif cmd == 'dec':
            registers[inst[1]] -= 1
            pc += 1
        elif cmd == 'jnz':
            if isNumber(inst[1]):
                value = int(inst[1])
            else:
                value = registers[inst[1]]
            if value != 0:
                if isNumber(inst[2]):
                    jump_val = int(inst[2])
                else:
                    jump_val = registers[inst[2]]
                pc += jump_val
            else:
                pc += 1
        elif cmd == 'tgl':
            if isNumber(inst[1]):
                value = int(inst[1])
            else:
                value = registers[inst[1]]
            loc = pc + value
            if 0 <= loc < len(memory):
                memory[loc][-1] = not memory[loc][-1]
            pc += 1
        else:
            print("We shouldn't get here", inst)
            assert False
        #print(memory)
    return registers


reg = simulate({'a': 7, 'b': 0, 'c': 0, 'd': 0})
print("Part 1:", reg['a'])

# Reset memory
for m in memory:
    m[-1] = False
reg = simulate({'a': 12, 'b': 0, 'c': 0, 'd': 0})
print("Part 2:", reg['a'])