#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse and Graham Rubin
"""
Truncatable primes
Problem 37 
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import functools
import math

@functools.lru_cache(maxsize=None)
def is_prime(n):
    """
    is_prime(n) returns True if n is prime
    """
    if n == 1:
        return False
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def trunk_prime(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        return False
    if not is_prime(n):
        return False
    digs = [i for i in str(n)]
    for i in range(1, len(digs)):
        right= int("".join(digs[i:]))
        # print(right)
        p = 1-i
        left = int("".join(digs[:i]))
        if not is_prime(right) or not is_prime(left):
            return False

    return True
    # print(left)


print(trunk_prime(3797))


primes = [ i for i in range(2, 100000) if trunk_prime(i) ]
print((primes))
print(len(primes))
print(max(primes))
