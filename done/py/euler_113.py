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
from bib.decorations import cash_it


def non_bouncy(tenexp):
    """Count non bouncy numbers below 10**tenexp

    the increasing and decreasing functions count number with two or more
    dijits, and doesn't count 1, nor 2, nor 3, nor 4, nor 5, nor 6, nor 7,
    nor 8, nor 9, which are all non-bouncy; so 9 is added.
    """

    @cash_it
    def _increasing(remaining_digits, last):
        """Count increasing numbers recursively"""
        if remaining_digits == 0: return 1
        return sum(_increasing(remaining_digits-1, next)  # increasing count w/ params
                   for next in range(last, 10))  # ge than the last number

    @cash_it
    def _decreasing(remaining_digits, last, start=None):
        """Count decreasing numbers
        excluding numbers with all the same digits"""
        if start is None: start = last
        if remaining_digits == 0:
            if start != last: return 1
            else: return 0  # Double counted numbers
        return sum(_decreasing(remaining_digits-1, i, start)
                   for i in range(0, last+1))

    return 9+sum(_decreasing(n_dij, start_dij)+_increasing(n_dij, start_dij)
                 for start_dij in range(1, 10)
                 for n_dij in range(1, tenexp))


def p113():
    return non_bouncy(100)


if __name__ == '__main__':
    assert 12951 == non_bouncy(6)
    ANSWER = p113()
    print("# bouncy numbers less than 10**100: {}".format(ANSWER))
