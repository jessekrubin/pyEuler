#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Consecutive positive divisors
Problem 179
Find the number of integers 1 < n < 10^7, for which n and n + 1 have the same
number of positive divisors. For example, 14 has the positive divisors
1, 2, 7, 14 while 15 has 1, 3, 5, 15.
"""

from lib.maths import n_divisors
from tqdm import tqdm

## THIS IS A SLOW ONE

def posdivs(upper_bound):
    divisors_dict = {}
    for i in tqdm(range(1, upper_bound)):
        divisors_dict[i] = n_divisors(i)

    cpd_count = 0
    for i in range(1, upper_bound-1):
        if (divisors_dict[i] == divisors_dict[i+1]):
            cpd_count += 1
    return cpd_count

result = posdivs(10**7)
print("ANSWER: {}".format(result))

