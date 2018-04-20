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
from statistics import mean

from tqdm import tqdm

from lib.vfunk import angle


c1 = 4000
c2 = 3000

def point_prob(tup):
    v1 = (c1 - tup[0],  -tup[1])
    v2 = (- tup[0], c2 - tup[1])
    return angle(v1, v2) / (2 * pi)


if __name__ == '__main__':
    points = [[i, j] for i in range(0, c1) for j in range(0, c2)]
    probs = list(tqdm(map(point_prob, points), total=len(points)))
    answer = mean(probs)
    print("probability: {}".format(answer))