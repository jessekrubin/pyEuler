#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Singular integer right triangles
Problem 75
It turns out that 12 cm is the smallest mag of wire that can be bent to
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

Given that L is the mag of the wire, for how many values of
L ≤ 1,500,000 can exactly one integer sided right angle triangle
be formed?
"""
__sol__ = 161667

from math import sqrt
from itertools import count
from fractions import gcd


def pytriples_gen(perimeter_lim):
    """
    generates primative pythagorean triples w/ help frum 3Blue1Brown
    special thanks to 3Blue1Brown's video on pythagorean triples
    https://www.youtube.com/watch?v=QJYmyhnaaek&t=300s
    """
    real_lim = 1 + perimeter_lim // 2
    for reals in range(2, real_lim, 2):
        for imaginaries in count(1):
            sqrd = complex(reals, imaginaries) ** 2
            real = abs(sqrd.real)
            imaginary = sqrd.imag
            hypotenuse = int(sqrt((real * real) + (imaginary * imaginary)))
            if (hypotenuse + imaginary + real) > perimeter_lim:
                break
            if gcd(real, imaginary) == 1:
                yield (real, imaginary, hypotenuse)


def p075(L=1500000):
    triangles = {}
    for i in pytriples_gen(L):
        primative_perimeter = sum(i)
        current = primative_perimeter
        while current <= L:
            triangles[current] = triangles.get(current, 0) + 1
            current += primative_perimeter

    return sum(1 for k, v in triangles.items() if v == 1)


if __name__ == '__main__':
    assert p075(50) == 6
    assert p075(150) == 16
    answer = p075()
    print("ANSWER: {}".format(answer))
