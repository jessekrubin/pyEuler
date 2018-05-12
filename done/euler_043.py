#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Sub-string divisibility
Problem 43
The number, 1406357289, is a 0 to 9 pandigital number because it is made up
of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from lib.listless import digits_to_int
from itertools import permutations


def pandigital_substring_thing(pandigit_list):
    if pandigit_list[0] == 0:
        return False  # leading 0 shouldnt count
    else:
        div_primes = [2, 3, 5, 7, 11, 13, 17]
        for i in range(1, 8):
            if digits_to_int(pandigit_list[i:i+3]) % div_primes[i-1] != 0:
                return False
    return True


def p043():
    # well_they_gave_us_this_one = [1,4,0,6,3,5,7,2,8,9]
    # test_answer = pandigital_substring_thing(well_they_gave_us_this_one)
    # print(test_answer)
    circle_to_nine = [i for i in range(0, 10)]  # circle is the way kids say 0 now a days
    pandigit_lists = [digits_to_int(i) for i in permutations(circle_to_nine) if pandigital_substring_thing(i)]
    return sum(pandigit_lists)


if __name__ == '__main__':
    ans = p043()
    print("Sum of products: {}".format(ans))