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
from __future__ import division
from math import log
from itertools import count

# def approxonacci(n):
#     """
#     Wikipedia - Computation by rounding
#     https://en.wikipedia.org/wiki/Fibonacci_number
#
#     """
#     # t = n*0.20898764024997873-0.3494850021680094
#     # return int(10**(t-int(t)+8))
#     phi = (1 + sqrt(5))/2.0
#     return int(((pow(phi,n) - (pow((1-phi), n) / sqrt(5)))))


# Python3 code to find n-th Fibonacci number

# Approximate value of golden ratio
PHI = 1.61803398874989484820
# Fibonacci numbers upto n = 5
f = [0, 1, 1, 2, 3, 5]

logroot5 = log(5) / 2
logphi = log((1 + 5 ** 0.5) / 2)

def nearest_fib(n):
    if n == 0:
        return 0
    # Approximate by inverting the large term of Binet's formula
    y = int((log(n) + logroot5) / logphi)
    lo = fast_fib(y)
    hi = fast_fib(y + 1)
    return lo if n - lo < hi - n else hi
# Function to find nth
# Fibonacci number
def approxonacci(n):
    # Fibonacci numbers for n < 6
    if n < 6:
        return f[n]

    # Else start counting from
    # 5th term
    t = 5
    fn = 5

    while t < n:
        fn = round(fn*PHI)
        t += 1

    return fn


def is_pandigital(n):
    print(n)
    return set(c for c in str(n) if c!='L') == set(str(i) for i in range(1, 10))

def fib_last10():
    a, b = 0, 1
    for n in count():
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
