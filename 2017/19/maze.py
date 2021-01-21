#!/usr/bin/env python3

from string import ascii_uppercase

maze = []
with open('input.txt', 'r') as f:
    for line in f:
        maze.append(line)

direction_info = {
    's': (1, 0, '|'),
    'n': (-1, 0, '|'),
    'w': (0, -1, '-'),
    'e': (0, 1, '-'),
}

row = 0
col = maze[0].index('|')
dir = 's'

done = False
letters = []
while not done:
    # Peak ahead and see what we're getting in to
    d_row, d_col, straight = direction_info[dir]
    next_spot = maze[row + d_row][col + d_col]
    if next_spot == straight:
        row += d_row
        col += d_col
    elif next_spot in ['|', '-']:  # Crossing over
        row += d_row
        col += d_col
    elif next_spot == '+':
        # find out which direction to go
        for new_dir in direction_info:
            d_r, d_c, straight = direction_info[new_dir]
            new_row = row + d_row + d_r
            new_col = col + d_col + d_c
            # this might have to get more fancy, but trying it for now
            if new_row != row and new_col != col and maze[new_row][new_col] != ' ':
                row = new_row
                col = new_col
                dir = new_dir
                break
    else:
        assert next_spot in ascii_uppercase
        letters.append(next_spot)
        # Try and figure out if we're in the middle of a line, at a junction, or the end
        if maze[row + 2 * d_row][col + 2 * d_col] in ['-', '|']:
            row = row + 2 * d_row
            col = col + 2 * d_col
        else:
            # It should act like a plus, but it could be the last one
            found = False
            for new_dir in direction_info:
                d_r, d_c, straight = direction_info[new_dir]
                new_row = row + d_row + d_r
                new_col = col + d_col + d_c
                if new_row == row and new_col == col:
                    continue
                if maze[new_row][new_col] == ' ':
                    continue
                else:
                    row = new_row
                    col = new_col
                    dir = new_dir
                    found = True
            if not found:
                done = True

print(''.join(letters))
