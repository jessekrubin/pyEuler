#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler
from collections import deque, Counter
from operator import mul
from sys import version_info
if version_info.major > 2:
    xrange = range

def list_product(l):
    return reduce(mul, l)


def is_permutation(a, b):
    """
    Checks if ints / lists are permutations

    :param a: int or list
    :param b: int or list
    :return: bool; True if a an b are permutations
    """
    if type(a)==int:
        a=digits_list(a)
    if type(b)==int:
        b=digits_list(b)
    return len(a)==len(b) and Counter(a)==Counter(b)


def rotate_list(l, n=1):
    return l[-n:]+l[:-n]


def rot_list_gen(l):
    for i in range(len(l)):
        yield (l[-i:]+l[:-i])


def digits_list(num):
    """
    Returns a list of the digits in a number

    :param num:
    :return:

    >>> digits_list(1111)
    [1, 1, 1, 1]
    >>> digits_list(982)
    [9, 8, 2]
    >>> digits_list(101)
    [1, 0, 1]
    >>> digits_list(123)
    [1, 2, 3]
    """
    digits=deque()
    while True:
        num, r=divmod(num, 10)
        digits.appendleft(r)
        if num==0:
            break
    return list(digits)


def dig_list_2_int(l):
    """
    >>> dig_list_2_int([3, 2, 1])
    321
    >>> dig_list_2_int([1, 1, 1, 1, 2, 3])
    111123
    >>> dig_list_2_int([1, 2, 3])
    123
    """
    d=0
    n_digs=len(l)
    for i in range(0, n_digs, 1):
        d+=(l[n_digs-i-1]*10**i)
    return d
