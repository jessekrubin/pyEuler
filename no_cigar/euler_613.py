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
from bib.maths import Vuple

try:
    xrange
except NameError:
    xrange = range

c1 = 40
c2 = 30

__sol__ = 0.3916721504

# def point_prob(tup):
#     v1 = (3-tup[0], -tup[1])
#     v2 = (- tup[0], c2-tup[1])
#     return Vuple.angle(v1, v2)
#
# # 0.3916904685875669
# # 0.3916904685876032
#
# if __name__ == '__main__':
#     points = [[i, j] for i in xrange(0, c1) for j in xrange(1, c2)]
#     probs = list(tqdm(map(point_prob, points), total=len(points)))
#     answer = (sum(probs)/float(len(probs)))/(2*pi)
#     print("probability: {}".format(answer))

from scipy.integrate import dblquad
import numpy as np


def integrand(y, x):
    """y must be the first argument, and x the second."""
    return y * np.sin(x) + x * np.cos(y)


# c1 = 400
# c2 = 300

# c1 = 300
# c2 = 400

# yp = Vuple((0, 30))
# xp = Vuple((40, 0))
#
# def point_prob(x, y):
#     v1 = (40-x, y)
#     v2 = (x, 30-y)
#     return Vuple.angle(v2, v1)/(2*pi)
#
#
# # ans, err = dblquad(point_prob, 1, 4, lambda x: 1, lambda x: 3)
# ans, err = dblquad(point_prob, 0, 40, lambda x: 0, lambda x: 30-(x*(0.75)))
# print(ans)
# print(ans/2)
# print(ans/(2 * pi))
# print((ans-360)/360)
# print((360-ans)/360)
# print((360-ans)/720)

xz = 4
yz = 3


def point_prob(x, y):
    v1 = (xz - x, y)
    v2 = (x, yz - y)
    return Vuple.angle(v2, v1, radians=False)


# ans, err = dblquad(point_prob, 1, 4, lambda x: 1, lambda x: 3)
def yyy(x):
    return yz - x * 0.75


# ans, err = dblquad(point_prob, 0, xz, lambda x: 0, lambda x: yz-(x*(yz/xz)))
ans, err = dblquad(point_prob, 0, xz, lambda x: 0, yyy)
print(ans)
print(ans / 180)
print(ans / 6)
print(ans / (2 * pi))
print((ans - 360) / 360)
print((360 - ans) / 360)
print((360 - ans) / 720)
