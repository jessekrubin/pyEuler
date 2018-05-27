#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Perfect Square Collection
Problem 142
Find the smallest x + y + z with integers x > y > z > 0 such that

x + y, x − y, x + z, x − z, y + z, y − z

are all perfect squares.
"""
from __future__ import  division
from bib import xrange
from itertools import combinations

squares = [i*i for i in range(0, 10**6)]
indcombso= combinations((i for i in xrange(2, 10**5)), 2)
# print(squares)
for i in indcombso:
    ymz, ypz = i
    # print(xmy, xpy)
    twoy = squares[ypz] + squares[ymz]
    # twox = squares[ypz] - squares[ymz]
    if twoy%2 ==0:
        print(ymz, ypz, twoy)
    # y =
    #     print(x)

    # x_plux_y, x_plus_z, x_minus_z, x_minus_y = reversed(i)

    # x_plux_y, x_minus_y, x_plus_z, x_minus_z, y_plux_z, y_minus_z = reversed(i)
    # print(x_plux_y, x_minus_y, x_plus_z, x_minus_z, y_plux_z, y_minus_z)
    # print(x_plux_y, x_minus_y, x_plus_z, x_minus_z)
    # x = (x_plux_y+x_minus_y)/2
    # x2 = (x_plus_z+x_minus_z)/2
    # y = (y_plux_z+y_minus_z)/2

    # print(x, x2)
    # if x == x2:
    #     break



"""
x + y, x − y, 
x + z, x − z, 
y + z, y − z


x + y,
x − y, 
x + z,
x − z,

y + z,
y − z
"""

#
# for x in range(4, 1000000):
#     for y in range(3, x):
#         for z in range(2, y):
#             if is_perfect_square((x+y)):
#                 if is_perfect_square(x-y):
#                     if is_perfect_square(x+z):
#                         if is_perfect_square(x-z):
#                             if is_perfect_square(y+z):
#                                 if is_perfect_square(y-z):
#                                     print(x, y, z)
#                                     break

