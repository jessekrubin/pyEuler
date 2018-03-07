#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Digit fifth powers
Problem 30
Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
"""

from lib.listless import digits_list

def digit_powers(number, power): return number == sum(map(lambda x: x**power, digits_list(number)))



fifth_pows = list(i for i in range(4000, 200000) if digit_powers(i, 5));
answer = sum(fifth_pows)
print("Digit fifth powers: {}".format(fifth_pows))
print("SUM: {}".format(answer))


