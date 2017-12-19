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

l = [2, 3, 5, 7, 11, 13, 17, 18, 19, 20]

i = 2
while(not all([i % x == 0 for x in l])):
    i += 1

answer = i
print("Answer: {}".format(answer))
