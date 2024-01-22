#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Step Numbers
Problem 178
Consider the number 45656.
It can be seen that each pair of consecutive digits of 45656 has a difference of one.
A number for which every pair of consecutive digits has a difference of one is called a step number.
A pandigital number contains every decimal digit from 0 to 9 at least once.
How many pandigital step numbers less than 1040 are there?
"""
from __future__ import division
from pupy.decorations import cash_it


@cash_it
def update_has(has, n):
    if str(n) in has:
        return has
    else:
        haset = set(c for c in has)
        haset.add(str(n))
        return "".join(str(c) for c in sorted(haset))


@cash_it
def rec(remaining, last, has):
    if remaining == 0 and has == "0123456789":
        return 1
    if remaining == 0 and has != "0123456789":
        return 0
    pancount = 0
    if last < 9:
        up = last + 1
        pancount += rec(remaining - 1, up, update_has(has, up))
    if last > 0:
        down = last - 1
        pancount += rec(remaining - 1, down, update_has(has, down))
    return pancount


def pandigital_step_numbers(ndigs):
    total = 0
    for nd in range(10, ndigs + 1, 1):
        for i in range(1, 10):
            total += rec(nd - 1, i, str(i))
    return total


def p178():
    return pandigital_step_numbers(40)


if __name__ == "__main__":
    assert 55 == pandigital_step_numbers(13)
    ANSWER = p178()
    print("# PANDIGITAL STEP NUMBERS LESS THAN 10^40 {}".format(ANSWER))
