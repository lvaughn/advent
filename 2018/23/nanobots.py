#!/usr/bin/env python3

import re
import networkx
import pprint
from z3 import Int, Optimize, If

def man_dist(a, b):
    return sum(abs(x[0] - x[1]) for x in zip(a, b))

distances = {}
largest_range = -1
longest_pos = None
bots = []
with open('input.txt', 'r') as f:
    line_regex = re.compile(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(-?\d+)')
    for line in f:
        m = line_regex.match(line)
        pos = (int(m[1]), int(m[2]), int(m[3]))
        r = int(m[4])
        bots.append((pos, r))
        distances[pos] = r
        if r > largest_range:
            largest_range = r
            longest_pos = pos

print("Part 1:", len([p for p in distances if man_dist(p, longest_pos) <= distances[longest_pos]]))

def z3_abs(x):
    return If(x >= 0,x,-x)

x = Int('x')
y = Int('y')
z = Int('z')

spheres = []
o = Optimize()
for i, bot in enumerate(bots):
    (pos, rng) = bot
    spheres.append(Int(f"bot_{i}"))
    o.add(spheres[-1] == If(z3_abs(x - pos[0]) + z3_abs(y - pos[1]) + z3_abs(z - pos[2]) <= rng, 1, 0))

range_count = Int('sum')
o.add(range_count == sum(spheres))
dist_from_zero = Int('dist')
o.add(dist_from_zero == z3_abs(x) + z3_abs(y) + z3_abs(z))
h1 = o.maximize(range_count)
h2 = o.minimize(dist_from_zero)
print(o.check())
#print o.lower(h1)
#print o.upper(h1)
print("b", o.lower(h2), o.upper(h2))
#
# graph = networkx.Graph()
# for i in range(len(bots) - 1):
#     a = bots[i]
#     for b in bots[i+1:]:
#         if man_dist(a[0], b[0]) <= (a[1] + b[1]):
#             graph.add_edge(a, b)
#
# best_size = 0
# best_clique = None
# for clique in networkx.find_cliques(graph):
#     if len(clique) == best_size:
#         print("Hi")
#     if len(clique) > best_size:
#         best_clique = clique
#         best_size = len(clique)
#
# # Find the minimum point for each bot's range, and then the maximum of all of those
# ranges = [max(man_dist(bot, (0,0,0)), 0) - rng for bot, rng in best_clique]
# print(len(bots))
# #pprint.pprint(best_clique)
# print(len(ranges))
# print("Part 2", max(ranges))
