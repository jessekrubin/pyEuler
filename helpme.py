# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
# JESSE'S pEuler helper functions

from math import sqrt
from collections import deque
from functools import lru_cache


@lru_cache(maxsize=None)
def is_prime(number: int) -> bool:
    """
    True if number is prime

    >>> is_prime(37)
    True
    >>> is_prime(100)
    False
    >>> is_prime(89)
    True
    >>> is_prime(10)
    False
    >>> is_prime(17)
    True
    """
    if number % 2 == 0 and number > 2:
        return False
    else:
        return all(number % i for i in range(3, int(sqrt(number) + 1), 2))


def prime_factorization(n):
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


@lru_cache(maxsize=None)
def is_perfect_square(positive_n):
    if positive_n < 5:
        if positive_n == 4 or positive_n == 1:
            return True
        return False
    half = positive_n // 2
    seen_set = {half}
    while half * half != positive_n:
        half = (half + (positive_n // half)) // 2
        if half in seen_set:
            return False
        seen_set.add(half)
    return True


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    """Return the nth fibonacci number

    :param n: fib_gen number index
    :return: nth fib_gen number
    >>> fib_gen(1)
    1
    >>> fib_gen(2)
    2
    >>> fib_gen(3)
    3
    >>> fib_gen(4)
    5
    >>> fib_gen(5)
    8
    >>> fib_gen(6)
    13
    """
    if n < 3:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


@lru_cache(maxsize=None)
def is_circ_prime(n):
    digist = [int(j) for j in digits_list(n)]
    return all(
        (is_prime(dig_list_2_int(i)) for i in number_rotations_generator(digist)))


@lru_cache(maxsize=4)
def divisors_gen(n):
    large_divisors = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor


@lru_cache(maxsize=None)
def n_divisors(n):
    """
    >>> n_divisors(12)
    6
    >>> n_divisors(10)
    4
    """
    return sum(1 for _ in divisors_gen(n))


def divisors_list(n):
    return [i for i in divisors_gen(n)]


def number_rotations_generator(l):
    for i in range(len(l)):
        yield (l[-i:] + l[:-i])


def is_palindrome(string):
    """True a string is a palindrome.

    Doctests:
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("greg")
    False
    """
    for index, character in enumerate(string):
        if character != string[-index - 1]:
            return False
    return True


def int_2_binary_string(n):
    return bin(n)[2:]


def rotate_list(l, n):
    return l[-n:] + l[:-n]


def num_base_ten_digits(number: int) -> int:
    return sum((1 for _ in str(number)))


def digits_list(num):
    """
    >>> digits_list(1111)
    [1, 1, 1, 1]
    >>> digits_list(982)
    [9, 8, 2]
    >>> digits_list(101)
    [1, 0, 1]
    >>> digits_list(123)
    [1, 2, 3]
    """

    digits = deque()
    while True:
        num, r = divmod(num, 10)
        digits.appendleft(r)
        if num == 0:
            break
    return list(digits)


def cross_prod(toop1, toop2):
    return (toop1[0] * toop2[1]) - (toop1[1] * toop2[0])


def dig_list_2_int(l):
    """
    >>> dig_list_2_int([3, 2, 1])
    321
    >>> dig_list_2_int([1, 1, 1, 1, 2, 3])
    111123
    >>> dig_list_2_int([1, 2, 3])
    123
    """
    d = 0
    n_digs = len(l)
    for i in range(0, n_digs, 1):
        d += (l[n_digs - i - 1] * 10 ** i)
    return d


def string_score(name):
    """
    >>> string_score('me')
    18
    >>> string_score('poooood')
    95
    >>> string_score('gregory')
    95
    """
    return sum((ord(character) - 96 for character in name.lower()))


if __name__ == '__main__':
    import doctest

    doctest.testmod()  # run doctests if this script is called
