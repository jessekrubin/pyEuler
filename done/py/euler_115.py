#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Counting block combinations II
Problem 115
NOTE: This is a more difficult version of Problem 114.

A row measuring n units in length has red blocks with a minimum length of m
units placed on it, such that any two red blocks (which are allowed to be
different lengths) are separated by at least one black square.

Let the fill-count function, F(m, n), represent the number of ways that a row
can be filled.

For example, F(3, 29) = 673135 and F(3, 30) = 1089155.

That is, for m = 3, it can be seen that n = 30 is the smallest value for which
the fill-count function first exceeds one million.

In the same way, for m = 10, it can be verified that F(10, 56) = 880711 and
F(10, 57) = 1148904, so n = 57 is the least value for which the fill-count
function first exceeds one million.

For m = 50, find the least value of n for which the fill-count function first
exceeds one million.
"""

from pupy.decorations import cash_it
from itertools import count


@cash_it
def f(m, n, last_one=True):
    if n == 0:
        return 1
    else:
        blockcount = 0
        blockcount += f(m, n - 1, True)
        if last_one:
            for i in range(m, n + 1):
                blockcount += f(m, n - i, False)
        return blockcount


def p115():
    for i in count(50):
        if f(50, i) > 1000000:
            return i


if __name__ == '__main__':
    assert f(3, 29) == 673135
    assert f(3, 30) == 1089155
    assert f(10, 56) == 880711
    assert f(10, 57) == 1148904
    ANSWER = p115()
    print("LEAST VALUE OF N: {}".format(ANSWER))
