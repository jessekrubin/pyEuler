#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
from operator import itemgetter
from bib.decorations import cash_it
from bib import xrange


@cash_it
def collatz_len(n):
    if n == 1: return 1
    elif n%2 == 0: return collatz_len(n//2)+1
    else: return collatz_len(3*n+1)+1


def p014():
    return max(((i, collatz_len(i)) for i in xrange(1, 1000000)),
               key=itemgetter(1))[0]+1


if __name__ == '__main__':
    LONGEST_CHAIN = p014()
    print("{} produces the longest collatz sequence".format(LONGEST_CHAIN))
