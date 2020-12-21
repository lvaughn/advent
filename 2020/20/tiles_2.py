#!/usr/bin/env python3

import numpy as np
import sys
import math
from collections import defaultdict

tiles = {}


def gen_symmetries(base):
    flipped = np.fliplr(base)
    yield np.copy(base)
    yield flipped
    for i in range(1, 4):
        yield np.rot90(base, i)
        yield np.rot90(flipped, i)


class Tile:
    def __init__(self, id, rows):
        self.id = id
        base = np.zeros((10, 10), dtype=bool)
        for r, row in enumerate(rows):
            for c, val in enumerate(row):
                if val == '#':
                    base[r, c] = True

        # Generate the 8 versions of the tile
        self.tiles = list(gen_symmetries(base))

        # should make life better later
        # Maps this[symmetry] => set of tuples of (tile_id, symmetry)
        self.bottom_neighbors = defaultdict(set)
        self.right_neighbors = defaultdict(set)


def solve_board(used_tiles):
    global board, side_len, tiles
    current_pos = len(used_tiles)
    if current_pos == len(tiles):
        return True
    row = current_pos // side_len
    col = current_pos % side_len
    if col == 0:
        top = board[current_pos - side_len]
        possible_moves = tiles[top[0]].bottom_neighbors[top[1]]
    else:
        left = board[current_pos - 1]
        possible_moves = tiles[left[0]].right_neighbors[left[1]]
        if row > 0:
            top = board[current_pos - side_len]
            possible_moves = possible_moves.intersection(tiles[top[0]].bottom_neighbors[top[1]])
    if len(possible_moves) == 0:
        return False
    for move in possible_moves:
        tile = move[0]
        if tile in used_tiles:
            continue
        used_tiles.add(tile)
        board[current_pos] = move
        if solve_board(used_tiles):
            return True
        used_tiles.remove(tile)
    board[current_pos] = None
    return False


def sea_monster_present(board, row, col):
    for pt in sea_monster_points:
        if board[row + pt[0], col + pt[1]] != 1:
            return False
    return True


def draw_monster_present(board, row, col):
    for pt in sea_monster_points:
        board[row + pt[0], col + pt[1]] = 2


# Load the data
with open(sys.argv[1], 'r') as infile:
    buffer = []
    for line in infile:
        if line.startswith('Tile'):
            tile_id = line[5:-2]
        elif line.strip() == '':
            t = Tile(tile_id, buffer)
            tiles[tile_id] = t
            buffer = []
        else:
            buffer.append(line.strip())

for tile_id in tiles:
    t = tiles[tile_id]
    for neighbor_id in tiles:
        n = tiles[neighbor_id]
        if neighbor_id == tile_id:
            continue
        # See which symetries could be to the right and below this one
        for i in range(len(t.tiles)):
            tile = t.tiles[i]
            for j in range(len(n.tiles)):
                if np.array_equal(tile[-1, :], n.tiles[j][0, :]):
                    t.bottom_neighbors[i].add((n.id, j))
                if np.array_equal(tile[:, -1], n.tiles[j][:, 0]):
                    t.right_neighbors[i].add((n.id, j))

# Figure out our sizes
side_len = int(math.sqrt(len(tiles)))
assert (side_len * side_len == len(tiles))
board = [None] * len(tiles)  # A list of (tile_id, symmetry_id) of a possible solution

print("Setup complete")
solved = False
for t in tiles:
    tile = tiles
    for i in range(8):
        board[0] = (t, i)
        if solve_board(set([t])):
            solved = True
            break
    if solved:
        break
# Bring tiles together
for r in range(side_len):
    print(" ".join(board[r * side_len + c][0] for c in range(side_len)))

sat_map = np.zeros((8 * side_len, 8 * side_len), dtype=int)
for r in range(side_len):
    for c in range(side_len):
        map_row = 8 * r
        map_col = 8 * c
        board_cell = r * side_len + c
        tile_id, symmetry = board[board_cell]
        image = tiles[tile_id].tiles[symmetry]
        sat_map[map_row:map_row + 8, map_col:map_col + 8] = image[1:-1, 1:-1]

# Now to look for sea monsters
sea_monster_points = []
max_col = -1
max_row = -1
with open('sea_monster.txt', 'r') as monster:
    for r, row in enumerate(monster):
        for c, ch in enumerate(row):
            if ch == '#':
                sea_monster_points.append((r, c))
                max_row = max(max_row, r)
                max_col = max(max_col, c)

# Now do the thing
for i, m in enumerate(gen_symmetries(sat_map)):
    monster_found = False
    for r in range(m.shape[0] - max_row):
        for c in range(m.shape[1] - max_col):
            if sea_monster_present(m, r, c):
                monster_found = True
                draw_monster_present(m, r, c)
    if monster_found:
        print(np.count_nonzero(m == 1))
        break
