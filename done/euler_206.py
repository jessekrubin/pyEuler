#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse and Graham Rubin
"""
Concealed Square
Problem 206 
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""
__sol__ = None

from lib.listless import digits_list
from math import sqrt

def is_1_2_3_4_5_6_7_8_9_0(n):
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

def p206():
    range_max = int(sqrt(1020304050607080900))
    range_min = int(sqrt(1929394959697989990))
    range_min -= (range_min%10)
    for i in range(range_min, range_max, -10):
        if is_1_2_3_4_5_6_7_8_9_0(i ** 2):
            return i

if __name__=='__main__':
    assert True == is_1_2_3_4_5_6_7_8_9_0(1122334455667788990)
    assert True == is_1_2_3_4_5_6_7_8_9_0(1121314151617181910)
    assert False == is_1_2_3_4_5_6_7_8_9_0(11122334455667788990)
    assert False == is_1_2_3_4_5_6_7_8_9_0(1112214455667788990)
    answer = p206()
    print('{}^2 is {}'.format(answer, answer**2))