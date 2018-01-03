#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Summation of primes
Problem 10 
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import functools


@functools.lru_cache(maxsize=None)
def is_prime(n):
    """
    is_prime(n) returns True if n is prime
    """
    import math

    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


primes = sum([i for i in range(2000000) if is_prime(i)])
print("Sum: {}".format(primes))
