#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Almost equilateral triangles
Problem 94
It is easily proved that no equilateral triangle exists with integral length
sides and integral area. However, the almost equilateral triangle 5-5-6 has
an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two
sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles w/ integral
side lengths and area and whose perimeters do not exceed one billion
(1,000,000,000).
"""
from fractions import gcd
from math import sqrt
from itertools import count

def pytriples_gen(perimeter_lim):
    """
    generates primative pythagorean triples w/ help frum 3Blue1Brown
    special thanks to 3Blue1Brown's video on pythagorean triples
    https://www.youtube.com/watch?v=QJYmyhnaaek&t=300s
    """
    real_lim = 1 + perimeter_lim // 2
    for reals in range(2, real_lim, 2):
        for imaginaries in count(1):
            sqrd = complex(reals, imaginaries)**2
            real = abs(int(sqrd.real))
            imaginary = int(sqrd.imag)
            hypotenuse = int(sqrt((real * real) + (imaginary * imaginary)))
            if (hypotenuse+imaginary+real) > perimeter_lim:
                break
            if gcd(real, imaginary) == 1:
                if real < imaginary:
                    yield (real, imaginary, hypotenuse)
                else:
                    yield (imaginary, real, hypotenuse)
from tqdm import tqdm
def is_almost_equilateral(tri):
    print(tri)

total = 0
for i in tqdm(pytriples_gen(1000000000), ascii=True):
    total += 1

print(total)
