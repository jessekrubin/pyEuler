#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""
__sol__ = None


def sq_sum_diff(num_numbers):
    return sum([i + 1 for i in range(num_numbers)]) ** 2 - sum([(i + 1) ** 2 for i in range(num_numbers)])


def p006():
    return sq_sum_diff(100)


if __name__ == '__main__':
    assert 2640 == sq_sum_diff(10)
    answer = p006()
    print("Difference ({}): {}".format(100, answer))  # Difference(100): 25164150
