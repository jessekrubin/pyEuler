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

from lib.maths import fib_r, n_digits


def p025(no_digits=1000):
    n_fib_digs = 0
    i = 0
    while n_fib_digs < no_digits:
        n_fib_digs = n_digits(fib_r(i))
        i += 1
    return i


if __name__ == '__main__':
    assert 12 == p025(3)
    answer = p025()
    print("index of first fib_gen num w/ 1000 digits: {}".format(answer))