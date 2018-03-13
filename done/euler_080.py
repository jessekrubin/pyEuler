#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Square root digital expansion
Problem 80
It is well known that if the square root of a natural number is not an integer,
then it is irrational. The decimal expansion of such square roots is infinite
without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the
first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums
of the first one hundred decimal digits for all the irrational square roots.
"""

from decimal import getcontext, Decimal
from lib.listless import digits_list

getcontext().prec = 111

def sum_n_decimal_digits(number, digits):
    return sum(digits_list(int(Decimal(number).sqrt() * 10**(digits-1) // 1)))

def p080():
    # make a set of the perfect squares
    perf_squares = {i**2 for i in range(1, 11)}

    # return the sum of the first 100 digits of each number if it is not a perf square
    return sum(sum_n_decimal_digits(j, 100) for j in range(1, 100 + 1) if j not in perf_squares)


answer = p080()
print(answer)
