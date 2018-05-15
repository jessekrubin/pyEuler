#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Pandigital Fibonacci ends
Problem 104
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci
number for which the last nine digits are 1-9 pandigital (contain all the
digits 1 to 9, but not necessarily in order). And F2749, which contains 575
digits, is the first Fibonacci number for which the first nine digits are
1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits
AND the last nine digits are 1-9 pandigital, find k.
"""

from itertools import permutations, count
from lib.listless import digits_to_int
from math import log, sqrt


# def approxonacci(fibn):
#     thing1 = log(sqrt(5), 10)
#     thing2 = log(1.618033988, 10)
#     t = thing2*fibn-thing1
#     t = int(pow(10, (t-int(t)+8)))
#     return t


def approxonacci(n):
    """
    Wikipedia - Computation by rounding
    https://en.wikipedia.org/wiki/Fibonacci_number
    """
    t = n*0.20898764024997873+(-0.3494850021680094)
    return int((10**(t-int(t)+8)))

def is_pandigital(n):
    print(n)
    return set(c for c in str(n) if c!='L') == set(str(i) for i in range(1, 10))

def fib_last10():
    a, b = 0, 1
    for n in count(0):
        yield a, n
        a, b = b%1000000000, a+b

for i, n in fib_last10():
    print(i, n)
    if is_pandigital(i):
        if is_pandigital(approxonacci(n)):
            break



def p104():
    pass


if __name__ == '__main__':
    p104()
