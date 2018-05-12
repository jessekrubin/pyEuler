# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Prime permutations
Problem 49
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

from lib.listless import digits_list
from lib.amazon_prime import is_prime
from itertools import combinations
from collections import defaultdict


def p049():
    four_dig_primes = [i for i in range(1000, 10000) if is_prime(i)]
    num_4dig_primes = len(four_dig_primes)

    prime_perms = defaultdict(list)
    for prime in four_dig_primes:
        sorted_digs = tuple(sorted(digits_list(prime)))
        prime_perms[sorted_digs].append(prime)

    topop = [k for k, v in prime_perms.items() if len(v) < 3]
    for toop in topop:
        prime_perms.pop(toop)

    validsets = []
    for k, v in prime_perms.items():
        for combo in combinations(v, 3):
            if combo[1] - combo[0] == combo[2] - combo[1]:
                validsets.append(combo)

    return int("".join(str(n) for n in validsets[1]))


if __name__ == '__main__':
    ANSWER = p049()
    print("The set of primes is: {}".format(ANSWER))