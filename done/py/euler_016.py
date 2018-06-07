#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin ~ Project Euler
"""
Power digit sum
Problem 16
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""


def p016(n=2**1000):
    return sum(int(c) for c in str((n)))


if __name__ == '__main__':
    assert p016(2**15) == 26
    answer = p016()
    print("Sum of digits of 2^1000: {}".format(answer))
