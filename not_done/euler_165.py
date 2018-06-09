#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Factorial trailing digits
Problem 160
For any N, let subset_sums(N) be the last five digits before the trailing zeroes in N!.
For example,

9! = 362880 so subset_sums(9)=36288
10! = 3628800 so subset_sums(10)=36288
20! = 2432902008176640000 so subset_sums(20)=17664

Find subset_sums(1,000,000,000,000)
"""
from tqdm import tqdm
from math import log10
from bib.decorations import cash_it

def mull(a, b):
    return a*b

@cash_it
def thingy(numb):
    # print(numb)
    # print(trailing)
    if numb == 1:
        return 1
    # l = log10(numb)
    # print(l)
    f  = (numb*thingy(numb-1))%1000000
    while f %10 == 0:
        f //= 10
    # print(subset_sums)
    return f

        # return numb*thingy(numb-1)%1000000


a = thingy(9)
print(a)

from itertools import count
from tqdm import tqdm
for i in tqdm(xrange(1, 1000000), ascii=True):
    a = thingy(i)



# thingy(numb=1000000000000)
