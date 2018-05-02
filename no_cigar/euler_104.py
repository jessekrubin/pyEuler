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

Given that Fk is the first Fibonacci number for which the first nine digits AND
the last nine digits are 1-9 pandigital, find k.
"""
__sol__ = None

from itertools import permutations
from lib.listless import dig_list_2_int


def fib_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b


def first_ten_pan_digital(n):
    last_9 = n%1000000000
    if last_9 in pandigital_numbers:
        flrst_nine = n
        while flrst_nine > 1000000000:
            flrst_nine //= 10
        if flrst_nine in pandigital_numbers:
            return True
    return False


one2nine = [i for i in range(1, 10)]
pandigital_numbers = set(dig_list_2_int(i) for i in permutations(one2nine))
fibs = fib_gen(99999999)
i = 0
while True:
    i += 1
    fi = next(fibs)
    if fi > 100000000000:
        if first_ten_pan_digital(fi):
            break
print(i-1)


def p104():
    pass


if __name__ == '__main__':
    p104()
