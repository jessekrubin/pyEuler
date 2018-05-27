# -*- coding: utf-8 -*-
# JESSE RUBIN - project euler
"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from bib.werd import is_palindrome


def largest_palidrome_product(n_digit_numbers):
    lower_bound = 10**(n_digit_numbers-1)
    upper_bound = lower_bound*10
    return max(map(int, filter(is_palindrome, (str(int(i*j))
                                               for i in range(lower_bound, upper_bound)
                                               for j in range(i, upper_bound)))))


def p004():
    return largest_palidrome_product(3)



if __name__ == '__main__':
    assert 9009 == largest_palidrome_product(2)
    answer = p004()
    print("max paindrome: {}".format(answer))
