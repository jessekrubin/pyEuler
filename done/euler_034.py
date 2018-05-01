#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Digit factorials
Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
__sol__ = 40730

from math import factorial
from lib.listless import digits_list


def is_digit_factorial(n):
    return n == sum(map(factorial, digits_list(n)))


def digit_factorials(upper_bound):
    return sum(i for i in range(3, upper_bound) if is_digit_factorial(i))


def p034():
    return digit_factorials(500000)


if __name__ == '__main__':
    ANSWER = p034()
    print("Sum of all 'digit factorial' numbers: {}".format(ANSWER))
