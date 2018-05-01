#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Prime square remainders
Problem 123
Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when
(pn−1)n + (pn+1)n is divided by pn2.

For example, when n = 3, p3 = 5, and 43 + 63 = 280 ≡ 5 mod 25.

The least value of n for which the remainder first exceeds 109 is 7037.

Find the least value of n for which the remainder first exceeds 1010.
"""
__sol__ = None


from lib.octopus_prime import prime_sieve_gen
from lib.decorations import tictoc

@tictoc()
def psr(remainder_max):
    for n, p in enumerate(prime_sieve_gen()):
        rem = 2*(n+2)*p
        if rem > remainder_max:
            return n

print((psr(1000000000)))
print((psr(10000000000)))



def p123():
    pass

if __name__ == '__main__':
    ANSWER = p123()
    print("Answer: {}".format(ANSWER))