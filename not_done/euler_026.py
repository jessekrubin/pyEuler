# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler

"""
Reciprocal cycles
Problem 26 
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
import functools


@functools.lru_cache(maxsize=None)
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


def num_cycles(p):
    nums = set()
    print("___")
    print(p)
    one_over = float(1 / p)
    print(one_over)
    cur = one_over
    while(cur < 1):
        cur = cur * 10
    print(cur)
    cur_int = int(cur // 1)
    print(cur_int)
    # for i in range(20):


primes_under_uno_thousand = [i for i in range(1, 1000) if is_prime(i)]
print(primes_under_uno_thousand)
# one_osvers_strings = [float(1 / p) for p in primes_under_uno_thousand]

for p in primes_under_uno_thousand:
    if p < 100:
        num_cycles(p)
