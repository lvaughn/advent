#!/usr/bin/env python3

import re

VALUE_A = 61
VALUE_B = 17


class Bot:
    def __init__(self, id, high, low):
        self.high = high
        self.low = low
        self.id = id
        self.has_run = False
        self.inputs = []

    def add_input(self, value):
        self.inputs.append(value)
        if len(self.inputs) == 2:
            assert not self.has_run
            if VALUE_A in self.inputs and VALUE_B in self.inputs:
                print("Bot {} compared {} and {} ({})".format(self.id, VALUE_A, VALUE_B, self.inputs))
            if self.high[0] == 'bot':
                bots[self.high[1]].add_input(max(self.inputs))
            else:
                output_bins[self.high[1]] = max(self.inputs)
            if self.low[0] == 'bot':
                bots[self.low[1]].add_input(min(self.inputs))
            else:
                output_bins[self.low[1]] = min(self.inputs)
            self.has_run = True


bots = {}
output_bins = {}
starting = []

value_re = re.compile(r'value\s+(\d+).*\s(\d+)')
bot_re = re.compile(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)')

with open('input.txt', 'r') as f:
    for line in f:
        if line.startswith('value'):
            m = value_re.match(line)
            assert m is not None
            starting.append((m[2], int(m[1])))
        else:
            m = bot_re.match(line)
            assert m is not None
            id = m[1]
            low = (m[2], m[3])
            high = (m[4], m[5])
            bot = Bot(id, high, low)
            bots[id] = bot
    for bot, value in starting:
        bots[bot].add_input(value)

print("Part 2: {}".format(output_bins['0'] * output_bins['1'] * output_bins['2']))
