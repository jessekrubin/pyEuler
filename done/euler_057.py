#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Square root convergents
Problem 57
It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than denominator?
"""

from biblioteca import cash_it
from fractions import Fraction


@cash_it
def sqrt_2_recursion(n_expansions):
    if n_expansions == 1:
        return Fraction(4, 2)
    return Fraction(2+Fraction(1, sqrt_2_recursion(n_expansions-1)))


def sqrt_2_expansions(ex):
    return sqrt_2_recursion(ex+1)-1


def num_gt_denom(frac):
    return len(str(frac.numerator)) > len(str(frac.denominator))


def p057():
    return sum(1 for expansion in range(1, 1001) if num_gt_denom(sqrt_2_expansions(expansion)))


if __name__ == '__main__':
    assert Fraction(3, 2) == sqrt_2_expansions(1)
    assert Fraction(7, 5) == sqrt_2_expansions(2)
    assert Fraction(17, 12) == sqrt_2_expansions(3)
    assert Fraction(41, 29) == sqrt_2_expansions(4)
    assert Fraction(1393, 985) == sqrt_2_expansions(8)
    assert True == num_gt_denom(sqrt_2_expansions(8))
    sol = p057()
    assert sol == 153
    print("Solution: {}".format(sol))