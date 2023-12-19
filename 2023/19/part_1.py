#!/usr/bin/env python3
from collections import Counter, defaultdict, deque, namedtuple
import re
import sys

def get_next_workflow(workflow, part):
    for step in workflow:
        if ':' not in step:
            return step 
        rule, dest = step.split(':')
        var = rule[0]
        op = rule[1]
        val = int(rule[2:])
        if op == '<':
            if part[var] < val:
                return dest 
        elif op == '>':
            if part[var] > val:
                return dest 
        else:
            assert False, "Workflow:" + workflow 
    assert False 
    
    
def new_ranges(op, value, current_range):
    # Returns new_range, range_left
    if op == '>':
        if value > current_range[1]:
            return [], current_range 
        if value < current_range[0]:
            return current_range, []
        new_range = (value + 1, current_range[1])
        range_left = (current_range[0], value)
        return (new_range, range_left)
    assert op == '<'
    if value < current_range[0]:
        return [], current_range
    if value > current_range[1]:
        return current_range, []
    new_range = (current_range[0], value-1)
    range_left = (value, current_range[1])
    return new_range, range_left 
    
def get_next_states(workflow, state):
    new_states = []
    for step in workflow:
        if ':' not in step:
            new_states.append((step, state))
            continue 
        rule, dest = step.split(':')
        var = rule[0]
        op = rule[1]
        val = int(rule[2:])
        new_state = dict(state)
        new_range, range_left = new_ranges(op, val, state[var])
        new_state[var] = new_range
        if len(new_range) > 0:
            new_states.append((dest, new_state))
        if len(range_left) > 0:
            state[var] = range_left
        else:
            break # We've used everything up 
    return new_states
        
def n_accepts(st):
    result = 1
    for var in st:
        rng = st[var]
        result *= 1 + rng[1] - rng[0]
    return result 
        
def get_rating(part):
    return part['x'] + part['m'] + part['a'] + part['s']

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    

workflow_re = re.compile(r'(\w+)\{(.*)\}')
workflows = {}
parts = []
mode = 1 # workflow
for l in lines:
    if l == '':
        mode = 2
    elif mode == 1:
        m = workflow_re.match(l)
        name = m[1]
        steps = m[2].split(',')
        workflows[name] = steps
    else:
        part = {}
        sections = l.strip('{}').split(',')
        for s in sections:
            var, val = s.split('=')
            part[var] = int(val)
        parts.append(part)
        

for p in parts:
    wf = 'in'
    while wf not in ['A', 'R']:
        wf = get_next_workflow(workflows[wf], p)
        
    if wf == 'A':
        answer += get_rating(p)

print("Part 1", answer)

starting_state = {
    'x': (1, 4000),
    'm': (1, 4000),
    'a': (1, 4000),
    's': (1, 4000),
}

work_queue = deque()
work_queue.append(('in', starting_state))

answer = 0
while len(work_queue) > 0:
    wf_name, state = work_queue.popleft()
    new_states = get_next_states(workflows[wf_name], state)
    for rule, st in new_states:
        if rule == 'A':
            answer += n_accepts(st)
        elif rule == 'R':
            continue 
        else:
            work_queue.append((rule, st))
print("Part 2", answer)
