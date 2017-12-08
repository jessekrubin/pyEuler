#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler

# Consider the divisors of 30: 1,2,3,5,6,10,15,30.
# It can be seen that for every divisor d of 30, d+30/d is prime.

# Find the sum of all positive integers n not exceeding 100 000 000
# such that for every divisor d of n, d+n/d is prime.


import helpme as hm

def funnn(d, n):
    return ((d+n)/d)

def divisors_thing(number):
    divs = hm.factors_list(number)
    new_nums = [(i + number) // i for i in divs]
    print(number)
    print(divs)
    print(new_nums)
    for num in new_nums:
        print(num)
        print(hm.is_prime(num))
    l = [hm.is_prime(j) for j in new_nums]
    print(l)
    print(all(l))

    for i in hm.divisors_gen(number):
        print("___")
        print(i)
        fun_num = (funnn(i, number))

        if not funnn(i, number).is_integer():
            return False
        else:
            if not hm.is_prime(fun_num):
                return False

    return True


print(divisors_thing(30))
