#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Summation of primes
Problem 10 
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from bib.amazon_prime import prime_gen


def p010():
    return sum(p for p in prime_gen(2000000))


# 1179908152
if __name__ == '__main__':
    answer = p010()
    print("Sum: {}".format(answer))
