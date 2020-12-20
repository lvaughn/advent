#!/usr/bin/env python3

import numpy as np
import sys
import math
from collections import defaultdict

tiles = {}

class Tile:
    def __init__(self, id, rows):
        self.id = id
        base = np.zeros((10,10), dtype=bool)
        for r, row in enumerate(rows):
            for c, val in enumerate(row):
                if val == '#':
                    base[r,c] = True

        # Generate the 8 versions of the tile
        self.tiles = []
        flipped = np.fliplr(base)
        self.tiles.append(base)
        self.tiles.append(flipped)
        for i in range(1, 4):
            self.tiles.append(np.rot90(base, i))
            self.tiles.append(np.rot90(flipped, i))

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
    #print(current_pos, row, col, board[current_pos - 1])
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
                    t.right_neighbors[i].add((n.id, j))
                if np.array_equal(tile[:, -1], n.tiles[j][:, 0]):
                    t.bottom_neighbors[i].add((n.id, j))
    #print(t.id, t.bottom_neighbors, t.right_neighbors)

# Figure out our sizes
side_len = int(math.sqrt(len(tiles)))
assert(side_len*side_len == len(tiles))
board = [None] * len(tiles) # A list of (tile_id, symmetry_id) of a possible solution

for t in tiles:
    tile = tiles
    for i in range(8):
        board[0] = (t, i)
        if solve_board(set([t])):
            print(board)
            ans = 1
            ans *= int(board[0][0])
            ans *= int(board[side_len - 1][0])
            ans *= int(board[len(tiles)-side_len][0])
            ans *= int(board[-1][0])
            print(ans)
            sys.exit(0)

