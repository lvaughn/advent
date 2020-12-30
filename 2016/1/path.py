#!/usr/bin/env python3

# Directions
#      0
#    3 * 1
#      2


x = 0
y = 0
facing = 0
seen = set()
first_twice = None

def test_seen(x, y):
    global first_twice
    if (x, y) in seen and first_twice is None:
        first_twice = (x, y)
    seen.add((x, y))

with open('input.txt', 'r') as f:
    for line in f:
        for step in line.split(','):
            s = step.strip()
            if s[0] == 'L':
                facing = (facing - 1) % 4
            else: # R
                facing = (facing + 1) % 4
            if facing == 0:
                for _ in range(int(s[1:])):
                    y += 1
                    test_seen(x, y)
            elif facing == 1:
                for _ in range(int(s[1:])):
                    x += 1
                    test_seen(x, y)
            elif facing == 2:
                for _ in range(int(s[1:])):
                    y -= 1
                    test_seen(x, y)
            else: # facing == 3
                for _ in range(int(s[1:])):
                    x -= 1
                    test_seen(x, y)

print("Part 1", abs(x)+abs(y))
print("Part 2", first_twice[0] + first_twice[1])

