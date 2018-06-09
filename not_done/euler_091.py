#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
"""

from bib import xrange
from bib.maths import pytriple_gen
from math import sqrt


def basic_tris(max_xy):
    total = 0
    for i in xrange(1,max_xy+1):
        # iso rightangles
        total += 3
        for j in xrange(1, i):
            total += 6
        if i%2==0:
            total += 2
    return total

def comp_tris(max_xy):
    total = 0
    max_c = int(sqrt((max_xy**2)*2)+1)
    for tri in pytriple_gen(max_c):
        print(tri)
    return total



def thing(n):
    a = basic_tris(n) + comp_tris(n)
    print(a)
    return a

thing(2)
thing(10)
