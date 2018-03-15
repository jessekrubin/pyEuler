#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Coin partitions
Problem 78
Let p(n) represent the number of different ways in which n coins can be
separated into piles. For example, five coins can be separated into piles
in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
"""

from itertools import count
import functools


def p(n):
    sums = [0] * (n+1)
    sums[0] = 1
    for num in range(1, n+1):
        for i in range(num, n+1):
            sums[i] += sums[i - num]
    print(sums)
    return sums

#
# def p(n):
#     if n < 2:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         # sums = [0] * (n+1)
#         # sums[0] = 1
#         tot = 0
#         for num in range(1, n+1):
#             for i in range(num, n+1):
#                 # print("")
#                 # print(i, num)
#
#                 tot += p(num - i-1)
#         return tot

a = p(4)
print(a)
# print(p(5))
# print(p(6))

# for i in range(2, 20):
#     print("__")
#     print(i)
#     print(p(i))


# def p():
#     n = 2
#
#     sums = [1, 0]
# #     for n in count(2):
#         sums = [0] * (n - 1)
#         sums[0] = 1
#         # print(sums)
#         # for num in range(1, n):
#             print(sums)
#             # for i in range(num, n):
#                 print("")
#                 print(sums)
#                 print(len(sums))
#                 print(i-num)
#                 # sums[i] += sums[i - num]
#         # yield sums[-1]
#         # sums.append(0)

#         if n > 20:
#             break
#
# for i in p():
#     print(i)
#


