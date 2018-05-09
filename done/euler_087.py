#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Prime power triples
Problem 87
The smallest number expressible as the sum of a prime square, prime cube, and
prime fourth power is 28. In fact, there are exactly four numbers below fifty
that can be expressed in such a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the sum of a prime
square, prime cube, and prime fourth power?
"""

from lib.maths import prime_gen
from lib.decorations import tictoc
from math import sqrt


def power_triple(triple):
    return sum(triple[index] ** (index + 2) for index in range(3))


def prime_power_triples(below):
    primes = [p for p in prime_gen(int(sqrt(below)+1))]
    n_primes = len(primes)
    hermy = [0] * below
    for first in range(n_primes):
        for second in range(n_primes):
            for third in range(n_primes):
                pt = power_triple([primes[third],
                                   primes[second],
                                   primes[first]])
                if pt > below:
                    break
                hermy[pt] = 1
    return sum(hermy)


def p087():
    return prime_power_triples(50000000)


if __name__ == '__main__':
    MY_ANSWER = p087()
    print("ANSWER: {}".format(MY_ANSWER))