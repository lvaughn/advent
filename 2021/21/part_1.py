#!/usr/bin/env python3

class Die:
    def __init__(self):
        self.n_rolls = 0
        self.value = 0

    def roll(self):
        result = self.value + 1
        self.value = (self.value + 1) % 100
        self.n_rolls += 1
        return result

    def get_three(self):
        return self.roll() + self.roll() + self.roll()


pos_a = 6
pos_b = 8

score_a = 0
score_b = 0

done = False
die = Die()
while not done:
    pos_a = (((pos_a - 1) + die.get_three()) % 10) + 1
    score_a += pos_a
    if score_a >= 1000:
        print(score_b * die.n_rolls)
        done = True
        break
    pos_b = (((pos_b - 1) + die.get_three()) % 10) + 1
    score_b += pos_b
    if score_b >= 1000:
        print(score_a * die.n_rolls)
        done = True

