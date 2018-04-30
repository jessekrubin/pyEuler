#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Combinatoric selections
Problem 053

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr = n!/r!(n−r)!,

where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are
greater than one-million?
"""
__sol__ = 4075

from lib.decorations import cash_muney

@cash_muney
def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n - 1) * n


def choose(a, b):
    if a >= b:
        return fact(a) / (fact(b) * fact(a - b))
    else:
        raise Exception("b>a; which isnt supposed to happen")


up_bound = 100
total_over_a_mil = 0
for N in range(1, up_bound + 1):
    for i in range(1, N):
        if choose(N, i) > 1000000:
            total_over_a_mil += 1

print("ANSWER: {}".format(total_over_a_mil))
def p053():
    pass

if __name__ == '__main__':
    p053()