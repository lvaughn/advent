#!/usr/bin/env python3

from collections import namedtuple

State = namedtuple("State", ['a_score', 'b_score', 'a_pos', 'b_pos', 'turn'])

totals = [0] * 10
for i in range(1,4):
    for j in range(1, 4):
        for k in range(1,4):
            totals[i + j + k] += 1

pos_a = 6
pos_b = 8

state = State(0, 0, pos_a, pos_b, 0)
states = {state: 1}

a_wins = 0
b_wins = 0
while len(states) > 0:
    state, count = states.popitem()
    score_a, score_b, pos_a, pos_b, turn = state

    if turn == 0: # a goes
        for roll in range(3, 10):
            new_pos_a = ((pos_a - 1 + roll) % 10) + 1
            new_score_a = score_a + new_pos_a
            if new_score_a >= 21:
                a_wins += totals[roll] * count
            else:
                new_state = State(new_score_a, score_b, new_pos_a, pos_b, 1)
                if new_state in states:
                    states[new_state] += totals[roll] * count
                else:
                    states[new_state] = totals[roll] * count
    else: # b goes
        for roll in range(3, 10):
            new_pos_b = ((pos_b - 1 + roll) % 10) + 1
            new_score_b = score_b + new_pos_b
            if new_score_b >= 21:
                b_wins += totals[roll] * count
            else:
                new_state = State(score_a, new_score_b, pos_a, new_pos_b, 0)
                if new_state in states:
                    states[new_state] += totals[roll] * count
                else:
                    states[new_state] = totals[roll] * count


print(max(a_wins, b_wins))