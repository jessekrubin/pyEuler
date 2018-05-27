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


def tuple2string(t):
    return ''.join(t)


def p024():
    numbers = [str(i) for i in range(10)]
    strangs = []
    for i in permutations(numbers, len(numbers)):
        strangs.append(tuple2string(i))
    return int(strangs[999999])


if __name__ == '__main__':
    answer = p024()
    print("i = 1,000,000: {}".format(answer))


