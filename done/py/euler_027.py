# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler

"""
Quadratic primes
Problem 27 

The incredible formula n^2−79n+1601 was discovered, which produces
80 primes for the consecutive values 0≤n≤790≤n≤79. The product of the
coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000 where |n| is the modulus/absolute value
of n (e.g. |11|=11 and |−4|=4). Find the product of the coefficients, a and b,
for the quadratic expression that produces the maximum number of primes for
consecutive values of n, starting with n=0.
"""

from bib.amazon_prime import is_prime


def quad(n, a, b):
    return (n * n) + (a * n) + b


def sequece_length(a, b):
    n = 0
    while True:
        numb = abs(quad(n, a, b))
        if not is_prime(numb):
            return n
        n += 1


def p027():
    combos = [(i, j) for i in range(-1000, 1001, 1) for j in range(-1000, 1001, 1)]
    maxseq = 1
    c = (1, 1)
    for combo in combos:
        sl = sequece_length(combo[0], combo[1])
        if sl > maxseq:
            maxseq = sl
            c = combo
    return c[0] * c[1]


if __name__ == '__main__':
    ANSWER = p027()
    print("a*b: {}".format(ANSWER))