#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Numbers for which no 3 consecutive digits have a sum greater than a given value
Problem 164
How many 20 digit numbers n (without any leading zero) exist such that no three
consecutive digits of n have a sum greater than 9?
"""

from functools import lru_cache


# recursive solution
@lru_cache(maxsize=None)
def num_nums(first, second, remaining_digits):
    if remaining_digits == 0:
        return 1
    else:
        ret_val = 0
        for i in range(10 - (first + second)):
            ret_val += num_nums(second, i, remaining_digits - 1)
        return ret_val


one_two_nine_answer = 0
for i in range(1, 10, 1):
    one_two_nine_answer += num_nums(0, i, 19)

print("ANSWER: {}".format(one_two_nine_answer))
