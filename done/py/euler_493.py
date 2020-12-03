#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Jesse Rubin ~ project Euler ~
"""
Under The Rainbow
Problem 493
https://projecteuler.net/problem=493
70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.

What is the expected number of distinct colors in 20 randomly picked balls?

Give your answer with nine digits after the decimal point (a.bcdefghij).
"""
from __future__ import division

from pupy.maths import n_choose_r


def p493():
    a = n_choose_r(70, 20)  # total combinations
    b = n_choose_r(60, 20)  # combinations if a set of 10 balls is removed
    p = b / a  # prob that a single color is not picked
    ip = 1 - p  # inverse is prob that a color was picked/present at the end
    return ip * 7  # bc there are 7 possible colors


if __name__ == '__main__':
    ANSWER = p493()
    print("ANSWER: {:1.9f}".format(ANSWER))  # ANSWER: 6.818741802
