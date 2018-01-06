# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
# JESSES pEuler helper functions

from math import sqrt, log
import math
from functools import lru_cache


@lru_cache(maxsize=None)
def is_prime(n):
    """returns True if n is prime

    >>> is_prime(10)
    False
    >>> is_prime(17)
    True
    """
    import math

    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

@lru_cache(maxsize=None)
def is_circ_prime(n):
    digist = [int(j) for j in digits_list(n)]
    return all(
        (is_prime(dig_list_2_int(i)) for i in number_rotations_generator(digist)))


def number_rotations_generator(l):
    for i in range(len(l)):
        yield (l[-i:] + l[:-i])


def rotate_list(l, n):
    return l[-n:] + l[:-n]



def num_base_ten_digits(n):
    digs = sum((1 for i in str(n)))
    return digs


def digits_list(number):
    return [(number // (10 ** i)) % 10 for i in range(math.ceil(math.log(number, 10)) - 1, -1, -1)]


def test_digits_list():
    assert digits_list(123) == [1, 2, 3]

def dig_list_2_int(l):
    l.reverse()
    d = 0
    for i in range(len(l)):
        d += (l[i] * 10 ** i)
    return d