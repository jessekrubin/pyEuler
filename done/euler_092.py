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

from functools import lru_cache
from lib.listless import digits_list


def next_num(n):
    d = digits_list(n)
    m = 0
    for p in d:
        m += p * p
    return m


@lru_cache(maxsize=None)
def goes2_89(n):
    while True:
        if n == 89:
            return True
        elif n == 1:
            return False
        else:
            return goes2_89(next_num(n))


many_lines = 0
for i in range(1, 10000000):
    if goes2_89(i):
        many_lines += 1

print("# of numbers that go to 89: {}".format(many_lines))

one_line = sum((1 for i in range(1, 10000000) if goes2_89(i)))
print("# of numbers that go to 89: {}".format(one_line))
