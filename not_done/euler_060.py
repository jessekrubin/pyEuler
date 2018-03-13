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

from lib.octopus_prime import is_prime
from itertools import combinations


def num_digits(number):
    d = number
    digs = 0
    while d > 0:
        d //= 10
        digs += 1
    return digs

def concat_numbers(a, b):
    return a*10**(num_digits(b)) + b

def check_pair(pair):
    if is_prime(concat_numbers(pair[0], pair[1])) and is_prime(concat_numbers(pair[1], pair[0])):
        return True
    else:
        return False

def is_prime_pair_set(primes):
    print(primes)
    return all(check_pair(c) for c in combinations(primes, 2))

test_set = [3, 7, 109, 673]
assert True == is_prime_pair_set(test_set)



