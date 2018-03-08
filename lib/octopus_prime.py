#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler
from lib.decorations import json_cash
from os import path, getcwd, pardir
from json import load, dump

def primes_below(upperbound):
    return list(n for n in prime_sieve_gen(upperbound))


def prime_sieve_gen(upper_bound=None, save_path=None):
    if save_path is None:
        save_path = path.abspath(path.join(getcwd(), pardir, 'files_n_stuff', 'prime_sieve_cache.json'))
    try:
        with open(save_path, 'r', encoding='utf-8') as f:
            D = load(f)
    except IOError:
        D = {}

    q = 2
    while True:
        # print(D)
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

    with open(save_path, 'w', encoding='utf-8') as f: dump(D, f, indent=2)

# @lru_cache(maxsize=None)
@json_cash(path.join(path.abspath(path.join(getcwd())), 'files_n_stuff'))
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
    if number == 2 or number == 3:
        return True
    if number < 2 or number % 2 == 0:
        return False
    if number < 9:
        return True
    if number % 3 == 0:
        return False
    r = int(number ** 0.5)
    step = 5
    while step <= r:
        if number % step == 0:
            return False
        if number % (step + 2) == 0:
            return False
        step += 6
    return True


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
