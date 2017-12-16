#!/usr/bin/env python
# -*- coding: utf-8 -*-
# phil and samantha and jesse

"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

from itertools import count


def smallest_divisible_by_1_(n):
    l = [i+1 for i in range(n)]
    i = 1
    while(True):
        if all(i % x == 0 for x in l):
            return i
        i += 1

answer = smallest_divisible_by_1_(20)
print("Answer: {}".format(answer))
