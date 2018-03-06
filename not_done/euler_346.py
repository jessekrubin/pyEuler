#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Strong Repunits
Problem 346
The number 7 is special, because 7 is 111 written in base 2, and 11 written in
base 6 (i.e. 710 = 116 = 1112). In other words, 7 is a repunit in at least two
bases b > 1.

We shall call a positive integer with this property a strong repunit. It can be
verified that there are 8 strong repunits below 50: {1,7,13,15,21,31,40,43}.
Furthermore, the sum of all strong repunits below 1000 equals 15864.

Find the sum of all strong repunits below 10^12.
"""

from collections import defaultdict
from tqdm import tqdm

def ones_base_n(base, under):
    current = 0
    place = 0
    nums = set()
    while(current < under):
        current += base**place
        if current < under:
            nums.add(current)
        place += 1
    return nums

def strong_repunits(upper_limit):
    strong_repunits = defaultdict(set)

    for n_ones in range(3, upper_limit):
        for base in range(2, upper_limit):
            for number in ones_base_n(base, upper_limit):
                strong_repunits[number].add(base)

    str_reps = [k for k, v in strong_repunits.items() if len(v) > 1]
    return str_reps

def sum_strong_repunits(upper_limit):
    return sum(strong_repunits(upper_limit))

result = sum_strong_repunits(1000)
print(result)

result = sum_strong_repunits(10**12)
print(result)



