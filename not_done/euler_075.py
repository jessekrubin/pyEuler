#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Singular integer right triangles
Problem 75
It turns out that 12 cm is the smallest length of wire that can be bent to
form an integer sided right angle triangle in exactly one way, but there are
many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an
integer sided right angle triangle, and other lengths allow more than one
solution to be found; for example, using 120 cm it is possible to form
exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of
L ≤ 1,500,000 can exactly one integer sided right angle triangle
be formed?
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
