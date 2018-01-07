#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler

# Consider the divisors_gen of 30: 1,2,3,5,6,10,15,30.
# It can be seen that for every divisor d of 30, d+30/d is prime.

# Find the sum of all positive integers n not exceeding 100,000,000
# such that for every divisor d of n, d+n/d is prime.

from functools import lru_cache
from helpme import divisors_list, is_prime


@lru_cache(maxsize=None)
def funnn(d, n):
    return d + (n / d)


def divisors_thing(number):
    for i in divisors_list(number):
        fun_num = (funnn(i, number))
        if not funnn(i, number).is_integer():
            return False
        else:
            if not is_prime(fun_num):
                return False
    return True


total = 0
for i in range(1, 100000000):
    if divisors_thing(i):
        # print(i)
        total += i
