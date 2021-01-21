#!/usr/bin/env python3

import re
from collections import defaultdict

memory = []
with open('input.txt', 'r') as f:
    inst_re = re.compile(r'(\w{3})\s+(\w)\s+(.*)')
    for line in f:
        m = inst_re.match(line)
        if m[3].startswith('-') or m[3].isnumeric():
            memory.append((m[1], m[2], int(m[3])))
        else:
            memory.append((m[1], m[2], m[3]))

registers = defaultdict(int)
def get_val(val):
    if type(val) == int:
        return val
    else:
        return registers[val]

last_played = None
recovered = None
pc = 0
while recovered is None:
    instruction = memory[pc]
    inst = instruction[0]
    arg1 = instruction[1]
    arg2 = instruction[2]
    if inst == 'snd':
        last_played = registers[arg1]
        pc += 1
    elif inst == 'set':
        registers[arg1] = get_val(arg2)
        pc += 1
    elif inst == 'add':
        registers[arg1] += get_val(arg2)
        pc += 1
    elif inst == 'mul':
        registers[arg1] *= get_val(arg2)
        pc += 1
    elif inst == 'mod':
        registers[arg1] = registers[arg1] % get_val(arg2)
        pc += 1
    elif inst == 'rcv':
        if get_val(arg1) != 0:
            recovered = last_played
        pc += 1
    elif inst == 'jgz':
        if registers[arg1] > 0:
            pc += get_val(arg2)
        else:
            pc += 1

print(recovered)
