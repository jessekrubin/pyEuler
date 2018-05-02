#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Powerful digit sum
Problem 56
A googol (10100) is a massive number: one followed by one-hundred zeros;
100100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the
maximum digital sum?
"""
__sol__ = 972

from lib.listless import digits_list


def p056():
    return max((sum(digits_list(i**j)) for i in range(1, 100) for j in range(1, 100)))


if __name__ == '__main__':
    max_dig_sum = p056()
    print("Max digit sum: {}".format(max_dig_sum))
