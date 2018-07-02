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

from pupy.listless import rotations_gen, digits_list, int_from_digits
from pupy.amazon_prime import prime_gen, is_prime
from pupy.decorations import cash_it


@cash_it
def is_circ_prime(n):
    digist = [int(j) for j in digits_list(n)]
    return all((is_prime(int_from_digits(i)) for i in rotations_gen(digist)))


def p035():
    return sum(1 for p in prime_gen(10 ** 6) if is_circ_prime(p))


if __name__ == '__main__':
    ANSWER = p035()
    print("# of circlular primes: {}".format(ANSWER))
