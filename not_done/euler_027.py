# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler

"""
Quadratic primes
Problem 27 

The incredible formula n2−79n+1601n2−79n+1601 was discovered, which produces
80 primes for the consecutive values 0≤n≤790≤n≤79. The product of the
coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+bn2+an+b, where |a|<1000|a|<1000 and |b|≤1000|b|≤1000

where |n||n| is the modulus/absolute value of nn
e.g. |11|=11|11|=11 and |−4|=4|−4|=4
Find the product of the coefficients, aa and bb, for the quadratic expression
that produces the maximum number of primes for consecutive values of nn,
starting with n=0n=0.
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


def quad_thing(n, a, b):
    return
