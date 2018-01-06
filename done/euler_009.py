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


# combos = []
# for i in range(1, 1000):
#     for j in range(i):
#         for k in range(j):
#             thing = tuple((i, j, k))
#             if sum(thing) == 1000:
#                 combos.append(thing)
def is_p_triplet(t):
    # print   (t)
    if t[0] > t[1] or t[0] > t[2] or t[1] > t[2] or t[0] < 0 or t[0] == t[1] or t[1] == t[2]:
        return False
    else:
        if t[2] ** 2 == t[1] ** 2 + t[0] ** 2:
            return True
        else:
            return False


combos = []
for i in range(1, 1000):
    for j in range(i):
        trio = [i, j, (1000 - i - j)]
        trio.sort()
        trio = tuple(trio)
        combos.append(trio)
        # print(l)

combos = set(combos)
for trip in filter(is_p_triplet, combos):
    triplet = trip
    product = triplet[0] * triplet[1] * triplet[2]
    print("Triplet product: {}".format(product))
