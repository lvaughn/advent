#!/usr/bin/env python3

import re

gates = {}

cache = {}
def ev(gate_id):
    if gate_id not in cache:
        cache[gate_id] = gates[gate_id].evaluate()
    return cache[gate_id]

class ConstantGate:
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        if self.value.isnumeric():
            return int(self.value)
        return ev(self.value)

class NotGate:
    def __init__(self, source):
        self.source = source

    def evaluate(self):
        return ~ ev(self.source)

class AndGate:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def evaluate(self):
        if self.a.isnumeric():
            a = int(self.a)
        else:
            a = ev(self.a)
        if self.b.isnumeric():
            b = int(self.b)
        else:
            b = ev(self.b)
        return a & b


class OrGate:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def evaluate(self):
        if self.a.isnumeric():
            a = int(self.a)
        else:
            a = ev(self.a)
        if self.b.isnumeric():
            b = int(self.b)
        else:
            b = ev(self.b)
        return a | b

class LShiftGate:
    def __init__(self, source, bits):
        self.source = source
        self.bits = bits

    def evaluate(self):
        return ev(self.source) << self.bits

class RShiftGate:
    def __init__(self, source, bits):
        self.source = source
        self.bits = bits

    def evaluate(self):
        return ev(self.source) >> self.bits

args_re = re.compile(r'([a-z0-9]+)\s+[A-Z]+\s+([a-z0-9]+)')
with open('input.txt', 'r') as f:
    for line in f:
        idx = line.index('->')
        dest = line[idx+2:].strip()
        source = line[:idx]
        if 'NOT' in source:
            source = source[4:].strip()
            gates[dest] = NotGate(source)
        elif 'OR' in source:
            m = args_re.match(source)
            gates[dest] = OrGate(m[1], m[2])
        elif 'AND' in source:
            m = args_re.match(source)
            gates[dest] = AndGate(m[1], m[2])
        elif 'RSHIFT' in source:
            m = args_re.match(source)
            gates[dest] = RShiftGate(m[1], int(m[2]))
        elif 'LSHIFT' in source:
            m = args_re.match(source)
            gates[dest] = LShiftGate(m[1], int(m[2]))
        else:
            gates[dest] = ConstantGate(source.strip())

print(ev('a'))
cache = {}
gates['b'] = ConstantGate('3176')
print(ev('a'))