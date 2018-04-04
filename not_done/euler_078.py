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
from functools import lru_cache


def p(n):
    sums = [0] * (n+1)
    sums[0] = 1
    for num in range(1, n+1):
        for i in range(num, n+1):
            sums[i] += sums[i - num]%1000000
        if num %100 ==0:

            print(sums[num])
        # if num %1000 ==0:
        #     print(sums)
    return sums

print(p(55374))
@lru_cache(maxsize=None)
def partitions(n, I=1):
    if n < 2:
        return 1
    else:
        total = 1
        for i in range(I, n//2 + 1):
            total += partitions(n-i, i)
        return total

@lru_cache(maxsize=None)
def partitions2(n, I=1):
    if n < 2:
        return 1
    else:
        total = 1
        for i in range(I, n//2 + 1):
            total += partitions(n-i, i)
        return total % 1000000

a = p(4)
print(a)
a = partitions(4)
print(a)

a = p(5)
print(a)
a = partitions(5)
print(a)

# def p078():
#     div = 100
#     for i in count(1):
#         # thing = (partitions(i))
#         thing2 = (partitions2(i))
#         if i % 100 == 0:
#             print(i, thing2)
#         if thing2 % 1000000 == 0:
#             print("rit here")
#             print(thing2)
#             return i
#         if thing2 == 0:
#             print(thing2)
#             return i
#
# print(p078())

# def thingy():
#     for n in count(1):
#         sums = [0] * (n+1)
#         sums[0] = 1
#         for num in range(1, n+1):
#             for i in range(num, n+1):
#                 sums[i] += sums[i - num]%1000000
#         if n%100 == 0:
#
#             print(n,sums[-1])




thingy()
