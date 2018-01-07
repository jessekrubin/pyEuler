# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Prime permutations
Problem 49
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

import helpme as hm

four_dig_primes = []
for i in range(1000, 10000):
    if hm.is_prime(i):
        four_dig_primes.append(i)

# 4_dig_prime_perms = []


def str_rotations_gen(s):
    for j in range(len(s)):
        return s[j:] + s[:j]


print(str_rotations_gen('123'))
