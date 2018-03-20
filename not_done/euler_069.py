#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Totient maximum
Problem 69
Euler's Totient function, φ(n) [sometimes called the phi function], is used to
determine the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	                1   	2
3	1,2              	2	    1.5
4	1,3	                2    	2
5	1,2,3,4	            4	    1.25
6	1,5	                2	    3
7	1,2,3,4,5,6         6	    1.1666...
8	1,3,5,7             4    	2
9	1,2,4,5,7,8	        6	    1.5
10	1,3,7,9	            4   	2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""

from math import gcd
from operator import itemgetter
from lib.maths import divisors_gen
from lib.octopus_prime import is_prime


def phi(n):
    return sum(1 for rel_p in range(1, n+1) if gcd(rel_p, n) == 1)

def n_over_phi(n):
    return n/phi(n)

def p069(upper_bound):
    phis = ((n, n_over_phi(n)) for n in range(10, upper_bound + 1, 10))
    index, value = max(phis, key=itemgetter(1))
    return index


print(p069(10))
print(p069(100))
print(p069(1000))
print(p069(10000))
print(p069(100000))