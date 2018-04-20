#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Strong Repunits
Problem 346
The number 7 is special, because 7 is 111 written in base 2, and 11 written in
base 6 (i.e. 7_10 = 11_6 = 111_2). In other words, 7 is a repunit in at least two
bases b > 1.

We shall call a positive integer with this property a strong repunit. It can be
verified that there are 8 strong repunits below 50: {1,7,13,15,21,31,40,43}.
Furthermore, the sum of all strong repunits below 1000 equals 15864.

Find the sum of all strong repunits below 10^12.
"""

import time


def ones_base_n(base, under):
    """returns 1111...1 base10 repunits for a given base under a number"""
    current = base + 1
    place = 2
    while current < under:
        current += base ** place
        place += 1
        if current < under:
            yield current


def sum_strong_repunits(upper_limit):
    """sums the strong repunites beneath the upper limit"""
    total = 0
    max_base = upper_limit.bit_length() ** 2
    for base in range(2, max_base):
        # for number in ones_base_n(base, upper_limit):
        #     total += number
        total += sum(ones_base_n(base, upper_limit))
    return total


# @tictoc()
def p346():
    return sum_strong_repunits(10**12)

if __name__ == '__main__':
    print("___")
    t0 = time.time()
    result = sum_strong_repunits(1000)
    t1 = time.time() - t0
    print("ANSWER: {}".format(result))
    print("time: {}".format(t1))

    result = p346()-30

    print("ANSWER: {}".format(result))
