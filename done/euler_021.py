#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Amicable numbers
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a
and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from lib.maths import divisors_gen
from lib.decorations import cash_muney


@cash_muney
def sum_proper_divisors(n):
    return sum(divisors_gen(n)) - n


def p021():
    amicable_numbers = set()
    for a in range(10, 10000):
        b = sum_proper_divisors(a)
        c = sum_proper_divisors(b)
        if a == c and a != b:
            amicable_numbers.add(a)
    return sum(amicable_numbers)


if __name__ == '__main__':
    ans = p021()
    print("Sum of amicable numbers below 10000: {}".format(ans))