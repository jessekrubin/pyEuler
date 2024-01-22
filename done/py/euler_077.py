#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Prime summations
Problem 77
It is possible to write ten as the sum of primes in exactly five different
ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over
five thousand different ways?
"""
from pupy.amazon import is_prime


def prime_sums(n):
    # this is the same as my coin sums code
    primes = [p for p in range(2, n) if is_prime(p)]
    ok_primes = [i for i in primes if i < (n + 1)]
    # print(ok_coins)
    sums = [0] * (n + 1)
    sums[0] = 1
    for prime in ok_primes:
        for i in range(prime, n + 1):
            sums[i] += sums[abs(i - prime)]
    return sums[n]


def p077():
    answer = None
    i = 3
    while answer is None:
        i += 1
        if prime_sums(i) > 5000:
            return i


# test_pupy case
# n1 = 10
# ans1 = coin_partitions(n1)
# print("{} ways to make {}".format(ans1, n1))
if __name__ == "__main__":
    answer = p077()
    print("Answer: {}".format(answer))
