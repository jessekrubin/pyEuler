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


def p(n):
    sums = [0] * (n+1)
    sums[0] = 1
    for num in range(1, n+1):
        for i in range(num, n+1):
            sums[i] += sums[i - num]
    print(sums)
    return sums

a = p(4)
print(a)
