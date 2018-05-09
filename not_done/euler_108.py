#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Diophantine reciprocals I
Problem 108
In the following equation x, y, and n are positive integers.

1/x+1/y=1/n

For n = 4 there are exactly three distinct solutions:

1/5+1/20 = 1/4
1/6+1/12 = 1/4
1/8+1/8  = 1/4

What is the least value of n for which the number of distinct solutions
exceeds one-thousand?

NOTE: This problem is an easier version of Problem 110; it is strongly advised
that you solve this one first.
"""

from itertools import count


def count_recips(n):
    total = 1  # because everything has at least one
    print(n)
    for i in range(n+1, 2*n):
        for j in count(2*n):
            print(i, j)
            if i*j == i*n+j*n:
                total += 1
            elif i*j > i*n+j*n:
                # print(i*j)
                # print(i*n)
                # print(n*j)
                break
                # return total
            if j > 100:
                return total


print(count_recips(4))

# def p108(limit):
#     ddd = {}
#     for x in count(1):
#         # if x > limit**2:
#         #     break
#         for y in range(1, x):
#             mulled = x * y
#             added = x + y
#             n = mulled // added
#             modded = mulled % added
#             # print(x, y, n)
#             if modded == 0:
#                 if n in ddd:
#                     ddd[n] += 1
#                     if ddd[n] > limit-1:
#                         print(ddd)
#                         return n
#                     # print(ddd[n], "HAYHAY")
#                 else:
#                     ddd.setdefault(n, 1)
#
#         # print(x, len(ddd))
#
#             # if x>20:
#             #     return ddd
# print(p108(1000))
#
