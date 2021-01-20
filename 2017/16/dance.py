#!/usr/bin/env python3

from string import ascii_lowercase

with open('input.txt', 'r') as f:
    all_moves = f.read()


def do_dance(dancers):
    for move in all_moves.strip().split(','):
        if move.startswith('s'):
            dist = int(move[1:])
            break_pt = len(dancers) - dist
            dancers = dancers[break_pt:] + dancers[:break_pt]
        elif move.startswith('x'):
            a, b = [int(x) for x in move[1:].split('/')]
            tmp = dancers[a]
            dancers[a] = dancers[b]
            dancers[b] = tmp
        elif move.startswith('p'):
            a_char, b_char = move[1:].split('/')
            a = dancers.index(a_char)
            b = dancers.index(b_char)
            tmp = dancers[a]
            dancers[a] = dancers[b]
            dancers[b] = tmp
    return dancers


dancers = do_dance([c for c in ascii_lowercase[:16]])
print('Part 1:', ''.join(dancers))

dancers = [c for c in ascii_lowercase[:16]]
key = ''.join(dancers)
first_seen = {}

rounds = 0
while key not in first_seen:
    first_seen[key] = rounds
    dancers = do_dance(dancers)
    rounds += 1
    key = ''.join(dancers)

print(key, rounds)
print([a for a in first_seen.items() if a[1] == 1000000000 % rounds])
