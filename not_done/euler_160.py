#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Factorial trailing digits
Problem 160
For any N, let f(N) be the last five digits before the trailing zeroes in N!.
For example,

9! = 362880 so f(9)=36288
10! = 3628800 so f(10)=36288
20! = 2432902008176640000 so f(20)=17664

Find f(1,000,000,000,000)
"""

from functools import lru_cache

from tqdm import tqdm


@lru_cache(maxsize=None)
def mull(a, b):
    return a*b

def thingy(numb=9, trailing=5):
    # print(numb)
    # print(trailing)
    fact = 1
    for n in tqdm(range(1, numb), total=numb):
        # print(fact)
        mul = n+1
        while mul%10==0:
            mul//=10
        mul %= 10**trailing

        fact = mull(mul, fact)
        while fact%10==0:
            fact//=10
        fact %= 10**trailing
    print(fact)

thingy(numb=20, trailing=5)
thingy(numb=1000000000000, trailing=5)
