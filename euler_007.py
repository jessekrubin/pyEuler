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

def is_prime(n):
    """is_prime(n) returns True if n is prime

    Doctests:
    >>> is_prime(10)
    False
    >>> is_prime(17)
    True
    """
    import math

    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

i = 1
n_primes = 0
nth_prime = 10001
while(n_primes < nth_prime + 1):
    if(is_prime(i)):
        n_primes += 1
    i += 1

answer = (i - 1)
print("10,001th prime is: {}".format(answer))
