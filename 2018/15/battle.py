#!/usr/bin/env python3

import numpy as np
from collections import deque
import sys


class Unit:
    def __init__(self, type):
        self.hp = 200
        self.attack = 3
        self.type = type
        self.dead = False

    def type_id(self):
        # -2 = elf
        # -3 = goblin
        if self.type == 'E':
            return -2
        return -3

    def attacks(self):
        if self.type == 'G':
            return -2
        return -3

    def __repr__(self):
        return "<{}: hp={}>".format(self.type, self.hp, self.attack)


def reachable_from(board, row, col):
    # return all cells reachable from row, col, in order
    b = np.copy(board)
    b[row, col] = 1
    queue = deque([(row, col, 0)])
    while len(queue) != 0:
        r, c, n_moves = queue.popleft()
        for d_r, d_c in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            new_r = r + d_r
            new_c = c + d_c
            if b[new_r, new_c] == 0:
                move = (new_r, new_c, n_moves + 1)
                queue.append(move)
                b[new_r, new_c] = 1
                yield move


def find_targets(board, target_type):
    for r in range(board.shape[0]):
        for c in range(board.shape[1]):
            if board[r, c] == target_type:
                for d_r, d_c in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    new_r = r + d_r
                    new_c = c + d_c
                    if 0 <= new_r < board.shape[0] and 0 <= new_c < board.shape[1] and board[new_r, new_c] == 0:
                        yield (new_r, new_c)


def next_to(board, row, col, type):
    results = []
    for d_r, d_c in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        new_r = row + d_r
        new_c = col + d_c
        if 0 <= new_r < board.shape[0] and 0 <= new_c < board.shape[1] and board[new_r, new_c] == type:
            results.append((new_r, new_c))
    return results


def best_move(board, start, end):
    targets = next_to(board, start[0], start[1], 0)
    if end in targets:
        return end
    board = np.copy(board)
    queue = deque()
    queue.append((end, 0))
    board[end[0], end[1]] = 0
    stop_point = None
    while len(queue) > 0:
        loc, n_moves = queue.popleft()
        #print("  Checking loc={}, moves={}, stop={}".format(loc, n_moves, stop_point))
        if stop_point and stop_point + 5 < n_moves:
            continue
        row, col = loc
        for d_r, d_c in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r = row + d_r
            c = col + d_c
            if 0 <= r < board.shape[0] and 0 <= c < board.shape[1] and board[r, c] == 0:
                board[r, c] = n_moves + 1
                # Check to see if we're done
                new_loc = (r, c)
                if new_loc in targets:
                    stop_point = n_moves + 1
                queue.append([new_loc, n_moves + 1])
    # print("Finding best move", start, end)
    # for target in targets:
    #     print("    ", target, board[target[0], target[1]])
    best = 99999
    # best_move = None
    # for target in targets:
    #     if board[target[0], target[1]] > 0 and board[target[0], target[1]] < best:
    #         best = board[target[0], target[1]]
    #         best_move = target
    # print("Returning ", best_move)
    best_moves = []
    for target in targets:
        if board[target[0], target[1]] > 0 and board[target[0], target[1]] < best:
            best = board[target[0], target[1]]
            best_moves = [target]
        elif board[target[0], target[1]] > 0 and board[target[0], target[1]] == best:
            best_moves.append(target)
    best_moves.sort()
    return best_moves[0]


def find_dest(board, row, col):
    unit = units[(row, col)]
    desired_locations = set(find_targets(board, unit.attacks()))

    best_distance = 100000
    good_moves = []
    for r, c, dist in reachable_from(board, row, col):
        if (r, c) not in desired_locations:
            continue
        if dist < best_distance:
            good_moves = [(r, c)]
            best_distance = dist
        elif dist == best_distance:
            good_moves.append((r, c))
    good_moves.sort()
    if len(good_moves) == 0:
        return None
    return good_moves[0]


def check_attack(board, unit, units):
    u = units[unit]
    to_attack = next_to(board, unit[0], unit[1], u.attacks())
    if len(to_attack) > 0:
        to_attack.sort()
        vic_coords = to_attack[0]
        if len(to_attack) > 1:
            for coords in to_attack[1:]:
                if units[coords].hp < units[vic_coords].hp:
                    vic_coords = coords
        vic = units[vic_coords]
        vic.hp -= u.attack
        if vic.hp <= 0:
            vic.dead = True
            board[vic_coords[0], vic_coords[1]] = 0
        return True
    return False


def print_board(board):
    for row in range(board.shape[0]):
        s = ''
        us = []
        for col in range(board.shape[1]):
            ch = {0: '.', -1: '#', -2: 'E', -3: 'G'}[board[row, col]]
            s += ch
            if ch in ['E', 'G']:
                unit = units[(row, col)]
                us.append(str(unit))
        print(s, ','.join(us))


with open(sys.argv[1], 'r') as f:
    initial_board = [line.strip() for line in f]

board_size = (len(initial_board), len(initial_board[0]))

# 0 = empty
# -1 = wall
# -2 = elf
# -3 = goblin

units = {}
board = np.zeros((board_size), dtype=int)
for row, r in enumerate(initial_board):
    for col, ch in enumerate(r):
        if ch == '#':
            board[row, col] = -1
        elif ch == 'E':
            board[row, col] = -2
            units[(row, col)] = Unit('E')
        elif ch == 'G':
            board[row, col] = -3
            units[(row, col)] = Unit('G')

turns = 0
# print_board(board)
early_exit = False
while np.count_nonzero(board == -2) > 0 and np.count_nonzero(board == -3) > 0:
    units_to_play = sorted(units.keys())
    for unit in units_to_play:
        u = units[unit]
        if u.dead:
            continue
        if np.count_nonzero(board == u.attacks()) == 0:
            early_exit = True
            break

        # Attack if we can, and if so, move on
        if check_attack(board, unit, units):
            continue

        # Otherwise, move
        new_dest = find_dest(board, unit[0], unit[1])
        if new_dest is None:
            continue
        new_loc = best_move(board, unit, new_dest)
        # print("Moving unit at {} to {} via {}".format(unit, new_dest, new_loc))
        units[new_loc] = units[unit]
        del units[unit]
        board[new_loc[0], new_loc[1]] = board[unit[0], unit[1]]
        board[unit[0], unit[1]] = 0

        # Attack if we can
        check_attack(board, new_loc, units)

    # Bring out your dead
    for unit in [u for u in units if units[u].dead]:
        del units[unit]
    if not early_exit:
        turns += 1

    # print("End of turn {}, e={}, g={}".format(turns, np.count_nonzero(board == -2), np.count_nonzero(board == -3)))
    print_board(board)
    print(turns)
    for u in sorted(units):
        print(u, units[u])
    print()

hp_sum = sum(u.hp for u in units.values())
for u in units.values():
    print(u)
print("Turns", turns)
print("HP", hp_sum)
print("Answer", turns * hp_sum)

# 204743 Wrong
# 202084 Wrong
