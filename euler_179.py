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

from helpme import n_divisors, divisors_gen

consecutive_positive_divisors = 0

for i in range(1, (10**5 // 2)):
    eye = n_divisors(i)
    eye2 = n_divisors(i+1)
    if eye == eye2:
        consecutive_positive_divisors += 1
    #     consecutive_positive_divisors += 1

print(consecutive_positive_divisors)
