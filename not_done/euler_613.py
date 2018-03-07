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

from math import sqrt, acos, pi
from multiprocessing import Pool
from statistics import mean
from tqdm import tqdm
from lib.vfunk import dotproduct, angle




def get_vecs(tup):
    c1 = (400, 0)
    c2 = (0, 300)
    v1 = (c1[0] - tup[0], c1[1] - tup[1])
    v2 = (c2[0] - tup[0], c2[1] - tup[1])
    return v1, v2


v = [
    i
    for i in map(get_vecs, ((x, y) for x in range(1, 300, 1)
                            for y in range(1, 400, 1)))
]
p = Pool(16)
# angs = p.map(angle, vecs)
# print(mean(angs))
# print(stdev(angs))

list1 = []
for _ in tqdm(p.imap_unordered(angle, v), total=len(v)):
    list1.append(abs(_))

list2 = [(i / pi) for i in list1]
print(mean(list1))
print(mean(list1) / pi)
print(mean(list2))
