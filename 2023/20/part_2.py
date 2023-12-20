#!/usr/bin/env python3
from collections import Counter, defaultdict, deque, namedtuple
import sys
import math 

registry = {}
inverters = {}

queue = deque()
def send_message(source, dest, value):
    global queue 
    # print(f"Message:{source}:{dest}:{value}")
    queue.append((source, dest, value))

class Broadcast:
    def __init__(self, name, destinations):
        self.outputs = destinations
        self.low_pulses = 0
        self.high_pulses = 0
        self.name = name 
        
    def send(self, source, hi_low):
        if hi_low == 1:
            self.high_pulses += len(self.outputs)
        else:
            self.low_pulses += len(self.outputs)
        for dest in self.outputs:
            send_message(self.name, dest, hi_low)
            
class FlipFlip:
    def __init__(self, name, destinations):
        self.outputs = destinations
        self.low_pulses = 0
        self.high_pulses = 0
        self.name = name
        self.is_on = 0
      
    def send(self, source, hi_low):
        if hi_low == 0:
            self.is_on = 1 - self.is_on
            if self.is_on:
                self.high_pulses += len(self.outputs)
            else:
                self.low_pulses += len(self.outputs)   
            for dest in self.outputs:
                send_message(self.name, dest, self.is_on)
               
            
class Inverter:
    def __init__(self, name, destinations):
        self.outputs = destinations
        self.sources = {}
        self.low_pulses = 0
        self.high_pulses = 0
        self.name = name

    def add_source(self, source):
        self.sources[source] = 0
        
    def send(self, source, hi_low):
        self.sources[source] = hi_low
        if sum(self.sources.values()) == len(self.sources):
            for dest in self.outputs:
                send_message(self.name, dest, 0)
                self.low_pulses += 1
        else:
            for dest in self.outputs:
                send_message(self.name, dest, 1)
                self.high_pulses += 1
            
        

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
for line in lines:
    node, inputs = line.split('->')
    node = node.strip()
    dests = [i.strip() for i in inputs.split(',')]
    if node[0] == '%':
        n = FlipFlip(node[1:], dests)
        registry[node[1:]] = n 
    elif node[0] == '&':
        n = Inverter(node[1:], dests)
        registry[node[1:]] = n 
        inverters[node[1:]] = n
    else:
        assert node == 'broadcaster'
        registry[node] = Broadcast(node, dests)
        
# Now, wire up the inverters
for line in lines:
    node, inputs = line.split('->')
    node = node.strip()
    if node[0] != 'b':
        node = node[1:]
    dests = [i.strip() for i in inputs.split(',')]
    for d in dests:
        if d in inverters:
            inverters[d].add_source(node)
     
presses = 0
rx_seen_low = False
ft_signals = defaultdict(list)
ft_node = registry['ft']
# Run 5000 cycles to see the pattern
while not rx_seen_low and presses < 5000:
    send_message('button', 'broadcaster', 0)
    presses += 1
    while(len(queue)) > 0:
        (source, dest, value) = queue.popleft()
        if dest in registry:
            if dest == 'ft':
                if ft_node.sources[source] != value:
                    ft_signals[source].append((presses, value))
            registry[dest].send(source, value)
        else:
            if dest == 'rx' and value == 0:
                rx_seen_low = True
        
    if presses % 100000 == 0:
        print(ft_signals)

answer = 1
for source in ft_signals:
    cycle_time = ft_signals[source][0][0]
    answer = (answer * cycle_time)//math.gcd(answer, cycle_time)
    
print("Part 2", answer)

