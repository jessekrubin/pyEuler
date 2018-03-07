#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler
from functools import lru_cache
from math import sqrt

def prime_sieve_gen(upper_bound):
    """
    Generates primes below the parameter, upper_bound.

    :param upper_bound:
    :return:
    """
    prime_mask = [False] + [True] * (upper_bound - 1)
    num_i = 2
    while num_i**2 <= upper_bound:
        yield num_i
        for n_below in range(2 * num_i, upper_bound + 1, num_i): prime_mask[n_below - 1] = False
        while prime_mask[num_i] is False and num_i**2 < upper_bound: num_i += 1
        num_i += 1
    yield from (j + 1 for j in range(num_i, upper_bound) if prime_mask[j])

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
