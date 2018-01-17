#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Perfect Square Collection
Problem 142
Find the smallest x + y + z with integers x > y > z > 0 such that

x + y, x − y, x + z, x − z, y + z, y − z

are all perfect squares.
"""

from helpme import is_palindrome


def palindromic_sums(limit):
    # create squares below limit
    for startnum in range(limit // 2):
        nums = []
