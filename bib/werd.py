#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - Biblioteca
"""
String Methods
"""


def binary_string(number):
    """Number to binary string"""
    return bin(number)[2:]


def string_score(strang):
    """Sum of letter values where a==1 and z == 26

    Args:
        strang (str): string to be scored

    Returns:
        (int): score of the string

    Examples:
        >>> string_score('me')
        18
        >>> string_score('poooood')
        95
        >>> string_score('gregory')
        95
    """
    return sum((ord(character)-96 for character in strang.lower()))


def is_palindrome(strang):
    """True a string is a palindrome; False if string is not a palindrome.

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("greg")
        False
    """
    for index, character in enumerate(strang):
        if character != strang[-index-1]: return False
    return True
