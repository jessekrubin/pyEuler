#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler
from functools import lru_cache
from math import sqrt
from lib.decorations import json_cash
from os import path, getcwd, pardir

@json_cash(path.join(path.abspath(path.join(getcwd(), pardir)), 'files_n_stuff', 'primes.json'))
def prime_sieve_gen(upper_bound, D=None):
    if D is None:
        D = {}
    else:
        D = D
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
        if upper_bound is not None and upper_bound < q:
            break


@lru_cache(maxsize=None)
def is_prime(number: int) -> bool:
    """
    Returns True if number is prime

    >>> is_prime(37)
    True
    >>> is_prime(100)
    False
    >>> is_prime(89)
    True
    """
    if number % 2 == 0 and number > 2:
        return False
    else:
        return all(number % i for i in range(3, int(sqrt(number) + 1), 2))


def prime_factorization(n):
    """
    Returns prime factorization as a list

    :param n:
    :return:
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
