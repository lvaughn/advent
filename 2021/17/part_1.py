#!/usr/bin/env python3
# Is this ugly as sin: Yes
# Does it work: Also, yes

MIN_X = 241
MAX_X = 273
MIN_Y = -97
MAX_Y = -63


def should_quit(x, y):
    if MIN_X <= x <= MAX_X and MIN_Y <= y <= MAX_Y:
        return True
    if x > MAX_X or y < MIN_Y:
        return True
    return False


def simulate_shot(dx, dy):
    x, y = 0, 0
    max_y = y
    while not should_quit(x, y):
        x += dx
        y += dy
        max_y = max(y, max_y)
        dy -= 1
        if dx > 0:
            dx -= 1
        if dx < 0:
            dx += 1
    if MIN_X <= x <= MAX_X and MIN_Y <= y <= MAX_Y:
        return max_y
    return None


highest_y = -1
hits = 0
for dx in range(1, MAX_X + 1):
    for dy in range(MIN_Y, 500):
        highest = simulate_shot(dx, dy)
        if highest is not None:
            hits += 1
            highest_y = max(highest, highest_y)

print(f"Part 1: {highest_y}")
print(f"Part 2: {hits}")
