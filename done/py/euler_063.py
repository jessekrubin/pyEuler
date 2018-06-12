#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Powerful digit counts
Problem 63
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit
number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
from itertools import count


def powerful_digits(n):
    max_n_digit_num = (10 ** n) - 1
    current = 0
    n_powerful_digits = 0
    for i in count(1):
        current = i ** n
        if 10 ** (n - 1) <= current < 10 ** n:
            n_powerful_digits += 1
        elif current > max_n_digit_num:
            return n_powerful_digits


def number_of_powerful_digits():
    total_powerful_digits = 0
    for ndigs in count(1):
        result = powerful_digits(ndigs)
        total_powerful_digits += result
        if result == 0:
            return total_powerful_digits


def p063():
    return number_of_powerful_digits()


if __name__ == '__main__':
    answer = p063()
    print("Total number of powerful digits: {}".format(answer))