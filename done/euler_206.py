#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse and Graham Rubin
"""
Concealed Square
Problem 206 
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""

from lib.listless import digits_list


def is_1_2_3_4_5_6_7_8_9_0(n):
    # """
    # >>> is_1_2_3_4_5_6_7_8_9_0(1122334455667788990)
    # True
    # >>> is_1_2_3_4_5_6_7_8_9_0(1121314151617181910)
    # True
    # >>> is_1_2_3_4_5_6_7_8_9_0(11122334455667788990)
    # False
    # >>> is_1_2_3_4_5_6_7_8_9_0(1112214455667788990)
    # False
    # """
    digs = digits_list(n)
    if len(digs) != 19:
        return False
    the_digs = [digs[index] for index in range(0, 19, 2)]
    for i in range(10):
        if i == 9 and the_digs[9] == 0:
            return True
        if i + 1 != the_digs[i]:
            return False
    return True


# upper_bound = 1020304050607080900
# lower_bound = 1929394959697989990
# print(math.sqrt(upper_bound))
# print(math.sqrt(lower_bound))


def p206():
    for i in range(1389026620, 1010101010, -10):
        if is_1_2_3_4_5_6_7_8_9_0(i ** 2):
            return i

if __name__=='__main__':
    answer = p206()
    print('{} squared is {} -- a concealed square'.format(answer, answer**2))
