#!/usr/bin/env python3

from collections import namedtuple
from pprint import pprint

Instruction = namedtuple("Instruction", ["op", "a", "b"])

sections = []
sec = []
with open('input.txt', 'r') as infile:
    for line in infile:
        tokens = line.strip().split()
        if len(tokens) == 2:
            op, arg1 = tokens
            arg2 = None
        else:
            op, arg1, arg2 = tokens
            if arg2.isnumeric() or arg2.startswith('-'):
                arg2 = int(arg2)
        inst = Instruction(op, arg1, arg2)
        if sec and inst.op == 'inp':
            sections.append(sec)
            sec = []
        sec.append(inst)
    sections.append(sec)


def get_val(registers, val):
    if type(val) == int:
        return val
    return registers[val]


CACHE = {}


def eval_section(sec_number, z, w):
    key = f"sn={sec_number},z={z},w={w}"
    if key in CACHE:
        return CACHE[key]
    registers = {'x': 0, 'y': 0, 'w': w, 'z': z}
    instructions = sections[sec_number]
    for inst in instructions:
        if inst.op == 'inp':
            registers[inst.a] = w
        elif inst.op == 'add':
            registers[inst.a] += get_val(registers, inst.b)
        elif inst.op == 'mul':
            registers[inst.a] *= get_val(registers, inst.b)
        elif inst.op == 'div':
            registers[inst.a] //= get_val(registers, inst.b)
        elif inst.op == 'mod':
            registers[inst.a] %= get_val(registers, inst.b)
        elif inst.op == 'eql':
            if registers[inst.a] == get_val(registers, inst.b):
                registers[inst.a] = 1
            else:
                registers[inst.a] = 0
        else:
            assert False

    CACHE[key] = registers['z']
    return registers['z']


TOP_CACHE = {}


def solve_from(level, z):
    key = f"lvl={level},z={z}"
    if key in TOP_CACHE:
        return TOP_CACHE[key]
    result = None
    #for w in range(9, 0, -1):
    for w in range(1, 10):
        res = eval_section(level, z, w)
        if level == len(sections) - 1:
            if res == 0:
                result = [w]
                break
        else:
            new_sol = solve_from(level + 1, res)
            if new_sol:
                result = [w] + new_sol
                break
    TOP_CACHE[key] = result
    return result


print(''.join(str(n) for n in solve_from(0, 0)))
