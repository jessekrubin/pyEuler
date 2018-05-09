#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse + Graham Rubin
"""
Pandigital multiples
Problem 38 
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product 
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

from itertools import permutations, count


def make_number(l):
    return int(''.join(l))


def p038():
    lists_of_multipliers = [[j for j in range(1, i)] for i in range(3, 11)]
    one_to_nine = ['9', '8', '7', '6', '5', '4', '3', '2', '1']
    list_of_perms = set(make_number(perm) for perm in permutations(one_to_nine))
    max_pan_digit = max(list_of_perms)

    def check_num(n):
        for multipliers in lists_of_multipliers:
            num = int(''.join([str(i*n) for i in multipliers]))
            if num in list_of_perms:
                return True
            if num > max_pan_digit:
                return False
        return False

    starting_n = max(i for i in range(10000) if check_num(i))
    remaining_digs = 9
    products = []
    for n in count(1):
        products.append(starting_n*n)
        remaining_digs -= len(str(starting_n*n))
        if remaining_digs == 0:
            return int("".join([str(num) for num in products]))


if __name__ == '__main__':
    ANSWER = p038()
    print("ANSWER: {}".format(ANSWER))
