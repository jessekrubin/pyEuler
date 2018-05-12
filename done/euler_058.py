#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Spiral primes
Problem 58
Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side mag 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side mag 9 will be formed. If this process is continued, what is the
side mag of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?
"""

from lib.amazon_prime import is_prime
from operator import truediv


def spiral_prime_iterator(ratio_bound):
    ratio = 0.5
    i = 0
    addon = 2
    adds = 0
    no_primes = 0
    total_nums = 0
    while ratio > ratio_bound:
        if adds > 0 and adds%4 == 0:
            addon += 2
        i += addon
        adds += 1
        total_nums += 1
        if is_prime(i+1):
            no_primes += 1
        ratio = truediv(no_primes, total_nums)
    return addon+1


def p058():
    return spiral_prime_iterator(0.1)


if __name__ == '__main__':
    ANSWER = p058()
    print("ANSWER: {}".format(ANSWER))