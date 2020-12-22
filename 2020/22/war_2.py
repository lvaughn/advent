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


def play_war(a_deck, b_deck):
    states_seen = set()
    while len(a_deck) > 0 and len(b_deck) > 0:
        key = (tuple(a_deck), tuple(b_deck))
        if key in states_seen:
            return 1, a_deck
        states_seen.add(key)
        a = a_deck.popleft()
        b = b_deck.popleft()
        if a <= len(a_deck) and b <= len(b_deck):
            winner, _ = play_war(deque(list(a_deck)[:a]), deque(list(b_deck)[:b]))
            if winner == 1:
                a_deck.append(a)
                a_deck.append(b)
            else:
                b_deck.append(b)
                b_deck.append(a)
        else:
            if a > b:
                a_deck.append(a)
                a_deck.append(b)
            else:
                b_deck.append(b)
                b_deck.append(a)
    if len(a_deck) > 0:
        return 1, a_deck
    return 2, b_deck


winner, winning_deck = play_war(my_deck, crab_deck)
print(winner, winning_deck)
answer = 0
for i in range(len(winning_deck)):
    answer += winning_deck[i] * (len(winning_deck) - i)
print(answer)
