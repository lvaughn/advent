#!/usr/bin/env python3

import re
from collections import defaultdict, deque

class Compy:
    def __init__(self, id, mem):
        self.memory = list(mem)
        self.reg = {} #defaultdict(int)
        self.reg['p'] = id
        self.input_queue = deque()
        self.pc = 0
        self.n_sends = 0
        self.waiting = False

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
        if inst == 'snd':
            self.other.input_queue.append(self.reg[arg1])
            self.n_sends += 1
            self.pc += 1
        elif inst == 'set':
            self.reg[arg1] = self.get_value(arg2)
            self.pc += 1
        elif inst == 'add':
            self.reg[arg1] += self.get_value(arg2)
            self.pc += 1
        elif inst == 'mul':
            self.reg[arg1] *= self.get_value(arg2)
            self.pc += 1
        elif inst == 'mod':
            self.reg[arg1] = self.reg[arg1] % self.get_value(arg2)
            self.pc += 1
        elif inst == 'rcv':
            if len(self.input_queue) > 0:
                self.reg[arg1] = self.input_queue.popleft()
                self.pc += 1
                self.waiting = False
            else:
                self.waiting = True
        elif inst == 'jgz':
            if self.get_value(arg1) > 0:
                self.pc += self.get_value(arg2)
            else:
                self.pc += 1


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

zero = Compy(0, memory)
one = Compy(1, memory)
zero.other = one
one.other = zero
while zero.still_in_mem() or one.still_in_mem():
    if one.waiting and zero.waiting:
        break
    one.step()
    zero.step()



print(one.n_sends)
