#!/usr/bin/env python3

def simulate(reg_0, find_non_loop):
    seen = set()
    c = 0
    last_unique_c = -1

    while True:
        a = c | 65536
        c = reg_0

        while True:
            c = (((c + (a & 255)) & 16777215) * 65899) & 16777215

            if a < 256:
                if find_non_loop:
                    return c
                else:
                    if c not in seen:
                        seen.add(c)
                        last_unique_c = c
                        break
                    else:
                        return last_unique_c
            else:
                a //= 256


print(simulate(7041048, True))
print(simulate(7041048, False))
