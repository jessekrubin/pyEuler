#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - Project Euler
"""
Pythagorean Ant
Problem 613 
Dave is doing his homework on the balcony and, preparing a presentation about 
Pythagorean triangles, has just cut out a triangle with side lengths 30cm, 40cm 
and 50cm from some cardboard, when a gust of wind blows the triangle down into 
the garden.

Another gust blows a small ant straight onto this triangle. The poor ant is 
completely disoriented and starts to crawl straight ahead in random direction 
in order to get back into the grass.

Assuming that all possible positions of the ant within the triangle and all 
possible directions of moving on are equiprobable, what is the probability that 
the ant leaves the triangle along its longest side?

Give your answer rounded to 10 digits after the decimal point.
"""

from math import pi
from multiprocessing import Pool
from statistics import mean

from tqdm import tqdm

from lib.vfunk import angle


def get_vecs(tup):
    c1 = (400, 0)
    c2 = (0, 300)
    v1 = (c1[0] - tup[0], c1[1] - tup[1])
    v2 = (c2[0] - tup[0], c2[1] - tup[1])
    return v1, v2

print(get_vecs((0, 0)))

