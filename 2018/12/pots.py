#!/usr/bin/env python3

PADDING = 10

pots = [0] * PADDING  # PADDING to the left of zero

transforms = {}  # 5-wide tuple of 0-1's to a zero or a 1
with open('input.txt', 'r') as f:
    start = f.readline()
    idx = start.index(':')
    for ch in start[idx+1:].strip():
        if ch == '#':
            pots.append(1)
        else:
            pots.append(0)

    for i in range(PADDING):
        pots.append(0)
    # Burn a line
    f.readline()

    # Read the rest
    for line in f:
        key = []
        for i in range(5):
            if line[i] == '#':
                key.append(1)
            else:
                key.append(0)
        value = 0
        if line[9] == '#':
            value = 1
        transforms[tuple(key)] = value

# Do the generations
last = 0
for gen in range(20): 
    new_pots = [0, 0]
    last_one = None
    for i in range(len(pots) - 4):
        key = tuple(pots[i:i+5])
        val = transforms[key]
        new_pots.append(val)
        if val == 1:
            last_one = i
    while len(new_pots) < last_one + 6:
        new_pots.append(0)
    pots = new_pots
    # total = 0
    # lowest = PADDING
    # highest = len(new_pots)
    # for i, pot in enumerate(pots):
    #     if pot == 1:
    #         total += i - PADDING
    #         lowest = min(lowest, i)
    #         highest = max(highest, i)
    # if total - last != 26:
    #     print(gen, total, total - last, lowest, highest, len(pots))
    # last = total

total = 0
for i, pot in enumerate(pots):
    if pot == 1:
        total += i - PADDING
print(total)

