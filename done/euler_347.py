#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Largest integer divisible by two primes
Problem 347
The largest integer ≤ 100 that is only divisible by both the primes 2 and 3 is
96, as 96=32*3=25*3. For two distinct primes p and q let M(p,q,N) be the
largest positive integer ≤N only divisible by both p and q and M(p,q,N)=0 if
such a positive integer does not exist.

E.g. M(2,3,100)=96.
M(3,5,100)=75 and not 90 because 90 is divisible by 2 ,3 and 5.

Also M(2,73,100)=0 because there does not exist a positive integer ≤ 100 that
is divisible by both 2 and 73.

Let S(N) be the sum of all distinct M(p,q,N). S(100)=2262.

Find S(10,000,000).
"""
__sol__ = 11109800204052

from math import log
from lib.octopus_prime import prime_gen
from bisect import bisect_right


def m(p, q, N):
    max_int_div = 0
    max_p_exp = int(log(N // q) / log(p)) + 2
    q_log = log(q)
    for p_exp in range(1, max_p_exp):
        max_q_exp = int(log(N // p ** p_exp) / q_log) + 2
        for q_exp in range(1, max_q_exp):
            num = (p ** p_exp) * (q ** q_exp)
            if N >= num > max_int_div:
                max_int_div = num
    return max_int_div


def s(n):
    primes = []
    prime_sieve_limit = int(n // 2) + 1  # plus two cause idk
    ret_sum = 0
    for p in prime_gen(prime_sieve_limit):
        mul_list = primes[0:bisect_right(primes, n // p)]
        ret_sum += sum(m(ppp, p, n) for ppp in mul_list)
        primes.append(p)
    return ret_sum


def p347(n=10 ** 7):
    return s(n)


if __name__ == '__main__':
    # m(pytriple_gen, q, N) test
    assert 96 == m(2, 3, 100)
    assert 75 == m(3, 5, 100)
    assert 0 == m(2, 73, 100)

    # s(n) test
    assert 2262 == s(100)

    # answer
    ANSWER = p347()
    print("Solution: {}".format(ANSWER))
