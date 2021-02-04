#!/usr/bin/env python3

# Directions = 0-4: [>, ^, <, v]
DIRECTIONS = ['>', '^', '<', 'v']
MOVE_INFO = [(0, 1), (-1, 0), (0, -1), (1, 0)]
JUNCTION_DIR = [+1, 0, -1]
class Cart:
    def __init__(self, r, c, symbol):
        self.next_turn = 0
        self.row = r
        self.col = c
        self.dir = {'>': 0, '^': 1, '<': 2, 'v': 3}[symbol]

    def get_symbol(self):
        return DIRECTIONS[self.dir]

    def __repr__(self):
        return 'Cart(row={}, col={}, dir={}, turn={})'.format(self.row, self.col, self.dir, self.next_turn)

    def process_move(self, map):
        move = MOVE_INFO[self.dir]
        row = self.row + move[0]
        col = self.col + move[1]
        new_cell = map[row][col]
        if new_cell in ['|', '-']:
            pass # Just move
        elif new_cell == '+':
            self.dir = (self.dir +JUNCTION_DIR[self.next_turn]) % 4
            self.next_turn = (self.next_turn + 1) % 3
        elif new_cell == '/':
            # Figure out new direction
            if self.dir == 0:
                self.dir = 1
            elif self.dir == 1:
                self.dir = 0
            elif self.dir == 2:
                self.dir = 3
            else:
                self.dir = 2
        elif new_cell == '\\':
            if self.dir == 0:
                self.dir = 3
            elif self.dir == 1:
                self.dir = 2
            elif self.dir == 2:
                self.dir = 1
            else:
                self.dir = 0
        else:
            assert new_cell is not None
        self.row, self.col = row, col


def display_map(m):
    cart_locs = {}
    for c in carts:
        cart_locs[(c.row, c.col)] = c
    for row, r in enumerate(m):
        s = ''
        for col in range(len(r)):
            if (row, col) in cart_locs:
                s += cart_locs[(row, col)].get_symbol()
            else:
                s += m[row][col]
        print(s)


with open('input.txt', 'r') as f:
    map = [[c for c in l.strip('\n')] for l in f]

carts = []
for row in range(len(map)):
    for col in range(len(map[row])):
        ch = map[row][col]
        if ch in ('>', '<'):
            carts.append(Cart(row, col, ch))
            map[row][col] = '-'
        elif map[row][col] in ('v', '^'):
            carts.append(Cart(row, col, ch))
            map[row][col] = '|'

has_crash = False
while not has_crash:
    #display_map(map)
    carts.sort(key=lambda c: (c.row, c.col))
    cart_locations = set([(c.row, c.col) for c in carts])
    #print(carts)
    for cart in carts:
        cart_locations.remove((cart.row, cart.col))
        cart.process_move(map)
        loc = (cart.row, cart.col)
        if loc in cart_locations:
            print("Crash at ({},{})".format(loc[1], loc[0]))
            has_crash = True
            break
        cart_locations.add(loc)