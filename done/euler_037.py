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
__sol__ = 748317

from lib.octopus_prime import is_prime


def trunk_prime(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        return False
    if not is_prime(n):
        return False
    digs = [i for i in str(n)]
    for i in range(1, len(digs)):
        right = int("".join(digs[i:]))
        # print(right)
        left = int("".join(digs[:i]))
        if not is_prime(right) or not is_prime(left):
            return False

    return True
    # print(left)


primes = [i for i in range(2, 1000000) if trunk_prime(i)]
print("Trunk-Ate-Able primes: {}".format(primes))
print("Num trunk primes: {}".format(len(primes)))
print("SUM: {}".format(sum(primes)))
answer = """
Trunk-Ate-Able primes: [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
Num trunk primes: 11
SUM: 748317
"""
def p037():
    pass

if __name__ == '__main__':
    p037()