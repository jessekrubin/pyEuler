#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Prime pair connection
Problem 134
Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that
1219 is the smallest number such that the last digits are formed by p1 whilst
also being divisible by p2.

In fact, with the exception of p1 = 3 and p2 = 5, for every pair of consecutive
primes, p2 > p1, there exist values of n for which the last digits are formed
by p1 and n is divisible by p2. Let S be the smallest of these values of n.

Find ∑ S for every pair of consecutive primes with 5 ≤ p1 ≤ 1000000.
"""

from pyximport import install; install()
from bib.amazon_prime import prime_gen
from tqdm import tqdm
################################
# solution = 18613426663617118 #
################################


def p134_cy(lim=1000000):
    from bib.cybib.prime_pairs import prime_pair_cy
    primes = [p for p in prime_gen(lim+5) if p > 3]
    mod10e = 10
    multipliers = []
    for i in tqdm(range(len(primes)-1), ascii=True):
        if primes[i] > mod10e: mod10e *= 10
        multipliers.append(prime_pair_cy(primes[i], primes[i+1], mod10e))
    return sum(a*b for a, b in zip(primes[1:], multipliers))

# OLD AND SLOW
# 3:10 (min:sec) runtime with pypy
# def p134_py(lim=1000000):
#     def _pp(p1, p2, mod_tens):
#         """prime pair (connection)"""
#         ret = p2
#         mul = 1
#         mul_by = 2  # the multiplication is always by 2 so skip every other
#         while ret%mod_tens != p1:
#             ret += mul_by*p2
#             ret %= mod_tens
#             mul += mul_by
#         return mul*p2
#
#     upper_bound_p1 = lim+5  # get one more prime larger than 1000000
#     primes = [p for p in prime_gen(upper_bound_p1) if p > 3]
#     total = 0
#     mod_tens = 10
#     for i in tqdm(range(len(primes)-1), ascii=True):
#         if primes[i] > mod_tens:
#             mod_tens *= 10
#         total += _pp(primes[i], primes[i+1], mod_tens)
#     return total


if __name__ == '__main__':
    # assert 53 == prime_pair_cy(19, 23, 100)
    ANSWERcy = p134_cy(1000000)
    print(ANSWERcy)

    # ANSWER = p134_py(1000000)
    # print("ANSWER: {}".format(ANSWER))




    # ANSWER = p134_py()
    # print("ANSWER: {}".format(ANSWER))  # ANSWER: 18613426663617118
