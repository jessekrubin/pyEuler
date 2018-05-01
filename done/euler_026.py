# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Reciprocal cycles
Problem 26
A unit fraction contains 1 in the numerator. The decimal representation of
the unit ordered_fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part.
"""
__sol__ = 983

from lib.octopus_prime import is_prime


def num_cycles(p):
    # cycle has to be smaller than prime number
    # so for all nums less than,
    # if the the remainder of the 10 to the power of that number  is one
    # that's the cycle length
    for i in range(1, p):
        hopefully_one_maybe = 10 ** i % p
        if hopefully_one_maybe == 1:
            return i
    return -1


def p026():
    primes_lt1000 = [i for i in range(1, 1000) if is_prime(i)]
    cycles = [num_cycles(p) for p in primes_lt1000]
    return primes_lt1000[cycles.index(max(cycles))]


if __name__ == '__main__':
    ANSWER = p026()
    print("D w/ longest cycles: {}".format(ANSWER))
