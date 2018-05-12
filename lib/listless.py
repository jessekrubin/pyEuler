#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - Biblioteca
from functools import reduce
from operator import mul

from collections.__init__ import Counter, deque

from lib import xrange


def chunks(l, n):
    """

    Args:
        l:
        n:
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


def is_permutation(a, b):
    """
    Checks if two integers or lists are permutations lists are permutations

    Args:
        a (int or list): possible perumtation of b
        b (int or list): possible perumtation of a

    Returns:
        bool: True if a and b are permutations of one another; False otherwise

    """

    if type(a) == int:
        a = digits_list(a)
    if type(b) == int:
        b = digits_list(b)
    return len(a) == len(b) and Counter(a) == Counter(b)


def rotate_list(l, n=1):
    """

    Args:
        l:
        n:

    Returns:

    """
    return l[-n:]+l[:-n]


def list_rotation_gen(l):
    """Yields rotations of a list

    Args:
        l:
    """
    for i in xrange(len(l)):
        yield (l[-i:]+l[:-i])


def digits_list(num):
    """Returns a list of the digits in num

    Args:
        num (int): number w/ digits to be listsed

    Returns:
        list of digits

    Examples:
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
    for _ in xrange(len(str(num))):
        num, r = divmod(num, 10)
        digits.appendleft(r)
    return list(digits)


def digits_to_int(l):
    """
    >>> digits_to_int([3, 2, 1])
    321
    >>> digits_to_int([1, 1, 1, 1, 2, 3])
    111123
    >>> digits_to_int([1, 2, 3])
    123
    """
    return sum(l[len(l)-i-1]*10**i for i in xrange(0, len(l), 1))


def list_product(l):
    """Product of all the elements in a list

    Args:
        l: list with integer elements

    Returns:
        int: product of all the elements in a list

    Examples:
        >>> list_product([1, 2, 3, 4])
        24
        >>> list_product([-1, -2, -3, 4])
        -24

    """
    return reduce(mul, l)