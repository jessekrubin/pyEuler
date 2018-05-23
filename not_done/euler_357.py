#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Problem 357

Consider the divisors_gen of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100,000,000
such that for every divisor d of n, d+n/d is prime.
"""

from functools import partial

from tqdm import tqdm

from bib.amazon_prime import prime_gen


def funnn(d, n):
    return d+(n/d)


def thingy(limit):
    print("____")
    print(limit)
    D = {}
    count = 1
    primes = set(i for i in (prime_gen(limit)))

    # print("\nprimes made")
    def divisors_thing(divs, n):
        return all(i in primes for i in map(partial(funnn, n=n), divs))

    for q in tqdm(range(0, limit+1)):
        if q not in D:
            D.setdefault(q+q, set()).add(q)
        else:
            if q%4 == 2:
                first_half = sorted(D[q])

                if divisors_thing(first_half[0:1+len(first_half)//2], q):
                    # print(q)
                    count += q
            # print("SOMETHING", something)

            for p in D[q]:
                D.setdefault(p+q, set()).add(p)
            D.setdefault(q+q, set()).add(q)
            del D[q]

    return count


for i in range(2, 10):
    print(thingy(10**i))
