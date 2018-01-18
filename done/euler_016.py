#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin ~ Project Euler
"""
Power digit sum
Problem 16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

from helpme import digits_list

ANSWER = sum(digits_list(2**1000))
print("Sum of digits of 2^1000: {}".format(ANSWER))