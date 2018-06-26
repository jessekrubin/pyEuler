#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - Biblioteca
from functools import reduce
from operator import mul
from collections import Counter, deque
from bib import xrange


def chunks(list, chunk_size):
    """Yields chunks of a list with length == chunk_size

    Args:
        list (list or tuple): list to be broken up
        chunk_size (int): size of the chunks

    Yields:
        (list): chunk with length == chunk_size from list

    Examples:
        >>> list(chunks([1, 2, 3, 4, 5, 6], 3))
        [[1, 2, 3], [4, 5, 6]]
        >>> list(chunks([1, 2, 3, 4, 5, 6], 2))
        [[1, 2], [3, 4], [5, 6]]
    """
    for i in xrange(0, len(list), chunk_size): yield list[i:i+chunk_size]


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


def rotate(rlist, rn=1, left_rotate=True):
    """Rotate a list (rlist) by rn indices to the left or right

    Args:
        rlist (list or tuple): list/toople or slicable to be rotated
        rn (int): steps bywhich to rotate
        left_rotate (bool): True (default) left rotates; False right rotates.

    Returns:
        (list): rotated list

    Examples:
        >>> rotate([1, 2, 3, 4], left_rotate=True)
        [2, 3, 4, 1]
        >>> rotate([1, 2, 3, 4], left_rotate=False)
        [4, 1, 2, 3]
        >>> rotate([1, 2, 3, 4], rn=4, left_rotate=False)
        [1, 2, 3, 4]

    """

    def _left_rotate(l, n=1):
        return l[n:]+l[:n]

    def _right_rotate(l, n=1):
        return l[-n:]+l[:-n]

    return _left_rotate(rlist, rn) if left_rotate else _right_rotate(rlist, rn)


def rotations_gen(rlist):
    """Yields all rotations of a list

    Args:
        rlist:
    """
    for i in xrange(len(rlist)):
        yield (rlist[-i:]+rlist[:-i])


def digits_list(number):
    """Returns a list of the digits in num

    Args:
        number (int): number w/ digits to be listsed

    Returns:
        (list): digits in a list

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
    for _ in xrange(len(str(number))):
        number, r = divmod(number, 10)
        digits.appendleft(r)
    return list(digits)


def int_from_digits(dlist):
    """Convert digits list or tuple to integer

    Args:
        dlist (list or tuple): digits to be converted

    Returns:
        (int): number

    Examples:
        >>> int_from_digits([3, 2, 1])
        321
        >>> int_from_digits([1, 1, 1, 1, 2, 3])
        111123
        >>> int_from_digits([1, 2, 3])
        123
    """
    return sum(dlist[len(dlist)-i-1]*10**i for i in xrange(0, len(dlist), 1))


def iter_product(l):
    """Product of all the elements in a list or tuple

    Args:
        l: list with integer elements

    Returns:
        int: product of all the elements in a list

    Examples:
        >>> iter_product([1, 2, 3, 4])
        24
        >>> iter_product(tuple([1, 2, 3, 4]))
        24
        >>> iter_product([-1, -2, -3, 4])
        -24

    """
    return reduce(mul, l)
