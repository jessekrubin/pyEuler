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

from lib.octopus_prime import is_prime, prime_sieve_gen
from tqdm import tqdm
from tqdm import trange

lower_bound_p1 = 5
upper_bound_p1 = 1000000

def prime_pair_connection(p1, p2, mod_tens):
    ret = p2*11
    mul = 11
    mul_by = 2 # the multiplication is always by 2 so skip every other
    while ret%mod_tens!=p1:
        ret += mul_by*p2
        ret %= mod_tens
        mul += mul_by
    return mul * p2

assert 1219 == prime_pair_connection(19, 23, 100)

primes = [p for p in prime_sieve_gen(upper_bound_p1+5) if p > 3]

total = 0
mod_tens = 10
for i in trange(len(primes) - 1, ascii=True):
    if primes[i] > mod_tens:
        mod_tens *= 10
    total += prime_pair_connection(primes[i], primes[i+1], mod_tens)

print(total)

# 18613431715334298