#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Counting rectangles
Problem 85
By counting carefully it can be seen that a rectangular grid measuring 3 by 2
contains eighteen rectangles.

Although there exists no rectangular grid that contains exactly two million
rectangles, find the area of the grid with the nearest solution.
"""
__sol__ = None


# num rectangles is (height**2 + height) times (width**2 + width)
# all over four
# this equation is simple enough to figure out, though it took me a while and
# I tore some of my hari out
def num_rectangles(height, width): return ((height ** 2 + height) * (width ** 2 + width)) // 4


numrectdict = {}
# so go ahead and just try abunch, i guess
for i in range(1, 100):
    for j in range(1, i + 1):
        numrectdict[abs(2000000 - num_rectangles(i, j))] = i * j

min_key = min(numrectdict.keys())  # min key is going to be the closes
print("AREA w/ nearest solution: {}".format(numrectdict[min_key]))
def p085():
    pass

if __name__ == '__main__':
    p085()