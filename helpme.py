#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler

import math
import functools


def is_pan_digit(n):
    nset = set(digitsList(n))
    return(nset == set([(i + 1) for i in range(b10length(n))]))


def b10_num_length(n):
    l = 0
    cur = n
    while(cur > 0):
        l += 1
        cur = cur // 10
    return l


def digits_list(n):
    """
    Returns a list of the base-10 digits in a number
    """

    digits = []
    cur = n
    while(cur > 10):
        digits.append(cur % 10)
        cur = cur // 10
    digits.append(cur)
    return digits


def factors_list(x):
    """returns a list of factors

    >>> factors_list(12)
    [1, 2, 3, 4, 6, 12]
    >>> factors_list(20)
    [1, 2, 4, 5, 10, 20]
    """

    leeest = []
    for i in range(1, int(x / 2) + 1):
        if x % i == 0:
            leeest.append(i)
    leeest.append(x)
    return leeest


def divisors_list(x):
    """divisors_list(n) returns list of divisors of n(umber)

    >>> divisors_list(12)
    [1, 2, 3, 4, 6, 12]
    """
    return [i for i in divisors_gen(x)]


def num_divisors(x):
    n = 0
    for i in range(int((1 + x) / 2), 0, -1):
        # print(i)
        if x % i == 0:
            n += 1
    return n


def proper_divisors_gen(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        if divisor != n:
            yield divisor


def divisors_gen(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor


@functools.lru_cache(maxsize=None)
def is_prime(n):
    """is_prime(n) returns True if n is prime

    Doctests:
    >>> is_prime(10)
    False
    >>> is_prime(17)
    True
    """
    import math

    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


@functools.lru_cache(maxsize=None)
def str_is_pal(s):
    """Returns True if string is a palindrome.

    Doctests:
    >>> str_is_pal("racecar")
    True
    >>> str_is_pal("greg")
    False
    """

    for i, c in enumerate(s):
        if c != s[-i - 1]:
            return False
    return True


@functools.lru_cache(maxsize=None)
def int_2_binary_str(n):
    """
    Converts an integer to a string version of binary

    Doctests:
    >>> int_2_binary_str(1)
    '1'
    >>> int_2_binary_str(2)
    '10'
    >>> int_2_binary_str(9)
    '1001'
    """
    return str(bin(n)[2:])


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
