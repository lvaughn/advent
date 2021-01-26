#!/usr/bin/env python3

players = 438
balls = 71626 * 100


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


current = Node(0)
current.next = current
current.prev = current
scores = [0] * players
player = 0
for ball in range(1, balls + 1):
    if ball % 23 == 0:
        scores[player] += ball
        # Move back 7 times
        for _ in range(7):
            current = current.prev
        # Take the value of it
        scores[player] += current.value
        # Remove it
        current.prev.next = current.next
        current.next.prev = current.prev
        current = current.next
    else:
        current = current.next
        new_node = Node(ball)
        current.next.prev = new_node
        new_node.next = current.next
        new_node.prev = current
        current.next = new_node
        current = new_node
    player = (player + 1) % players

print(max(scores))
