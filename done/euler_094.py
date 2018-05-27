#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Almost equilateral triangles
Problem 94
It is easily proved that no equilateral triangle exists with integral mag
sides and integral area. However, the almost equilateral triangle 5-5-6 has
an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two
sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles w/ integral
side lengths and area and whose perimeters do not exceed one billion
(1,000,000,000).
"""
from bib.maths import pytriple_gen
from time import time


def almost_equilateral(max_perimeter):
    """
    Generates almost equilateral triangles

    Almost-equilateral-triangles (AET):
        A triangle for which two sides are equal and the third differs by no
        more than one unit.


    An AET is really just 2 pythag-triple-triangles (back 2 back), where double
    the shortest leg in the triple +/-1 is equal to the hypotenuse (c). For an
    AET max perimeter of p, we look at pythagorean triples with c < p/3.
    """
    for tri in pytriple_gen((max_perimeter+3)//3):
        if abs(tri[-1]-(tri[0]*2)) == 1:
            yield (tri[0]*2, tri[-1], tri[-1])


def p094(max_perimeter=(10**9)):
    perimeter_sum = 0
    for i in almost_equilateral(max_perimeter):
        perimeter_sum += sum(i)
    return perimeter_sum


if __name__ == '__main__':
    assert 66 == p094(100)
    assert 984 == p094(1000)
    ti = time()
    sol = p094()
    tf = time()
    print("Solution: {}".format(sol))
    print("Time:     {} ms".format((tf-ti)*1000))