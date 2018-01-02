#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project euler
"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def str_is_pal(s):
    """Returns True if string is a palindrome.

    Doctests:
    >>> str_is_pal("racecar")
    True
    >>> str_is_pal("greg")
    False
    """

    for i, c in enumerate(s):
        if c != s[-i - 1]:
            return False
    return True


palindrome_numbers = max(
    map(int,
        filter(str_is_pal, (str(int(i * j))
                            for i in range(100, 1000)
                            for j in range(100, 1000)))))

print("max paindrome: {}".format(palindrome_numbers))
