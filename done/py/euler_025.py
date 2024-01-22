#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to
contain 1000 digits?
"""

from pupy.maths import fib_r
from itertools import count


def p025(no_digits=1000):
    for i in count():
        if len(str(fib_r(i))) >= no_digits:
            return i + 1


if __name__ == "__main__":
    assert 12 == p025(3)
    ANSWER = p025()
    print("index of first fib_gen num w/ 1000 digits: {}".format(ANSWER))
