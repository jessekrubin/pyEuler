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

from helpme import is_palindrome

palindrome_numbers = max(
    map(int,
        filter(is_palindrome, (str(int(i * j))
                               for i in range(100, 1000)
                               for j in range(100, 1000)))))

print("max paindrome: {}".format(palindrome_numbers))
