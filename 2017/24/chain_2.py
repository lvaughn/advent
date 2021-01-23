#!/usr/bin/env python3

# returns (length, strength)
def find_strongest(start_val, links):
    best_len = 0
    best_str = 0
    for link in links:
        if link[0] == start_val:
            new_links = set(links)
            new_links.remove(link)
            best = find_strongest(link[1], new_links)
            best_new_len = best[0] + 1
            best_new_str = best[1] + link[0] + link[1]
            if best_new_len > best_len or (best_new_len == best_len and best_new_str > best_str):
                best_len = best_new_len
                best_str = best_new_str
        if link[1] == start_val:
            new_links = set(links)
            new_links.remove(link)
            best = find_strongest(link[0], new_links)
            best_new_len = best[0] + 1
            best_new_str = best[1] + link[0] + link[1]
            if best_new_len > best_len or (best_new_len == best_len and best_new_str > best_str):
                best_len = best_new_len
                best_str = best_new_str
    return best_len, best_str


pieces = set()
with open('input.txt', 'r') as f:
    for line in f:
        pieces.add(tuple(int(a) for a in line.split('/')))

print("Part 2", find_strongest(0, pieces))
