#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Integer right triangles
Problem 39
If pytriple_sum is the perimeter of a right angle triangle with integral mag
sides, {a,b,c}, there are exactly three solutions for pytriple_sum = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of pytriple_gen ≤ 1000, is the number of solutions maximised?
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


def p039():
    n_right_tris = [num_integer_right_triangles(p) for p in range(1, 1001)]
    best_perimeter, num_tris = max(enumerate(n_right_tris), key=itemgetter(1))
    return best_perimeter + 1  # bc array storage


if __name__ == '__main__':
    ans = p039()
    print("A perimeter = {} has 8 integer right triangles".format(ans))
