#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Largest exponential
Problem 99
Comparing two numbers written in index form like 211 and 37 is not difficult,
as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more
difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file
containing one thousand lines with a base/exponent pair on each line,
determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example
given above.
"""

from math import log
from operator import itemgetter


def log_thingy(pair):
    """
    Uses the identity log(a**x) = log(a) * x to calc aproximate value of the
    exponential terms.
    """
    return log(pair[0]) * pair[1]


def p099():
    with open("../../txt_files/p099_base_exp.txt") as f:
        pairs = [tuple(map(int, line.strip('\n').split(','))) for line in f.readlines()]
    logvals = [log_thingy(pair) for pair in pairs]
    index, log_val = max(enumerate(logvals), key=itemgetter(1))
    return index + 1


if __name__ == '__main__':
    greatest_line = p099()
    print("Line # with the greatest value is {}".format(greatest_line))
