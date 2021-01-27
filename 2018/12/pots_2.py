#!/usr/bin/env python3

# Results from pots.py
# 166 5011 -414 10 280 280
# 167 5037 26 10 281 281
# 168 5063 26 10 282 282
# 169 5089 26 10 283 283
# 170 5115 26 10 284 284
# 171 5141 26 10 285 285
#
# The delta between generations settles down to 26

gen_168_value = 5063
target = 50000000000
print((50000000000 - 168 - 1) * 26 + gen_168_value)

