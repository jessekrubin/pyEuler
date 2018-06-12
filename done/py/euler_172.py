#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Investigating numbers with few repeated digits
Problem 172

How many 18-digit numbers n (without leading zeros) are there such that no
digit occurs more than three times in n?
"""

from bib.decorations import cash_it
from collections import Counter
from bisect import insort


@cash_it
def eighteens(count_toop):
    """recursive function for this problem"""
    if len(count_toop) == 18: return 1 # end of the line [return 1]
    c = Counter(c for c in count_toop)
    nexts = [i for i in range(10) if i not in c or c[i] < 3] # digits to try
    n_count = 0 # total count that will be added to
    for n in nexts:
        c = list(count_toop)
        insort(c, n) # insort number for caching
        n_count += eighteens(tuple(c)) # recurse and add the total
    return n_count


def p172():
    total = 0
    for i in range(1, 10):
        total += eighteens(tuple([i]))
    return total


if __name__ == '__main__':
    ANSWER = p172()
    print("# 18-digit numbers: {}".format(ANSWER))
