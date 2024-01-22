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

from pupy.foreign import digits_list
from functools import reduce
from operator import mul


def concat_nums_2_length():
    n_list = []
    i = 1
    while len(n_list) < 1000001:
        n_list += digits_list(i)
        i += 1
    return map(str, n_list)


def p040():
    s = "".join(concat_nums_2_length())
    indexes = [10**i for i in range(6)]
    digs = [int(s[i - 1]) for i in indexes]
    return reduce(mul, digs, 1)


if __name__ == "__main__":
    SOL = p040()
    print("Expression val: {}".format(SOL))
