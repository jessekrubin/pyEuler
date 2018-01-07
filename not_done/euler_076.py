#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler

"""
Counting summations
Problem 76
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""


def total(n):
    leest = []


def num_sums(n):
    ways = 0
    if n == 0:
        return ways + 1
    # for every integer below n...
    for i in range(n):

        # for every integer between i and n
        for j in range(i, n):
            return ways + num_sums(i - j)
    print(n)
    return n


num1 = 5
ans1 = num_sums(num1)
print("There are {} possible sums for {}".format(ans1, num1))

num2 = 100
ans2 = num_sums(num1)
print("There are {} possible sums for {}".format(ans2, num2))
