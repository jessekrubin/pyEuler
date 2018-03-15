#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Prime pair sets
Problem 60
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these
four primes, 792, represents the lowest sum for a set of four primes with
this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""

from lib.octopus_prime import is_prime, prime_sieve_gen
from itertools import combinations
from collections import defaultdict
from functools import lru_cache

@lru_cache(maxsize=None)
def num_digits(number):
    d = number
    digs = 0
    while d > 0:
        d //= 10
        digs += 1
    return digs

@lru_cache(maxsize=None)
def concat_numbers(a, b):
    return a*10**(num_digits(b)) + b

@lru_cache(maxsize=None)
def check_pair(p1, p2):
    if is_prime(concat_numbers(p1, p2)) and is_prime(concat_numbers(p2, p1)):
        return True
    else:
        return False

# @lru_cache(maxsize=None)
def is_prime_pair_set(primes):
    # print(primes)
    return all(check_pair(c[0], c[1]) for c in combinations(primes, 2))

test_set = (3, 7, 109, 673)
assert True == is_prime_pair_set(test_set)

def prime_pair_sets(set_size):
    pairs = defaultdict(set)
    past_primes = []

    def look_up_is_prime_pair_set(comb):
        return set.intersection(*[pairs[c] for c in comb])

    for p in prime_sieve_gen():
        for pp in past_primes:
            if check_pair(p, pp):
                pairs[p].add(pp)
                pairs[pp].add(p)
                pairs[p].add(p)
                pairs[pp].add(pp)

        for comb in combinations(pairs[p], set_size-1):
            sssss = look_up_is_prime_pair_set(comb)
            if len(sssss) == set_size:
                return sum(sssss)
        past_primes.append(p)


answer = prime_pair_sets(4)
print(answer)
answer = prime_pair_sets(5)
print(answer)

