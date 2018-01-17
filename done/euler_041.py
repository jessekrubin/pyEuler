# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Pandigital prime
Problem 41
We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and
is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from itertools import permutations
from helpme import is_prime

numslists = []
for i in range(1, 10):
    numslists.append([x + 1 for x in range(i)])

pandigital_numbers = []
for j in range(len(numslists)):

    for i in permutations(numslists[j], len(numslists[j])):
        # snum = int("".join([str(k) for k in i]))
        pandigital_numbers.append(int("".join([str(k) for k in i])))

prime_pandigitals = filter(is_prime, pandigital_numbers)

print("Largest pandigital prime: {}".format(max(prime_pandigitals)))
