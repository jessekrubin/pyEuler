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
__sol__ = None

from lib.octopus_prime import pfactors_gen
from functools import reduce
from operator import mul, itemgetter


def prime_factors_set_list(n):
    return list(set(pfactors_gen(n)))


def rad(n):
    return reduce(mul, (prime_factors_set_list(n)), 1)


def rad_list(upper_bound):
    return [(rad(n), n) for n in range(1, upper_bound + 1)]


def eee(highest, k):
    return sorted(rad_list(upper_bound=highest), key=itemgetter(0))[k - 1][1]


greatest, k = 10, 4
solution = eee(greatest, k)
solution_str = "For 1 ≤ n ≤ {}, E({}) == {}.".format(greatest, k, solution)
print(solution_str)

greatest, k = 100000, 10000
solution = eee(greatest, k)
solution_str = "For 1 ≤ n ≤ {}, E({}) == {}.".format(greatest, k, solution)
print(solution_str)
def p124():
    pass

if __name__ == '__main__':
    ANSWER = p124()
    print("Answer: {}".format(ANSWER))