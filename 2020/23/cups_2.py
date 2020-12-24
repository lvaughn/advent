#!/usr/bin/env python3

starting_pattern = '123487596'
#starting_pattern = '389125467'
n_rounds = 10000000

cups = [int(i) for i in starting_pattern]
current_loc = 0
n_cups = len(cups)
cups = cups + list(range(n_cups + 1, 1000001))
for i in range(n_rounds):
    if i % 1000 == 0:
        print('Round',i)
    current_cup = cups[current_loc]

    # Remove three cups
    remove_start = (current_loc + 1) % n_cups
    new_ls = []
    if remove_start < n_cups - 3:
        new_ls.extend(cups[:remove_start])
        removed = cups[remove_start:remove_start+3]
        new_ls.extend(cups[remove_start+3:])
    else:
        n_before_wrap = n_cups - remove_start
        n_after_wrap = 3 - n_before_wrap
        #print("LGV:", n_after_wrap, n_before_wrap, remove_start)
        new_ls.extend(cups[n_after_wrap:-n_before_wrap])
        removed = cups[-n_before_wrap:] + cups[:n_after_wrap]


    # Find starting point to insert
    #print(new_ls, removed, current_cup)
    insert_cup = (current_cup - 1) % (n_cups + 1)
    if insert_cup == 0:
        insert_cup = n_cups
    while insert_cup in removed:
        insert_cup = (insert_cup - 1) % (n_cups + 1)
        if insert_cup == 0:
            insert_cup = n_cups
    #print(new_ls, removed, insert_cup)
    idx = new_ls.index(insert_cup)
    cups = new_ls[:idx+1] + removed + new_ls[idx+1:]
    current_loc = (cups.index(current_cup) + 1) % n_cups
    #print(new_ls, removed, insert_cup, cups, current_loc)

# True up the output
idx = cups.index(1)
print(cups[idx+1] * cups[idx+2])
