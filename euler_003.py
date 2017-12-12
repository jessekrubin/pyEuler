#!/usr/bin/env python
# -*- coding: utf-8 -*-
# phil and samantha and jesse

# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import helpme as hm


def get_prime_factors(number):
    factors = (hm.factors(number))
    letmewin = filter(hm.is_prime, factors)
    print(letmewin)
    for primefacks in (letmewin):
        print(primefacks)


get_prime_factors(600851475143)
