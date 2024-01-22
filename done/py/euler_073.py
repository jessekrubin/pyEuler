#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Counting fractions in a range
Problem 73
Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of
size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7,
3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper
fractions for d ≤ 12,000?
"""
from __future__ import division

from pupy.maths import gcd_it
from pupy.amazon import prime_gen

try:
    range
except NameError:
    range = range


def fractions_in_range(max_d=12000, gtd=3, ltd=2):
    """number of reduced proper fractions in a range

    Args:
        max_d: maximum denominator
        gtd: greater than denominator
        ltd: less than denominator

    Returns:
        int: no. reduced proper fractions, frac, such that frac > (1/gtd) and
             and frac < (1/ltd)

    """
    primes = set(p for p in prime_gen(max_d))
    nfractions = 0
    for denominator in range(4, max_d + 1):
        min_n = denominator // gtd + 1
        max_n = denominator // ltd + 1
        if denominator in primes:
            nfractions += max_n - min_n
        else:
            for numerator in range(min_n, max_n):
                if gcd_it(numerator, denominator) == 1:
                    nfractions += 1
    return nfractions


def p073():
    return fractions_in_range()


if __name__ == "__main__":
    assert 3 == fractions_in_range(8)
    answer = p073()
    print("# fracs: {}".format(answer))
