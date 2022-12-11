#!/usr/bin/env python3
from collections import Counter, defaultdict, deque, namedtuple
import re
import sys

NUMBER_RE = re.compile(r'(\d+)')

inspections = Counter()
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

n = 0
monkeys = []
while n < len(lines):
    _, monkey_no = lines[n].split(' ')
    monkey_no = int(monkey_no[:-1])
    _, items_str = lines[n + 1].split(':')
    items = list(map(lambda s: int(s.strip()), items_str.split(',')))
    _, operation = lines[n + 2].split('new =')
    m = NUMBER_RE.search(lines[n + 3])
    divisible_by = int(m[1])
    m = NUMBER_RE.search(lines[n + 4])
    true_to = int(m[1])
    m = NUMBER_RE.search(lines[n + 5])
    false_to = int(m[1])
    n += 7
    inspections[monkey_no] = 0

    monkeys.append(
        {
            'num': monkey_no,
            'items': items,
            'op': operation.replace('old', '%d'),
            'div_by': divisible_by,
            'true': true_to,
            'false': false_to
        })

for x in range(20):
    for monkey in monkeys:
        id = monkey['num']
        for w in monkey['items']:
            inspections[id] += 1
            if monkey['op'].count('%d') == 1:
                new_w = eval(monkey['op'] % w)
            else:
                new_w = eval(monkey['op'] % (w, w))
            new_w = new_w // 3
            if new_w % monkey['div_by'] == 0:
                monkeys[monkey['true']]['items'].append(new_w)
            else:
                monkeys[monkey['false']]['items'].append(new_w)
        monkey['items'] = []
top_2 = inspections.most_common(2)
print("Part 1", top_2[0][1] * top_2[1][1])
