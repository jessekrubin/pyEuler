#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Jesse Rubin ~ project Euler ~
"""
Problem Name
prob #

Prompt
"""
from bib.maths import pytriple_gen, Vuple
from math import sqrt
from itertools import count


def cuboid_routes(m):
    max_hypotlength = sqrt(1 + (5 * (m**2)))
    total = 0
    for p in pytriple_gen(max_hypotlength):
        trip = Vuple(p)
        a, b, c = p
        print("")
        print(trip)
        for i in range(b - a + 1, a):
            print(a, b - i, i)
            voop = Vuple((a, b - i, i))

            # print(max(voop))

            # total += 1
            print(m // max(voop))
            total += m // max(voop)

        # while trip[0] < m and trip[1] < m:

        # b is coing to be made up of the shorter two sides of the box
    print(total)


cuboid_routes(100)


def p086():
    pass


if __name__ == '__main__':
    p086()
