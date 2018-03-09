#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Semiprimes
Problem 187
A composite is a number containing at least two prime factors. For example,
15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

There are ten composites below thirty containing precisely two, not
necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 108, have precisely two, not necessarily
distinct, prime factors?
"""


from lib.octopus_prime import prime_sieve_gen
from math import sqrt

def semi_prime_sieve(upper_bound):
    primes_tomul = list(n for n in prime_sieve_gen(upper_bound))
    n_primes = len(primes_tomul)
    for i in range(n_primes):
        # print(i)
        for second in range(i, n_primes):
            mul = primes_tomul[i] * primes_tomul[second]
            if mul < upper_bound:
                yield mul
            elif mul > upper_bound:
                break

def semi_prime_search(upper_bound):
    primes_tomul = list(n for n in prime_sieve_gen(upper_bound))
    n_primes = len(primes_tomul)

    def max_index(x):
        start = 0
        end = len(primes_tomul)
        while start < end:
            mid = (start + end) // 2
            if x < primes_tomul[mid]:
                end = mid
            elif x > primes_tomul[mid]:
                start = mid + 1
            elif x == primes_tomul[mid]:
                return mid
            else:
                raise AssertionError()
        return -start - 1

    ans = 0
    for (i, p) in enumerate(primes_tomul):
        if p > int(sqrt(upper_bound) + 1):
            break
        end = max_index(upper_bound // p)
        ans += (end + 1 if end >= 0 else -end - 1) - i
    return str(ans)

# n_semiprimes = sum(1 for _ in semi_prime_sieve(10**8))
# print(n_semiprimes)
print(semi_prime_search(10 ** 8))
