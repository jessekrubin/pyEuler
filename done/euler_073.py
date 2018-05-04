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

from math import ceil, floor
from lib.maths import itgcd
from lib.octopus_prime import prime_gen

try: xrange
except NameError: xrange = range

__sol__ = 7295372


def fractions_in_range(max_denom):
    primes = set(p for p in prime_gen(max_denom))
    count = 0
    for denom in xrange(4, max_denom+1):
        min_n = int(floor(denom/3))
        max_n = int(ceil(denom/2))
        if denom in primes:
            count += max_n-min_n
        else:
            for numerator in xrange(min_n, max_n):
                if itgcd(numerator, denom) == 1:
                    count += 1
    return count


def p073a(d=12000):
    return fractions_in_range(d)


if __name__ == '__main__':
    assert 3 == fractions_in_range(8)
    answer = p074a()
    print("# fracs: {}".format(answer))
