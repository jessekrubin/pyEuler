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

from helpme import prime_factorization

def distinct_primes_factors(n_distinct_factors):
    num_prime_factors = {}
    i = 0
    while True:
        i += 1
        num_prime_factors[i] = len(set(prime_factorization(i)))
        if i > 10 and num_prime_factors[i] == n_distinct_factors:
            if all(n_distinct_factors == num_prime_factors[i - j] for j in range(n_distinct_factors)):
                return i + 1 - n_distinct_factors


# print(distinct_primes_factors(2))
# print(distinct_primes_factors(3))
answer = distinct_primes_factors(4)
print(answer)

