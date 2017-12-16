#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Special Pythagorean triplet
Problem 9 
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

l = []
for i in range(1000):
    for j in range(1000 - i):
        for k in range(1000 - (i + j)):
            if sum((i, k, j)) == 1000:
                l.append((i, j, k))
print(len(l))
