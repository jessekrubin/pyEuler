#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse and Graham Rubin
"""
Large non-Mersenne prime
Problem 97

The first known prime found to exceed one million digits was discovered in
1999, and is a Mersenne prime of the form 26972593−1; it contains exactly
2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have
been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains
2,357,207 digits:

28433×((2**7830457)+1).

Find the last ten digits of this prime number.
"""


def p097():
    return pow(2, 7830457, 10**10) * 28433 % (10**10) + 1


if __name__ == "__main__":
    answer = p097()
    print("Last ten digits: {}".format(answer))
