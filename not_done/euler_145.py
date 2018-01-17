#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
How many reversible numbers are there below one-billion?
Problem 145
Some positive integers n have the property that the sum [ n + reverse(n) ]
consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and
409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and
904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (109)?
"""

from helpme import is_perfect_square


for x in range(4, 1000000):
    for y in range(3, x):
        for z in range(2, y):
            if is_perfect_square((x+y)):
                if is_perfect_square(x-y):
                    if is_perfect_square(x+z):
                        if is_perfect_square(x-z):
                            if is_perfect_square(y+z):
                                if is_perfect_square(y-z):
                                    print(x, y, z)
                                    break

