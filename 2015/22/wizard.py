#!/usr/bin/env python3

from heapq import heappop, heappush, heapify
from collections import namedtuple
from pprint import pprint
import sys

GameState = namedtuple('GameState', ['manna_spent', 'p_hp', 'b_hp', 'manna', 'shield', 'poison', 'recharge', 'history'])

boss_hp = 71
boss_damage = 10
manna_start = 500
player_start_hp = 50
hard_mode = 1


def boss_turn(state):
    b_hp = state.b_hp
    damage = boss_damage
    manna = state.manna
    if state.poison > 0:
        b_hp -= 3
    if state.shield > 0:
        damage -= 7
    if state.recharge > 0:
        manna += 101

    gs = GameState(state.manna_spent, state.p_hp - damage, b_hp, manna,
                   max(0, state.shield - 1), max(0, state.poison - 1), max(0, state.recharge - 1),
                   state.history)
    return gs


queue = [GameState(0, player_start_hp, boss_hp, manna_start, 0, 0, 0, [])]
heapify(queue)
while len(queue) > 0:
    manna_spent, p_hp, b_hp, manna, shield, poison, recharge, history = heappop(queue)
    damage = 10
    p_hp -= hard_mode
    if poison > 0:
        b_hp -= 3
    if recharge > 0:
        manna += 101
    if boss_hp <= 0:
        print("Found it!", manna_spent, history)
        break
    # Now try all 5 moves
    moves = []
    if manna >= 53:
        boss_hp = b_hp - 4
        if boss_hp <= 0:
            print("Found it!", manna_spent + 53, history + ['MM'])
            break
        move = GameState(manna_spent + 53, p_hp, boss_hp, manna - 53,
                         max(0, shield - 1), max(0, poison - 1), max(0, recharge - 1),
                         list(history) + ['Magic Missile'])
        moves.append(move)
    if manna >= 73:
        boss_hp = b_hp - 2
        player_hp = p_hp + 2
        if boss_hp <= 0:
            print("Found it!", manna_spent + 73, history + ['Drain'])
            break

        move = GameState(manna_spent + 73, player_hp, boss_hp, manna - 73,
                         max(0, shield - 1), max(0, poison - 1), max(0, recharge - 1),
                         list(history) + ['Drain'])
        moves.append(move)
    if manna >= 113 and shield <= 1:
        move = GameState(manna_spent + 113, p_hp, b_hp, manna - 113,
                         6, max(0, poison - 1), max(0, recharge - 1),
                         list(history) + ['Shield'])
        moves.append(move)
    if manna >= 173 and poison <= 1:
        move = GameState(manna_spent + 173, p_hp, b_hp, manna - 173,
                         max(0, shield - 1), 6, max(0, recharge - 1),
                         list(history) + ['Poison'])
        moves.append(move)
    if manna >= 229 and recharge <= 1:
        move = GameState(manna_spent + 229, p_hp, b_hp, manna - 229,
                         max(0, shield - 1), max(0, poison - 1), 5,
                         list(history) + ['Recharge'])
        moves.append(move)
    if len(moves) == 0:
        move = GameState(manna_spent, p_hp, b_hp, manna,
                         max(0, shield - 1), max(0, poison - 1), max(0, recharge - 1),
                         list(history) + ['<Skipped>'])
        moves.append(move)
    for m in moves:
        new_state = boss_turn(m)
        if new_state.b_hp <= 0:
            print("Found it!", new_state.manna_spent, new_state.history)
            sys.exit(0)
            break
        if new_state.p_hp <= 0:
            continue  # Losing state
        heappush(queue, new_state)
