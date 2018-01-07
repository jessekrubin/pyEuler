# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
# JESSES pEuler helper functions

from math import sqrt
from collections import deque
from functools import lru_cache


@lru_cache(maxsize=None)
def is_prime(n):
    """returns True if n is prime

    >>> is_prime(10)
    False
    >>> is_prime(17)
    True
    """

    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))


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


def divisors_gen(n):
    large_divisors = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor


def n_divisors(n):
    return sum((1 for i in divisors_gen(n)))


def divisors_list(n):
    return [i for i in divisors_gen(n)]


def number_rotations_generator(l):
    for i in range(len(l)):
        yield (l[-i:] + l[:-i])


def is_palindrome(s):
    """Returns True a string is a palindrome.

    Doctests:
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("greg")
    False
    """

    for i, c in enumerate(s):
        if c != s[-i - 1]:
            return False
    return True


def int_2_binary_string(n):
    return bin(n)[2:]


def rotate_list(l, n):
    return l[-n:] + l[:-n]


def num_base_ten_digits(n):
    digs = sum((1 for i in str(n)))
    return digs


def digits_list(num):
    digits = deque()
    while True:
        num, r = divmod(num, 10)
        digits.appendleft(r)
        if num == 0:
            break
    return list(digits)


def cross_prod(toop1, toop2):
    return ((toop1[0] * toop2[1]) - (toop1[1] * toop2[0]))


def dig_list_2_int(l):
    d = 0
    for i in range(len(l), 0, -1):
        d += (l[i] * 10 ** i)
    return d


def string_score(name):
    return sum((ord(character) - 96 for character in name.lower()))
