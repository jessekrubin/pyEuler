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
good_divs = [20, 19, 18, 17, 16, 14, 13, 11]

answer = 20
while True:
    if all(answer % n == 0 for n in good_divs):
        break
    answer += 20

print("Answer: {}".format(answer))
