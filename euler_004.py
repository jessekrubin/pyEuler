#!/usr/bin/env python
# -*- coding: utf-8 -*-
<<<<<<< HEAD
# JESSE AND SOPHIE
"""
Largest palindrome product
Problem 4 

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.
=======
# phil and samantha and jesse

"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.
>>>>>>> 44fe9893c4ecb44e1ee58d9d6dfc13d5786055f7

Find the largest palindrome made from the product of two 3-digit numbers.
"""

<<<<<<< HEAD
for i in range(1, 1000):
    for j in range(1, 1000):
        print(i)
        print(j)
        print(i * j)
=======
def str_is_pal(s):
    """Returns True if string is a palindrome.

    Doctests:
    >>> str_is_pal("racecar")
    True
    >>> str_is_pal("greg")
    False
    """

    for i, c in enumerate(s):
        if c != s[-i - 1]:
            return False
    return True

answer = max(map(int, filter(str_is_pal, [str(i * j) for i in range(100, 1000) for j in range(100, 1000)])))
print("Answer: {}".format(answer))
>>>>>>> 44fe9893c4ecb44e1ee58d9d6dfc13d5786055f7
