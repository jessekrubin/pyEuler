#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Problem 0
template
# THIS IS A TEMPLATEEEEE

Consider the alphabet A made out of the letters of the word "project": A={c,e,j,o,p,r,t}.
Let T(n) be the number of strings of length n consisting of letters from A that do not have a substring that is one of the 5040 permutations of "project".

T(7)=77-7!=818503.
Find T(1012). Give the last 9 digits of your answer.
"""

from lib.maths import cash_factorial
from math import factorial


def tee(n):
    return 7 ** n - factorial(7)


assert tee(7) == 818503


def tee2(n):
    return n ** n, factorial(n)


print(tee2(10))
print(tee2(100))
print(tee2(1000))

print(tee(10 ** 18))
