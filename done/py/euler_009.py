#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Special Pythagorean triplet
Problem 9 
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from bib.maths import pytriple_gen
from bib.listless import iter_product


def p009():
    """
    for each possible pythagorean triplet:
        if 1000 is divisible by the sum of the triplet:
            RETURN: multiply product and the multiplier cubed
    """
    for tri in pytriple_gen(int(1000 // 2)):
        if 1000 % sum(tri) == 0:
            return iter_product(tri) * (1000 // sum(tri)) ** 3


if __name__ == '__main__':
    product = p009()
    print("Triplet product: {}".format(product))

#######
# OLD #
#######
# def is_p_triplet(t):
#     if t[0] > t[1] or t[0] > t[2] or t[1] > t[2] or t[0] < 0 or t[0] == t[1] or t[1] == t[2]:
#         return False
#     else:
#         if t[2]**2 == t[1]**2+t[0]**2:
#             return True
#         else:
#             return False
#
#
# def p009_OLD():
#     combos = set()
#     for i in range(1, 1000):
#         for j in range(i):
#             trio = [i, j, (1000-i-j)]
#             trio.sort()
#             trio = tuple(trio)
#             combos.add(trio)
#     combos = set(combos)
#     for triplet in filter(is_p_triplet, combos):
#         return triplet[0]*triplet[1]*triplet[2]
