#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Permuted multiples
Problem 52

It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""

from bib.listless import is_permutation
from itertools import count


def permuted_multiples(max_multiplier=6):
    for n_digits in count(2):
        for number in range(10 ** (n_digits - 1), ((10 ** n_digits) // max_multiplier)):
            if all(is_permutation(number, number * multiplier) for multiplier in range(2, max_multiplier + 1)):
                return number
        if n_digits > 30:
            break


def p052():
    return permuted_multiples(6)


if __name__ == '__main__':
    result = p052()
    print("Smallest integer: {}".format(result))