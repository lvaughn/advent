#!/usr/bin/env python3

import re
from collections import defaultdict, deque

class Compy:
    def __init__(self, mem):
        self.memory = list(mem)
        self.reg = defaultdict(int)
        self.pc = 0
        self.n_mulls = 0

    def get_value(self, value):
        if type(value) == int:
            return value
        else:
            return self.reg[value]

    def still_in_mem(self):
        return 0 <= self.pc < len(memory)

    def step(self):
        if not self.still_in_mem():
            return
        instruction = memory[self.pc]
        inst = instruction[0]
        arg1 = instruction[1]
        arg2 = instruction[2]
        if inst == 'set':
            self.reg[arg1] = self.get_value(arg2)
            self.pc += 1
        elif inst == 'add':
            self.reg[arg1] += self.get_value(arg2)
            self.pc += 1
        elif inst == 'sub':
            self.reg[arg1] -= self.get_value(arg2)
            self.pc += 1
        elif inst == 'mul':
            self.reg[arg1] *= self.get_value(arg2)
            self.pc += 1
            self.n_mulls += 1
        elif inst == 'jnz':
            if self.get_value(arg1) != 0:
                self.pc += self.get_value(arg2)
            else:
                self.pc += 1
        else:
            print("Unknown instruction", inst)
            assert False

    def run(self):
        while self.still_in_mem():
            self.step()


memory = []
with open('input.txt', 'r') as f:
    inst_re = re.compile(r'(\w{3})\s+(\w)\s+(.*)')
    for line in f:
        m = inst_re.match(line)
        if m[2].startswith('-') or m[2].isnumeric():
            m_2 = int(m[2])
        else:
            m_2 = m[2]
        if m[3].startswith('-') or m[3].isnumeric():
            m_3 = int(m[3])
        else:
            m_3 = m[3]
        memory.append((m[1], m_2, m_3))

c = Compy(memory)
c.run()
print(c.n_mulls)
