#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - Biblioteca
"""
String Methods
"""


def binary_string(number):
    """Number to binary string"""
    return bin(number)[2:]


def string_score(name):
    """Sum of letter values

    Args:
        name:

    Returns:

    Examples:
        >>> string_score('me')
        18
        >>> string_score('poooood')
        95
        >>> string_score('gregory')
        95
    """
    return sum((ord(character)-96 for character in name.lower()))


def is_palindrome(string):
    """True a string is a palindrome.

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("greg")
        False
    """
    for index, character in enumerate(string):
        if character != string[-index-1]:
            return False
    return True
