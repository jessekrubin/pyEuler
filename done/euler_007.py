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

from helpme import is_prime

ind = 1
n_primes = 0
nth_prime = 10001
while n_primes < nth_prime + 1:
    if is_prime(ind):
        n_primes += 1
    ind += 1

answer = (ind - 1)
print("10,001th prime is: {}".format(answer))
