#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Counting numbers with at least four distinct prime factors less than 100
Problem 268
It can be verified that there are 23 positive integers less than 1000 that are
divisible by at least four distinct primes less than 100.

Find how many positive integers less than 1016 are divisible by at least four
distinct primes less than 100.
"""

from itertools import combinations
from bib import xrange
from bib.amazon_prime import prime_gen
from bib.listless import reduce_product

primes = [p for p in prime_gen(100)]
print(primes)
lt100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
         43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

n = 0
for i in xrange(100, 1000):
    t = 0
    for p in lt100:
        if i%p == 0:
            t += 1
    if t > 3:
        print(i, t)
        n += 1

print(n)

def powers_lt(n, lim):
    i = n
    while i <= lim:
        yield i
        i *= n



d = {}
s = set()
for p in lt100:
    print(list(powers_lt(p, 1000)))
    s.update(set(powers_lt(p, 1000)))
t = len(s)
for rrr in range(2, 4):
    for c in combinations(s, r=rrr):
        if (reduce_product(c)) < 1000: t += 1
print(t)

# t = 1
# while(t<10**16):
#     t*=2
#     print(t)
