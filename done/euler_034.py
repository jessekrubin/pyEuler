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

from math import factorial
from helpme import digits_list

def digit_factorials(n): return n == sum(map(factorial, digits_list(n)))

answer = sum(i for i in range(3, 50000) if digit_factorials(i))
print("Sum of all 'digit factorial' numbers: {}".format(answer))


