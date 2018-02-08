# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Double-base palindromes
Problem 36
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

from helpme import is_palindrome, int_to_binary_string

multiple_liner = 0
for i in range(1000000):
    # Check if both as strings are palindromes
    if (is_palindrome(str(i))) and is_palindrome((int_to_binary_string(i))):
        multiple_liner += i

one_liner = sum([i for i in range(1000000) if (is_palindrome(str(i))) and is_palindrome((int_to_binary_string(i)))])

print("One liner(!): {}".format(one_liner))
