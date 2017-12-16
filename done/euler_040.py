# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler

"""
Champernowne's constant
Problem 40
An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

import functools
import operator


def digits_list(n):
    """
    Returns a list of the base-10 digits in a number
    """

    digits = []
    cur = n
    while(cur != 0):
        digits.append(cur % 10)
        cur = cur // 10
    # digits.append(cur)
    digits.reverse()
    return digits


def concat_nums_2_length(n):
    l = []
    i = 1
    while(len(l) < 1000001):
        l += digits_list(i)
        i += 1
    return map(str, l)


s = "".join(concat_nums_2_length(12))
# print(s)
indexes = [10**i for i in range(6)]

digs = [int(s[i - 1]) for i in indexes]

ans = functools.reduce(operator.mul, digs, 1)
print("product: {}".format(ans))
