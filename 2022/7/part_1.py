#!/usr/bin/env python3

import sys


def get_size(item):
    if type(item) is int:
        return item
    else:
        assert type(item) is dict
        total = 0
        for name in item:
            total += get_size(item[name])
        return total


def enum_size(cwd, path):
    for name in cwd:
        if type(cwd[name]) == dict:
            for r in enum_size(cwd[name], path + '/' + name):
                yield r
    yield path, get_size(cwd)


with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

root = {}
current_dir = root
path = []
for l in lines:
    if l.startswith('$'):
        if l[2:].startswith('cd'):
            dir = l[5:]
            if dir == '/':
                path = []
                current_dir = root
            elif dir == '..':
                path = path[:-1]
                current_dir = root
                for p in path:
                    current_dir = current_dir[p]
            else:
                if dir not in current_dir:
                    current_dir[dir] = {}
                current_dir = current_dir[dir]
                path.append(dir)
        else:
            assert l[2:].startswith('ls')
    else:
        size, name = l.split(' ')
        if size == 'dir':
            current_dir[name] = {}
        else:
            current_dir[name] = int(size)

total = 0
for path, size in enum_size(root, ''):
    if size <= 100000:
        total += size
print("Part 1", total)

current_free = 70000000 - get_size(root)
need_to_free = 30000000 - current_free

min_can_be_freed = 1000000000
for path, size in enum_size(root, ''):
    if size >= need_to_free and size < min_can_be_freed:
        min_can_be_freed = size

print("Part 2", min_can_be_freed)
