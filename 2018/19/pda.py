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

# Part 1
reg = [0, 0, 0, 0, 0, 0]
while 0 <= reg[ip] < len(memory):
    inst, vars = memory[reg[ip]]
    inst.func(*vars)
    reg[ip] += 1
print("Part 1:", reg[0])

# Part 1
reg = [1, 0, 0, 0, 0, 0]
while 0 <= reg[ip] < len(memory):
    inst, vars = memory[reg[ip]]
    inst.func(*vars)
    reg[ip] += 1

print("Part 2:", reg[0])


