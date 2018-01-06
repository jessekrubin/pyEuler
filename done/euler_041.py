# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler

"""We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?"""

from itertools import permutations
from functools import lru_cache


@lru_cache(maxsize=None)
def is_prime(n):
    """is_prime(n) returns True if n is prime

    Doctests:
    >>> is_prime(10)
    False
    >>> is_prime(17)
    True
    """
    import math

    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


numslists = []
for i in range(1, 10):
    numslists.append([x + 1 for x in range(i)])

pandigital_numbers = []
for j in range(len(numslists)):
    l = []

    for i in permutations(numslists[j], len(numslists[j])):
        # snum = int("".join([str(k) for k in i]))
        pandigital_numbers.append(int("".join([str(k) for k in i])))

prime_pandigitals = filter(is_prime, pandigital_numbers)

print("Largest pandigital prime: {}".format(max(prime_pandigitals)))
