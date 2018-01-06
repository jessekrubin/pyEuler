#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Summation of primes
Problem 10 
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import helpme as hm

primes = sum((i for i in range(2000000) if hm.is_prime(i)))
print("Sum: {}".format(primes))
