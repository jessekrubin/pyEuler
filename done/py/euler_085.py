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


# num rectangles is (height**2 + height) times (width**2 + width) over four
# this equation is simple enough to figure out, though it took me a while and
# I tore some of my hari out
def num_rectangles(height, width):
    return ((height**2 + height) * (width**2 + width)) // 4


def p085():
    numrectdict = {}
    for i in range(1, 100):
        for j in range(1, i + 1):
            numrectdict[abs(2000000 - num_rectangles(i, j))] = i * j
    min_key = min(numrectdict.keys())
    return numrectdict[min_key]


if __name__ == "__main__":
    answer = p085()
    print("AREA w/ nearest solution: {}".format(answer))
