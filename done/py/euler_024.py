#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler

"""
Lexicographic permutations
Problem 24
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits:
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from itertools import permutations


def p024():
    # enumerate the permutations
    for index, permutation in enumerate(permutations('0123456789')):
        # return the integer representation of the permutation
        if index + 1 == 1000000: return int(''.join(permutation))


if __name__ == '__main__':
    ANSWER = p024()
    print("i = 1,000,000: {}".format(ANSWER))
