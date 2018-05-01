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
__sol__ = 932718654

from itertools import permutations



def make_number(l):
    return int(''.join(l))


lists_of_multipliers = [[j for j in range(1, i)] for i in range(3, 11)]
one_to_nine = ['9', '8', '7', '6', '5', '4', '3', '2', '1']
list_of_perms = set([make_number(perm) for perm in permutations(one_to_nine)])
max_pan_digit = max(list_of_perms)


def check_num(n):
    for multipliers in lists_of_multipliers:
        num = int(''.join([str(i * n) for i in multipliers]))
        if num in list_of_perms:
            return True
        if num > max_pan_digit:
            return False
    return False


# test_check = check_num(192)
# print(test_check)

# print(make_number(one_to_nine))
# print(list_of_perms)
# print(len(list_of_perms))

print("greatest pandigit thingy formed with: {}".format(max([i for i in range(10000) if check_num(i)])))

# returns
# 1
# 9
# 192
# 219
# 273
# 327
# 6729
# 6792
# 6927
# 7269
# 7293
# 7329
# 7692
# 7923
# 7932
# 9267
# 9273
# 9327
def p038():
    pass

if __name__ == '__main__':
    p038()