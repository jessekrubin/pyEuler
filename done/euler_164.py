#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Numbers for which no 3 consecutive digits have a sum greater than a given value
Problem 164

How many 20 digit numbers n (without any leading zero) exist such that no three
consecutive digits of n have a sum greater than 9?
"""

from biblioteca import cash_it


@cash_it
def num_nums(first, second, remaining_digits):
    if remaining_digits == 0:
        return 1
    ret_val = 0
    for i in range(10 - (first + second)):
        ret_val += num_nums(second, i, remaining_digits - 1)
    return ret_val


def p164():
    count = 0
    # for nums 'starting' w/ i (1,2,...,9) find the answer and add to count
    for i in range(1, 10, 1):
        # each will have 19 remaining digits
        # 0 is fubbed in as the first
        count += num_nums(0, i, 19)
    return count


if __name__ == '__main__':
    count = p164()
    print("ANSWER: {}".format(count))