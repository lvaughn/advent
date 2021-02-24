#!/usr/bin/env python3

from collections import namedtuple

Inst = namedtuple('Inst', ['name', 'func'])


def addr(a, b, c):
    reg[c] = reg[a] + reg[b]


def addi(a, b, c):
    reg[c] = reg[a] + b


def mulr(a, b, c):
    reg[c] = reg[a] * reg[b]


def muli(a, b, c):
    reg[c] = reg[a] * b


def banr(a, b, c):
    reg[c] = reg[a] & reg[b]


def bani(a, b, c):
    reg[c] = reg[a] & b


def borr(a, b, c):
    reg[c] = reg[a] | reg[b]


def bori(a, b, c):
    reg[c] = reg[a] | b


def setr(a, _, c):
    reg[c] = reg[a]


def seti(a, _, c):
    reg[c] = a


def gtir(a, b, c):
    reg[c] = 1 if a > reg[b] else 0


def gtri(a, b, c):
    reg[c] = 1 if reg[a] > b else 0


def gtrr(a, b, c):
    reg[c] = 1 if reg[a] > reg[b] else 0


def eqir(a, b, c):
    reg[c] = 1 if a == reg[b] else 0


def eqri(a, b, c):
    reg[c] = 1 if reg[a] == b else 0


def eqrr(a, b, c):
    reg[c] = 1 if reg[a] == reg[b] else 0


instructions = [
    Inst('addr', addr),
    Inst('addi', addi),
    Inst('mulr', mulr),
    Inst('muli', muli),
    Inst('banr', banr),
    Inst('bani', bani),
    Inst('borr', borr),
    Inst('bori', bori),
    Inst('setr', setr),
    Inst('seti', seti),
    Inst('gtir', gtir),
    Inst('gtri', gtri),
    Inst('gtrr', gtrr),
    Inst('eqir', eqir),
    Inst('eqri', eqri),
    Inst('eqrr', eqrr),
]

inst_lookup = {i.name: i for i in instructions}

def run_simulation(reg_0):
    global reg
    reg = [reg_0, 0, 0, 0, 0, 0]
    loop_states = set()
    looped = False
    steps = 0
    print("Starting reg[0]=", reg_0)
    while 0 <= reg[ip] < len(memory) and not looped:
        inst, vars = memory[reg[ip]]
        #print("{}: {}({}) {}".format(reg[ip], inst.name, vars, reg))
        inst.func(*vars)
        steps += 1
        # if reg[ip] == 28 and reg[5] != 1:
        #     return True, reg, steps
        if reg[ip] == 28:
            if reg[3] in loop_states:
                print("Last unique", last_unique)
                exit(0)
            else:
                last_unique = reg[3]
                loop_states.add(reg[3])
            print("{}: {}({}) {} ({})".format(reg[ip], inst.name, vars, reg, len(loop_states)))
        reg[ip] += 1
    return looped, reg, steps

memory = []
ip = 0
with open('input.txt', 'r') as f:
    for line in f:
        if line.startswith('#'):
            ip = int(line[4:])
        else:
            inst = inst_lookup[line[:4]]
            vars = [int(a) for a in line[4:].split()]
            memory.append((inst, vars))


n = 9107763
looped = True
for n in range(0, 9107763*2):
    looped, reg, steps = run_simulation(n)
    if not looped:
        print(n, steps)
        #print("Non-loop for {}: reg={}".format(n, reg))
    #n += 1