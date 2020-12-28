#!/usr/bin/env python3

reg = {'a': 1, 'b': 0}
pc = 0
memory = []
with open('input.txt', 'r') as f:
    for line in f:
        parsed = [line[:3]]
        for arg in line[4:].split(','):
            arg = arg.strip()
            if arg[0] in ['+', '-']:
                arg = int(arg)
            parsed.append(arg)
        memory.append(parsed)

while 0 <= pc < len(memory):
    i = memory[pc]
    if i[0] == 'hlf':
        reg[i[1]] = reg[i[1]] // 2
        pc += 1
    elif i[0] == 'tpl':
        reg[i[1]] *= 3
        pc += 1
    elif i[0] == 'inc':
        reg[i[1]] += 1
        pc += 1
    elif i[0] == 'jmp':
        pc += i[1]
    elif i[0] == 'jie':
        if reg[i[1]] % 2 == 0:
            pc += i[2]
        else:
            pc += 1
    elif i[0] == 'jio':
        if reg[i[1]] == 1:
            pc += i[2]
        else:
            pc += 1
    else:
        print("Unknown instruction", i)
        assert False


print(reg)