#!/usr/bin/env python3

def mix_itter(total, ins):
    if len(ins) == 1:
        yield [(ins[0], total)]
    else:
        for i in range(1, total - len(ins) + 2):
            for sub_mix in mix_itter(total - i, ins[1:]):
                yield [([ins[0], i])] + sub_mix


values = {}
ingredients = []
factor_names = ['capacity', 'durability', 'flavor', 'texture']
with open('input.txt', 'r') as f:
    for line in f:
        idx = line.index(':')
        name = line[:idx]
        ingredients.append(name)
        factors = {}
        for val in line[idx + 1:].strip().split(','):
            factor, value = val.strip().split(" ")
            factors[factor] = int(value)
        values[name] = factors

best_so_far = -1
best_with_calories = -1
for combo in mix_itter(100, ingredients):
    goodness = 1
    for factor in factor_names:
        f = 0
        for (ing, amount) in combo:
            f += amount * values[ing][factor]
        goodness *= max(0, f)
    cal = 0
    for (ing, amount) in combo:
        cal += amount * values[ing]['calories']

    if goodness > best_so_far:
        best_so_far = goodness
    if goodness > best_with_calories and cal == 500:
        best_with_calories = goodness

print("Best overall", best_so_far)
print("Best 500 calories", best_with_calories)
