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

How many different ways can one hundred be written as a sum of at least two
positive integers?
"""


# this is the same as my coin sums code
def num_sums(n):
    numbers_lt = [p for p in range(1, n)]
    sums = [0] * (n + 1)
    sums[0] = 1
    for number in numbers_lt:
        for i in range(number, n + 1):
            sums[i] += sums[(i - number)]
    return sums[n]


numero = 100
number_o_sums = num_sums(numero)
print("{} can be written as a sum of at least two positive integers {} ways.".format(numero, number_o_sums))
