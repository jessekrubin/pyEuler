#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler


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


def int_to_binary_string(n):
    return bin(n)[2:]


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
