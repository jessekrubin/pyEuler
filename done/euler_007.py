#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin

"""
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""

from lib.octopus_prime import is_prime, prime_sieve_gen
from lib.decorations import tictoc
from itertools import count

def p007(nth_prime=10001):
    ind = 1
    n_primes = 0
    while n_primes < nth_prime + 1:
        if is_prime(ind):
            n_primes += 1
        ind += 2
    return ind-1

if __name__ == '__main__':
    answer = p007()
    print("10,001th prime is: {}".format(answer))

