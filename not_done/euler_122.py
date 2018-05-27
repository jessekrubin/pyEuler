#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Efficient exponentiation
Problem 122
The most naive way of computing n15 requires fourteen multiplications:

n × n × ... × n = n15

But using a "binary" method you can compute it in six multiplications:

n × n = n**2
n**2 × n**2 = n**4
n**4 × n**4 = n**8
n**8 × n**4 = n**12
n**12 × n**2 = n**14
n**14 × n = n**15

However it is yet possible to compute it in only five multiplications:

n × n = n**2
n**2 × n = n**3
n**3 × n**3 = n**6
n**6 × n**6 = n**12
n**12 × n**3 = n**15

We shall define m(k) to be the minimum number of multiplications to compute nk;
for example m(15) = 5.

For 1 ≤ k ≤ 200, find ∑ m(k).
"""
from itertools import chain

from bib.amazon_prime import pfactors_gen


def expo(d, n):
    """
    returns the number of times a divisor divides n (is the exponent)

    :param d: divisor
    :param n: number being divided
    :return:
    """
    if n < d:  # flip
        d, n = n, d
    c = n
    divs = 0
    while c%d == 0:
        c //= d
        divs += 1
    return divs


def pfactorization(n):
    return (n for n in chain.from_iterable([p]*expo(p, n) for p in pfactors_gen(n)))


def m(k):
    print("+++")
    print("K", k)
    factorization = list(pfactorization(k))
    print(factorization)


# result = m(16)
# print(result)
# result = m(15)
# print(result)
# result = m(18)
# print(result)
# result = m(15)
# print(result)
# for i in range(1, 10):
#     print("___")
#     print(i)
#     print(m(i))
print(m(15))

