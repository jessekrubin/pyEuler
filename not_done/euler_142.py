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

perfect_squares = set([i**2 for i in range(10000000)])


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

