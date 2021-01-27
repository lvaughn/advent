#!/usr/bin/env python3

import re
import numpy as np

input_re = re.compile(r'position=<\s*([0-9-]+),\s*([0-9-]+)> velocity=<\s*([0-9-]+),\s*([0-9-]+)>')

points = []
velocities = []
with open('input.txt', 'r') as f:
    for l in f:
        m = input_re.match(l)
        points.append((int(m[1]), int(m[2])))
        velocities.append((int(m[3]), int(m[4])))

pt_array = np.array(points, dtype=int)
vel_array = np.array(velocities, dtype=int)

last_diff = 99999999999
n_rounds = 0
while True:
    new_pt = pt_array + vel_array
    max_x = np.max(new_pt[:, 0])
    min_x = np.min(new_pt[:, 0])
    max_y = np.max(new_pt[:, 1])
    min_y = np.min(new_pt[:, 1])
    dx = max_x - min_x
    dy = max_y - min_y

    if dx + dy > last_diff:
        max_x = np.max(pt_array[:, 0])
        min_x = np.min(pt_array[:, 0])
        max_y = np.max(pt_array[:, 1])
        min_y = np.min(pt_array[:, 1])
        rows = []
        for x in range(min_y, max_y + 1):
            rows.append([' '] * (1 + max_x - min_x))

        # print(min_x, max_x)
        # print(min_y, max_y)
        # print(len(rows), len(rows[0]))
        for i in range(pt_array.shape[0]):
            x, y = pt_array[i, 0], pt_array[i, 1]
            rows[y - min_y][x - min_x] = '#'

        for row in rows:
            print(''.join(row))

        break
    pt_array = new_pt
    last_diff = dx + dy
    n_rounds += 1

print("Found in {} seconds".format(n_rounds))

