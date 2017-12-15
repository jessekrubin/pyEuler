#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
# SOLVED

# Circular primes
# Problem 35
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

import helpme as hm
from itertools import permutations


def rotate_list(l, n):
    """

    >>> rotate_list(l, n)
    """
    return l[-n:] + l[:-n]


one_nine_seven = hm.digits_list(197)

# print(one_nine_seven)
# print(rotate_list(one_nine_seven, 1))


def num_rotations_gen(l):
    for i in range(len(l)):
        yield (l[-i:] + l[:-i])


def dig_list_2_int(l):
    l.reverse()
    d = 0
    for i in range(len(l)):
        d += (l[i] * 10**i)
    return d


allits = num_rotations_gen(one_nine_seven)
print(allits)

from functools import lru_cache


@lru_cache(maxsize=None)
def is_circ_prime(n):
    # print(n)
    # print(hm.is_prime(n))
    digist = [int(j) for j in hm.digits_list(n)]
    return all(
        (hm.is_prime(dig_list_2_int(i)) for i in num_rotations_gen(digist)))


num_circ_primes = 0
for i in range(1, 1000000):
    if is_circ_prime(i):
        print("i is {}".format(i))
        num_circ_primes += 1

print("# of circlular primes: {}".format(num_circ_primes - 1))