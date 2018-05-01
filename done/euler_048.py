#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Self powers
Problem 48
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""
__sol__ = 9110846700


def power_series(number):
    series_sum = 0
    for i in range(1, number + 1):
        series_sum += i ** i
    return series_sum


def p048():
    return power_series(1000) % 10000000000

if __name__ == '__main__':
    answer = p048()
    print("Answer: {}".format(answer))
