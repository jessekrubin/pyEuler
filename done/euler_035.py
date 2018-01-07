#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler

"""
Circular primes
Problem 35
The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from helpme import is_circ_prime

num_circ_primes = 0
for i in range(1, 1000000):
    if is_circ_prime(i):
        num_circ_primes += 1

print("# of circlular primes: {}".format(num_circ_primes - 1))
