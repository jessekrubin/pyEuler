# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Distinct primes factors
Problem 47
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?
"""

from itertools import count
from biblioteca import pfactors_gen, cash_muney


@cash_muney
def n_distict_pfactors(n):
    return len([pf for pf in pfactors_gen(n)])


def p047(n_facs=4):
    num_prime_factors = {}
    for i in count(10):
        if i > 134050: break
        num_prime_factors[i] = n_distict_pfactors(i)
        if i > 10 and num_prime_factors[i] == n_facs:
            if all(n_facs == num_prime_factors[i-j] for j in range(n_facs)):
                return i+1-n_facs


if __name__ == '__main__':
    assert 14 == p047(2)
    assert 644 == p047(3)
    ANSWER = p047()
    print("ANSWER: {}".format(ANSWER))