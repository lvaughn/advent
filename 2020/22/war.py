#!/usr/bin/env python3

from collections import deque

my_deck = deque()
crab_deck = deque()

with open('input.txt', 'r') as f:
    d = my_deck
    for l in f:
        if l.startswith('Player 1'):
            continue
        elif l.startswith('Player 2'):
            d = crab_deck
        elif l.strip() == '':
            continue
        else:
            d.append(int(l))

while len(my_deck) > 0 and len(crab_deck) > 0:
    my = my_deck.popleft()
    crab = crab_deck.popleft()
    if my > crab:
        my_deck.append(my)
        my_deck.append(crab)
    else:
        crab_deck.append(crab)
        crab_deck.append(my)

winner = my_deck
if len(crab_deck) > len(my_deck):
    winner = crab_deck

answer = 0
for i in range(len(winner)):
    answer += winner[i] * (len(winner) - i)
print(answer)