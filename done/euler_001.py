#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from lib.decorations import tictoc

@tictoc(1000)
def fives_n_threes(upper_bound):
    return sum(i for i in range(upper_bound) if (i % 3 == 0) or (i % 5 == 0))

answer = fives_n_threes(upper_bound=1000)
print("Sum: {}".format(answer))  # Sum: 233168
