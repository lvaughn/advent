#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    s = ''.join([a.strip() for a in f])
    print(s.count('(') - s.count(')'))

    floor = 0
    for i, ch in enumerate(s):
        if ch == '(':
            floor += 1
        elif ch == ')':
            floor -= 1
            if floor < 0:
                print("Went to basement at pos {}".format(i+1))
                break
        else:
            print("Surprise character", ch)