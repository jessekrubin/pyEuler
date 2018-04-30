#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Factorial digit sum
Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is:
3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
__sol__ = 648

from math import factorial
from lib.listless import digits_list

number = 100
answer = sum(digits_list(factorial(number)))
print("Sum of the digits of {}!: {}".format(number, answer))
def p020():
    pass
if __name__ == '__main__':    p020()