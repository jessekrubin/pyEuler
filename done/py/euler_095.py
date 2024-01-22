#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Problem 95: Amicable chains
The proper divisors of a number are all the divisors excluding the number
itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the
sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the
proper divisors of 284 is 220, forming a chain of two numbers. For this reason,
220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we
form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element
exceeding one million.
"""

from functools import lru_cache
from pupy.decorations import cprof
from pupy.maths import divisors_gen
from pupy.amazon import prime_gen

upperlim = 1000000
primes = {p for p in prime_gen(upperlim)}
chainlengths = {}
perfects = set()
mean_numbers = set()


@lru_cache(maxsize=None)
def proper_divisors_gen(n):
    return sum(number for number in divisors_gen(n) if number < n)


@lru_cache(maxsize=None)
def is_perfect(n):
    return n == proper_divisors_gen(n)


@lru_cache(maxsize=None)
def chaingang(start_n):
    the_chain = []
    cur = start_n
    while cur not in the_chain and cur > 1:
        the_chain.append(cur)
        if cur in primes or cur > 1000000 or cur in mean_numbers:
            break
        cur = proper_divisors_gen(cur)

    if proper_divisors_gen(the_chain[-1]) == start_n:
        clen = len(the_chain)
        for n in the_chain:
            chainlengths[n] = clen
    else:
        mean_numbers.add(start_n)


def p095():
    # for i in tqdm(range(2, 1000000), ascii=True, desc="p095"):
    for i in range(2, 1000000):
        if i not in chainlengths:
            chaingang(i)

    max_chainlength = max(v for v in chainlengths.values())
    return min(k for k, v in chainlengths.items() if v == max_chainlength)


if __name__ == "__main__":
    ANSWER = p095()
    print("smallest member of the longest amicable chain: {}".format(ANSWER))
