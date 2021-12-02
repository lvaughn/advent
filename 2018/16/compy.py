#!/usr/bin/env python3

from collections import namedtuple

Inst = namedtuple('Inst', ['name', 'func'])
Test = namedtuple('Test', ['before', 'inst', 'after'])

reg = [0] * 4


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

with open('input.txt', 'r') as f:
    tests = []
    program = []
    line = f.readline()
    while line.strip() != '':
        if line.startswith("Before:"):
            before = eval(line[8:])
            instruction = [int(a) for a in f.readline().split()]
            line = f.readline()
            after = eval(line[8:])
            tests.append(Test(before, instruction, after))
            f.readline()
        line = f.readline()

    for line in f:
        if line.strip() != '':
            program.append([int(a) for a in line.split()])

possible = {}
for inst in instructions:
    possible[inst.name] = set(range(16))

n_with_three = 0
for test in tests:
    matches = 0
    for inst in instructions:
        reg = list(test.before)
        inst.func(*test.inst[1:])
        if reg == test.after:
            matches += 1
        else:
            possible[inst.name].discard(test.inst[0])
    if matches >= 3:
        n_with_three += 1

print("Part 1", n_with_three)

decoder = {}
while len(decoder) != 16:
    to_remove = []
    for inst in instructions:
        if len(possible[inst.name]) == 1:
            value = possible[inst.name].pop()
            decoder[value] = inst
            for s in possible.values():
                s.discard(value)

print(decoder)
reg = [0, 0, 0, 0]
for line in program:
    inst = decoder[line[0]]
    inst.func(*line[1:])

print("Part 2", reg[0])

