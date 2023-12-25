#!/usr/bin/env python3
from collections import Counter, defaultdict, deque, namedtuple
from itertools import count, product, permutations, combinations, combinations_with_replacement
import sys
from networkx import Graph, minimum_edge_cut, connected_components 

with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

connectioned = defaultdict(list)
connections = []
last_src = None
graph = Graph()
for l in lines:
    src, dests = l.split(':')
    last_src = src
    dest_ls = dests.strip().split(" ")
    for dest in dest_ls:
        graph.add_edge(src, dest)
        
cuts = minimum_edge_cut(graph)
assert len(cuts) == 3
graph.remove_edges_from(cuts)
parts = connected_components(graph)
answer = 1
for p in parts:
    answer *= len(p)
print("Part 1", answer)