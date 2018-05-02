#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Tribonacci non-divisors
Problem 225
The sequence 1, 1, 1, 3, 5, 9, 17, 31, 57, 105, 193, 355, 653, 1201 ...
is defined by T1 = T2 = T3 = 1 and Tn = Tn-1 + Tn-2 + Tn-3.

It can be shown that 27 does not divide any terms of this sequence.
In fact, 27 is the first odd number with this property.

Find the 124th odd number that does not divide any terms of the above sequence.
"""

from functools import lru_cache
from itertools import count


@lru_cache(maxsize=None)
def trib(n):
    if n < 3:
        return 1
    else:
        return trib(n-1)+trib(n-2)+trib(n-3)


def nth_non_div_odd(n):
    odd = 27
    nthnum = 1
    for i in count(1):
        print(trib(i))

        if i > 50:
            break


nth_non_div_odd(1)
