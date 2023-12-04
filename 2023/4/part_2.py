#!/usr/bin/env python3
from collections import Counter, defaultdict, deque, namedtuple
import re
import sys

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

line_re = re.compile(r'Card\s+(\d+):\s*(.+)\|(.+)')
cards = [0]
last_card = 0
for line in lines:
    m = line_re.match(line)
    assert(int(m.group(1)) == last_card + 1)
    last_card += 1
    winning_numbers = re.split(r'\s+', m.group(2).strip())
    my_numbers = re.split(r'\s+', m.group(3).strip())
    matches = [m for m in my_numbers if m in winning_numbers]
    cards.append(len(matches))
    
queue = deque(range(1, last_card+1))
while len(queue) > 0:
    answer += 1
    card = queue.popleft()
    queue.extend(range(card+1, card + cards[card]+1))

print("Part 2", answer)

