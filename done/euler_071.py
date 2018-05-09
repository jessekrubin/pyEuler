#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Counting fractions
Problem 71

Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of
size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7,
3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending
order of size, find the numerator of the fraction immediately to the left of
3/7.
"""


def ordered_fractions(d):
    right_denom = 7
    right_numerator = 3
    left_denom = 7
    left_numerator = 2
    for denom in range(d, 2, -1):
        frac_multiplied = (right_numerator*denom-1)//right_denom
        if frac_multiplied*left_denom > left_numerator*denom:
            left_denom = denom
            left_numerator = frac_multiplied
    return left_numerator, left_denom


def p071():
    numerator, denom = ordered_fractions(1000000)
    return numerator


if __name__ == '__main__':
    assert (2, 5) == ordered_fractions(8)
    sol = p071()
    print("Numerator: {}".format(sol))