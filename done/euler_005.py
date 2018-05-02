#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN -- project Euler
"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""
__sol__ = 232792560


def p005():
    good_divs = [20, 19, 18, 17, 16, 14, 13, 11]

    ret_val = 20
    while True:
        if all(ret_val%n == 0 for n in good_divs):
            break
        ret_val += 20
    return ret_val


if __name__ == '__main__':
    answer = p005()
    print("Answer: {}".format(answer))
