#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Ordered radicals
Problem 124
The radical of n, rad(n), is the product of the distinct prime factors of n.
For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on
n if the radical values are equal, we get:

something weirdly formatted

Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and
E(6) = 9. If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).
"""

from bib.amazon_prime import prime_factors_gen
from operator import mul, itemgetter

try: reduce
except: from functools import reduce


def prime_factors_set_list(n):
    return list(set(prime_factors_gen(n)))


def rad(n):
    return reduce(mul, (prime_factors_set_list(n)), 1)


def rad_list(upper_bound):
    return [(rad(n), n) for n in range(1, upper_bound+1)]


def eee(highest, k):
    return sorted(rad_list(upper_bound=highest), key=itemgetter(0))[k-1][1]


def p124(greatest=10**5, k=10**4):
    return eee(greatest, k)


if __name__ == '__main__':
    assert 8 == eee(10, 4)
    ANSWER = p124()
    print("For 1 ≤ n ≤ 10**5, E(10**4) == {}.".format(ANSWER))