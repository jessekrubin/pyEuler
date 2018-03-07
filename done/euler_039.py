#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Integer right triangles
Problem 39
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

from operator import itemgetter


def num_integer_right_triangles(perimeter):
    num_triangles = 0
    for b in range(1, perimeter // 2):
        a = (2 * b * perimeter - perimeter ** 2) / (2 * (b - perimeter))
        if a % 1:
            continue
        a = int(a)
        if a < b:
            if a ** 2 + b ** 2 == (perimeter - a - b) ** 2:
                num_triangles += 1
    return num_triangles


n_right_tris = [num_integer_right_triangles(p) for p in range(1, 1001)]
best_perimeter, num_tris = max(enumerate(n_right_tris), key=itemgetter(1))
print("A perimeter = {} has {} integer right triangles".format(best_perimeter, num_tris))
