#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Palindromic sums
Problem 125

The palindromic number 595 is interesting because it can be written as the sum
of consecutive squares: 62 + 72 + 82 + 92 + 102 + 112 + 122.

There are exactly eleven palindromes below one-thousand that can be written as
consecutive square sums, and the sum of these palindromes is 4164. Note that
1 = 02 + 12 has not been included as this problem is concerned with the squares
of positive integers.

Find the sum of all the numbers less than 108 that are both palindromic and can
be written as the sum of consecutive squares.
"""
__sol__ = 2906969179
from math import sqrt
from itertools import count
from lib.string_theory import is_palindrome


def some_pals(upper_bound):
    for i in range(1, int(sqrt(upper_bound)+1)):
        # print(i)
        cur = i*i
        for j in count(i+1):
            cur += j*j
            if cur >= upper_bound:
                break
            elif is_palindrome(str(cur)):
                yield cur


def p125():
    return sum(set(pal for pal in some_pals(10**8)))


if __name__ == '__main__':
    assert sum(set(pal for pal in some_pals(10**3))) == 4164
    answer = p125()
    print("Solution: {}".format(answer))
