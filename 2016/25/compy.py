#!/usr/bin/env python3

memory = []
with open('input.txt', 'r') as f:
    for line in f:
        memory.append(line.strip().split())


def isNumber(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def decodeArg(s, registers):
    if isNumber(s):
        return int(s)
    return registers[s]


def simulate(registers):
    output = []
    pc = 0
    states = set()
    while 0 <= pc < len(memory) and len(output) < 10:
        inst = memory[pc]
        cmd = inst[0]
        if cmd == 'cpy':
            pc += 1
            registers[inst[2]] = decodeArg(inst[1], registers)
        elif cmd == 'inc':
            registers[inst[1]] += 1
            pc += 1
        elif cmd == 'dec':
            registers[inst[1]] -= 1
            pc += 1
        elif cmd == 'jnz':
            value = decodeArg(inst[1], registers)
            if value != 0:
                jump_val = decodeArg(inst[2], registers)
                assert jump_val != 0
                pc += jump_val
            else:
                pc += 1
        elif cmd == 'out':
            output.append(decodeArg(inst[1], registers))
            pc += 1
        else:
            print("We shouldn't get here", inst)
            assert False
    return registers, output


def test_output(out):
    for x in out[0::2]:
        if x != 0:
            return False
    for x in out[1::2]:
        if x != 1:
            return False
    return True


# 2541 too high
start = 1
while True:
    reg, output = simulate({'a': start, 'b': 0, 'c': 0, 'd': 0})
    if len(output) > 1 and (test_output(output) or test_output(output[1:])):
        print("Found it", start, output)
        break
    start += 1
