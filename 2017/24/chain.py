#!/usr/bin/env python3

def find_strongest(start_val, links):
    best_so_far = 0
    for link in links:
        if link[0] == start_val:
            new_links = set(links)
            new_links.remove(link)
            best = find_strongest(link[1], new_links) + link[0] + link[1]
            best_so_far = max(best, best_so_far)
        if link[1] == start_val:
            new_links = set(links)
            new_links.remove(link)
            best = find_strongest(link[0], new_links) + link[0] + link[1]
            best_so_far = max(best, best_so_far)
    return best_so_far


pieces = set()
with open('input.txt', 'r') as f:
    for line in f:
        pieces.add(tuple(int(a) for a in line.split('/')))

print("Part 1", find_strongest(0, pieces))
