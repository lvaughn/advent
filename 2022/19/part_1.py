#!/usr/bin/env python3
from collections import deque, namedtuple
import re
import sys

SearchState = namedtuple('SearchState',
                         ['ore', 'clay', 'obs', 'geodes', 'n_ore', 'n_clay', 'n_obs', 'n_geo', 'time_left'])


def get_most_geodes(bp):
    starting_state = SearchState(0, 0, 0, 0, 1, 0, 0, 0, 24)
    most_geodes = -1
    queue = deque([starting_state])
    enqueued = set()
    max_ore = max(bp['ore_cost_ore'], bp['clay_cost_ore'], bp['obs_cost_ore'], bp['geo_cost_ore'])
    while len(queue) > 0:
        state = queue.popleft()
        # print(state)
        ore, clay, obs, geodes, n_ore, n_clay, n_obs, n_geo, time_left = state
        if time_left == 0:
            if geodes > most_geodes:
                most_geodes = geodes
            continue
        new_ore = ore + n_ore
        new_clay = clay + n_clay
        new_obs = obs + n_obs
        new_geodes = geodes + n_geo

        # Do nothing
        if ore <= max_ore:
            st = SearchState(new_ore, new_clay, new_obs, new_geodes,
                             n_ore, n_clay, n_obs, n_geo, time_left - 1)
            if st not in enqueued:
                queue.append(st)
                enqueued.add(st)
        if ore >= bp['ore_cost_ore']:
            st = SearchState(new_ore - bp['ore_cost_ore'], new_clay, new_obs, new_geodes,
                             n_ore + 1, n_clay, n_obs, n_geo, time_left - 1)
            if st not in enqueued:
                queue.append(st)
                enqueued.add(st)
        if ore >= bp['clay_cost_ore']:
            st = SearchState(new_ore - bp['clay_cost_ore'], new_clay, new_obs, new_geodes,
                             n_ore, n_clay + 1, n_obs, n_geo, time_left - 1)
            if st not in enqueued:
                queue.append(st)
                enqueued.add(st)
        if ore >= bp['obs_cost_ore'] and clay >= bp['obs_cost_clay']:
            st = SearchState(new_ore - bp['obs_cost_ore'], new_clay - bp['obs_cost_clay'], new_obs, new_geodes,
                             n_ore, n_clay, n_obs + 1, n_geo, time_left - 1)
            if st not in enqueued:
                queue.append(st)
                enqueued.add(st)
        if ore >= bp['geo_cost_ore'] and obs >= bp['geo_cost_obs']:
            st = SearchState(new_ore - bp['geo_cost_ore'], new_clay, new_obs - bp['geo_cost_obs'], new_geodes,
                             n_ore, n_clay, n_obs, n_geo + 1, time_left - 1)
            if st not in enqueued:
                queue.append(st)
                enqueued.add(st)

    return most_geodes


INT_RE = re.compile(r'(\d+)')
answer = 0
blueprints = []
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

for l in lines:
    parts = list(map(int, INT_RE.findall(l)))
    b = {
        'id': parts[0],
        'ore_cost_ore': parts[1],
        'clay_cost_ore': parts[2],
        'obs_cost_ore': parts[3],
        'obs_cost_clay': parts[4],
        'geo_cost_ore': parts[5],
        'geo_cost_obs': parts[6]
    }
    blueprints.append(b)

for bp in blueprints:
    best = get_most_geodes(bp)
    print(best, bp)
    answer += best * bp['id']

print("Part 1", answer)
