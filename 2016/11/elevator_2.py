#!/usr/bin/env python3

from collections import deque, namedtuple
from itertools import combinations
import sys

FloorState = namedtuple('FloorState', ['chips', 'gens'])


class State:
    def __init__(self):
        self.elevator = 0
        self.floors = [(), (), (), ()]
        self.n_moves = 0

    def copy(self):
        new_state = State()
        new_state.elevator = self.elevator
        for i, fs in enumerate(self.floors):
            new_state.floors[i] = FloorState(fs.chips, fs.gens)
        new_state.n_moves = self.n_moves
        return new_state

    def getKey(self):
        return (self.elevator, tuple(self.floors))


def is_valid_state(state):
    for floor in state.floors:
        for chip in floor.chips:
            if len(floor.gens) > 0 and chip not in floor.gens:
                return False
    return True


def merge_to_floor(floor_state, new_chips, new_gens):
    chips = frozenset(floor_state.chips.union(new_chips))
    gens = frozenset(floor_state.gens.union(new_gens))
    return FloorState(chips, gens)


def make_new_state(state, direction, chips, gens):
    floor = state.elevator
    curr_floor = state.floors[floor]
    new_gens = frozenset(curr_floor.gens - gens)
    new_chips = frozenset(curr_floor.chips - chips)
    new_curr_floor = FloorState(new_chips, new_gens)
    new_next_floor = merge_to_floor(state.floors[floor + direction], chips, gens)
    new_state = state.copy()
    new_state.n_moves += 1
    new_state.floors[floor] = new_curr_floor
    new_state.floors[floor + direction] = new_next_floor
    new_state.elevator += direction
    return new_state


def process_new_state(state):
    if is_valid_state(state):
        if len(state.floors[3].chips) == N_ELEMENTS and len(state.floors[3].gens) == N_ELEMENTS:
            print("Success", state.n_moves)
            sys.exit()
        key = state.getKey()
        if key not in has_processed:
            queue.append(state)
            has_processed.add(key)
        else:
            global skipped
            skipped += 1


initial_state = State()
empty_set = frozenset()
initial_state.floors[0] = FloorState(frozenset(['promethium', 'elerium', 'dilithium']),
                                     frozenset(['promethium', 'elerium', 'dilithium']))
# initial_state.floors[0] = FloorState(frozenset(['promethium']), frozenset(['promethium']))
initial_state.floors[1] = FloorState(empty_set, frozenset(['cobalt', 'curium', 'ruthenium', 'plutonium']))
initial_state.floors[2] = FloorState(frozenset(['cobalt', 'curium', 'ruthenium', 'plutonium']), empty_set)
initial_state.floors[3] = FloorState(empty_set, empty_set)
N_ELEMENTS = 7

queue = deque()
queue.append(initial_state)
has_processed = set()
step = 0
skipped = 0
while len(queue) > 0:
    state = queue.popleft()
    if step % 10000 == 0:
        print("Step {}: moves={}, queue={}, seen={}, skipped={}".format(step, state.n_moves, len(queue),
                                                                        len(has_processed), skipped))
    step += 1
    # Figure out where we can move from here
    for direction in [-1, 1]:
        floor = state.elevator
        if (direction == -1 and floor == 0) or (direction == 1 and floor == 3):
            continue
        # Two microchip cases
        curr_floor = state.floors[floor]
        if len(curr_floor.chips) >= 2:
            for combo in combinations(curr_floor.chips, 2):
                new_state = make_new_state(state, direction, set(combo), empty_set)
                process_new_state(new_state)
        # Two generators
        if len(curr_floor.gens) >= 2:
            for combo in combinations(curr_floor.gens, 2):
                new_state = make_new_state(state, direction, empty_set, set(combo))
                process_new_state(new_state)
        # One of each
        for chip in curr_floor.chips:
            # Move one chip
            new_state = make_new_state(state, direction, {chip}, empty_set)
            process_new_state(new_state)

            # Try with each generator
            for gen in curr_floor.gens:
                new_state = make_new_state(state, direction, {chip}, {gen})
                process_new_state(new_state)
        # Only one gen
        for gen in curr_floor.gens:
            new_state = make_new_state(state, direction, empty_set, {gen})
            process_new_state(new_state)
