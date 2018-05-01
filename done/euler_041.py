# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Pandigital prime
Problem 41
We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and
is also prime.

What is the largest n-digit pandigital prime that exists?
"""
__sol__ = 7652413

from itertools import permutations
from lib.octopus_prime import is_prime


def p041():
    numslists = []
    for i in range(1, 10):
        numslists.append([x + 1 for x in range(i)])

    pandigital_numbers = []
    for j in range(len(numslists)):

        for i in permutations(numslists[j], len(numslists[j])):
            # snum = int("".join([str(k) for k in i]))
            pandigital_numbers.append(int("".join([str(k) for k in i])))

    prime_pandigitals = filter(is_prime, pandigital_numbers)
    return max(prime_pandigitals)


if __name__ == '__main__':
    ans = p041()
    print("Largest pandigital prime: {}".format(ans))
