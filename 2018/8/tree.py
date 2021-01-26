#!/usr/bin/env python3

class Node:
    def __init__(self, values):
        self.children = []
        self.metadata = []
        n_children = next(values)
        n_metadata = next(values)
        for _ in range(n_children):
            self.children.append(Node(values))
        for _ in range(n_metadata):
            self.metadata.append(next(values))

    def sum_metadata(self):
        total = sum(self.metadata)
        for child in self.children:
            total += child.sum_metadata()
        return total

    def get_value(self):
        if len(self.children) == 0:
            return sum(self.metadata)
        value = 0
        for m in self.metadata:
            if 1 <= m <= len(self.children):
                value += self.children[m-1].get_value()
        return value


def int_iter(s):
    for n in s.split(' '):
        yield int(n)


with open('input.txt', 'r') as f:
    root = Node(int_iter(f.read()))

print("Part 1:", root.sum_metadata())
print("Part 1:", root.get_value())