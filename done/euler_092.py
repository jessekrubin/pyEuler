#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin ~ Project Euler
"""
Square digit chains
Problem 92
A number chain is created by continuously adding the square of the digits in a 
number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless 
loop. What is most amazing is that EVERY starting number will eventually arrive
at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

import functools


def digitsList(n):
    d = [int(x) for x in str(n)]
    return d


# digitsList(123) returns [1, 2, 3]


def nextNum(n):
    # print(n)
    d = digitsList(n)
    m = 0
    for p in d:
        m += p * p
    # print(m)
    return m


# nextNum(123) returns 14


@functools.lru_cache(maxsize=None)
def goes2_89(n):
    while True:
        # print("current: {}".format(n))
        if n == 89:
            return True
        elif n == 1:
            return False
        else:
            return goes2_89(nextNum(n))


count = 0
for i in range(1, 10000000):
    # print(i)
    # print(goes2_89(i))
    if goes2_89(i):
        count += 1

print("# -> 89: {}".format(count))
