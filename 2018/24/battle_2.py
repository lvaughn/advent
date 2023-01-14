#!/usr/bin/env python3

import re

INFECTION = 1
DEFENDER = 2


class Group:
    def __init__(self, side, id, units, hp, attack_type, attack, initiative):
        self.side = side
        self.id = id
        self.immune_to = []
        self.weaknesses = []
        self.units = units
        self.hp_per_unit = hp
        self.attack_type = attack_type
        self.attack_hp = attack
        self.initiative = initiative
        self.will_attack = None
        self.attacked_by = None

        if side == DEFENDER:
            self.name = f"Immune-{self.id}"
        else:
            self.name = f"Infection-{self.id}"

    def __str__(self):
        return f"Group {self.id}:side={self.side}, n_units={self.units}, hp={self.hp_per_unit}, attack={self.attack_type} ({self.attack_hp} pts), init={self.initiative}:immune={self.immune_to}:weak={self.weaknesses}"

    def effective_power(self):
        return self.units * self.attack_hp

    def would_damage(self, other):
        if self.attack_type in other.immune_to:
            return 0
        dmg = self.units * self.attack_hp
        if self.attack_type in other.weaknesses:
            dmg *= 2
        return dmg

    def reset(self):
        self.will_attack = None
        self.attacked_by = None

    def best_attack(self, enemies):
        pass


def play_round(immune, infection):
    # Target selection
    for group in sorted(infection, key=lambda x: (x.effective_power(), x.initiative), reverse=True):
        attack_order = sorted([i for i in immune if i.attacked_by is None and group.would_damage(i) > 0],
                              key=lambda x: (group.would_damage(x), x.effective_power(), x.initiative),
                              reverse=True)
        if attack_order:
            group.will_attack = attack_order[0]
            attack_order[0].attacked_by = group

    for group in sorted(immune, key=lambda x: (x.effective_power(), x.initiative), reverse=True):
        attack_order = sorted([i for i in infection if i.attacked_by is None and group.would_damage(i) > 0],
                              key=lambda x: (group.would_damage(x), x.effective_power(), x.initiative),
                              reverse=True)
        if attack_order:
            group.will_attack = attack_order[0]
            attack_order[0].attacked_by = group

    # Attack phase
    all_groups = sorted(immune + infection, key=lambda g: g.initiative, reverse=True)
    for grp in all_groups:
        opp = grp.will_attack
        if grp.units > 0 and opp:
            units_destroyed = grp.would_damage(opp) // opp.hp_per_unit
            opp.units = max(opp.units - units_destroyed, 0)
        grp.reset()

    return [i for i in immune if i.units > 0], [i for i in infection if i.units > 0]


def run_sim(bonus):
    immune_groups = []
    infection_groups = []
    current_groups = None
    line_re = re.compile(r'^(\d+)\D+(\d+) hit points (\(.*\))?\s*with an\D+(\d+)\s+(\w+)\s+damage\D+(\d+)')
    clause_re = re.compile(r'(\w+) to (.*)')
    side = None
    id = 0

    with open('input.txt', 'r') as infile:
        for line in infile:
            if line.strip() == '':
                continue
            if line.startswith('Immune'):
                current_groups = immune_groups
                side = DEFENDER
                id = 1
                continue
            if line.startswith('Infection'):
                current_groups = infection_groups
                side = INFECTION
                id = 1
                continue
            # Parse the line
            m = line_re.match(line)

            grp = Group(side, id, int(m[1]), int(m[2]), m[5], int(m[4]), int(m[6]))
            id += 1
            current_groups.append(grp)
            if m[3]:
                for clause in m[3].replace(')', '').split(';'):
                    match = clause_re.search(clause)
                    for attack in match[2].split(','):
                        if match[1].endswith('weak'):
                            grp.weaknesses.append(attack.strip())
                        else:
                            grp.immune_to.append(attack.strip())

    for g in immune_groups:
        g.attack_hp += bonus
    states = set()
    while len(immune_groups) > 0 and len(infection_groups) > 0:
        immune_groups, infection_groups = play_round(immune_groups, infection_groups)
        state = (tuple(i.units for i in immune_groups), tuple(i.units for i in infection_groups))
        if state in states:
            return 0
        states.add(state)

    result = sum(g.units for g in infection_groups + immune_groups)
    if len(immune_groups) > 0:
        return result
    else:
        return -result


min_bonus = 0
max_bonus = 10000000
while min_bonus + 1 < max_bonus:
    bonus = (min_bonus + max_bonus) // 2
    score = run_sim(bonus)
    # print(min_bonus, max_bonus, bonus, score)
    if score > 0:
        max_bonus = bonus
    else:
        min_bonus = bonus

# print(min_bonus, max_bonus, run_sim(min_bonus), run_sim(max_bonus))
print("Part 2:", run_sim(max_bonus))
