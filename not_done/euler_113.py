#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Non-is_bouncy numbers
Problem 113
Working from left-to-right if no digit is exceeded by the digit to its left it
is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a
decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a
"bouncy" number; for example, 155349.

As n increases, the proportion of bouncy numbers below n increases such that
there are only 12951 numbers below one-million that are not bouncy and only
277032 non-bouncy numbers below 10**10.

How many numbers below a googol (10**100) are not bouncy?
"""
from lib.listless import digits_list


def is_bouncy(n):
    digits = digits_list(n)
    increasing = False
    decreasing = False
    for i in range(0, len(digits)-1):
        if digits[i+1] < digits[i]:
            increasing = True
        elif digits[i+1] > digits[i]:
            decreasing = True
        if increasing and decreasing:
            return True
    return False


def is_inc(n):
    digits = digits_list(n)
    for i in range(0, len(digits)-1):
        if digits[i+1] < digits[i]:
            return False
    return True


def is_dec(n):
    digits = digits_list(n)
    for i in range(0, len(digits)-1):
        if digits[i+1] > digits[i]:
            return False
    return True


incs = []
decs = []
both = []
for i in range(1, 10**6):
    # print(i, is_bouncy(i), is_inc(i), is_dec(i))
    if is_inc(i) and is_dec(i):
        both.append(i)
    elif is_inc(i) and not is_dec(i):
        incs.append(i)
    elif is_dec(i) and not is_inc(i):
        decs.append(i)

print(incs)
print(decs)
print(both)
print(len(incs))
print(len(decs))
print(len(both))
print((len(incs)+len(decs)-len(both)))
print(len(set.union(set(incs), set(decs), set(both))))

