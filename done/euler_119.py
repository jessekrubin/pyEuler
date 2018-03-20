#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Digit power sum
Problem 119
The number 512 is interesting because it is equal to the sum of its digits
raised to some power: 5 + 1 + 2 = 8, and 8**3 = 512. Another example of a
number with this property is 614656 = 284.

We shall define an to be the nth term of this sequence and insist that a
number must contain at least two digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30.
"""

def digits_sum(number):
    tot = 0
    while number > 0:
        tot += number % 10
        number //= 10
    return tot

a = []
for num in range(2, 100):
    for exponent in range(1, 20):
        aaa = num ** exponent
        if digits_sum(aaa) == num and aaa > 10:
            a.append(aaa)
            a.sort()

a.sort()
print(a[29])
