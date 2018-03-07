#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Problem 0
template
"""

from math import sqrt


def num_integer_right_triangles(perimeter):
    num_triangles = 0
    for b in range(1, perimeter // 2):
        if num_triangles > 1:
            return False
        a = (2 * b * perimeter - perimeter ** 2) / (2 * (b - perimeter))

        if a % 1:
            continue
        a = int(a)
        if a < b:
            if a ** 2 + b ** 2 == (perimeter - a - b) ** 2:
                num_triangles += 1
    if num_triangles == 0:
        return False
    return True


def singular_right_tris(l):
    sings = 0
    l_max = int(sqrt(l) / 2)
    for i in range(1, l_max):
        if num_integer_right_triangles(i):
            sings += 1
    return sings


LLL = 1500000
print(singular_right_tris(LLL))
