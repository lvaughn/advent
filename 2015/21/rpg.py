#!/usr/bin/env python3

from collections import namedtuple
from itertools import combinations

Item = namedtuple('Item', ['name', 'cost', 'damage', 'armor'])

boss_hp = 109
boss_damage = 8
boss_armor = 2

weapons = [
    Item('Dagger', 8, 4, 0),
    Item('Shortsword', 10, 5, 0),
    Item('Warhammer', 25, 6, 0),
    Item('Longsword', 40, 7, 0),
    Item('Greataxe', 74, 8, 0)
]

armors = [
    Item('Leather', 13, 0, 1),
    Item('Chainmail', 31, 0, 2),
    Item('Splintmail', 53, 0, 3),
    Item('Bandedmail', 75, 0, 4),
    Item('Platemail', 102, 0, 5),
]

rings = [
    Item('Damage +1', 25, 1, 0),
    Item('Damage +2', 50, 2, 0),
    Item('Damage +3', 100, 3, 0),
    Item('Defense +1', 20, 0, 1),
    Item('Defense +2', 40, 0, 2),
    Item('Defense +3', 80, 0, 3),
]

def winningCombo(armor, damage):
    p_hp = 100
    b_hp = boss_hp

    turn = 0 # player is zero
    while b_hp > 0 and p_hp > 0:
        if turn == 0:
            b_hp -= max(1, damage-boss_armor)
        else:
            p_hp -= max(1,boss_damage - armor)
        turn = 1 - turn
    return p_hp > 0

ring_combos = [[]]
ring_combos.extend(combinations(rings, 2))
ring_combos.extend(combinations(rings, 1))

cheapest_win = 1000000
for r in ring_combos:
    for w in weapons:
        for a in armors:
            cost = w.cost + a.cost
            damage = w.damage + a.damage
            armor = w.armor + a.armor
            for ring in r:
                cost += ring.cost
                damage += ring.damage
                armor += ring.armor
            if cost < cheapest_win and winningCombo(armor, damage):
                cheapest_win = cost
                print("Best Combo", cost, [x.name for x in r], w.name, a.name)

expensive_win = -1
for r in ring_combos:
    for w in weapons:
        cost = w.cost
        damage = w.damage
        armor = w.armor
        for ring in r:
            cost += ring.cost
            damage += ring.damage
            armor += ring.armor
        if cost > expensive_win and not winningCombo(armor, damage):
            expensive_win = cost
            print("Worst Combo (no armor)", cost, [x.name for x in r], w.name)
        for a in armors:
            cost = w.cost + a.cost
            damage = w.damage + a.damage
            armor = w.armor + a.armor
            for ring in r:
                cost += ring.cost
                damage += ring.damage
                armor += ring.armor
            if cost > expensive_win and not winningCombo(armor, damage):
                expensive_win = cost
                print("Worst Combo", cost, [x.name for x in r], w.name, a.name)
