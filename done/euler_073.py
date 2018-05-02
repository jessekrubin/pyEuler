#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Counting fractions in a range
Problem 73
Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of
size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7,
3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper
fractions for d ≤ 12,000?
"""
__sol__ = 7295372

from operator import floordiv
from fractions import Fraction
from sys import version_info

if version_info.major > 2:
    xrange = range


def ordered_fractions(d):
    fracs = set()
    half = Fraction(1, 2)
    third = Fraction(1, 3)
    for denom in range(2, d + 1):
        for numerator in range(floordiv(denom, 3), floordiv((2 + denom), 2)):
            f = Fraction(numerator, denom)
            if half > f > third:
                fracs.add(f)
    return len(fracs)


def p073():
    return ordered_fractions(12000)


if __name__ == '__main__':
    assert 3 == ordered_fractions(8)
    answer = p073()
    print("# fracs: {}".format(answer))
