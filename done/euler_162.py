#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Problem Name
prob #

Prompt
"""

from itertools import count
from bib.decorations import cash_it
from collections import Counter

hex = ['0', '1', '2', '3', '4', '5', '6', '7',
       '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


# def hexadecimal_01A(remaining, cur, has_0, has_1, has_a):
#     if remaining == 0:
#         if has_0 and has_1 and has_a:
#             # print(cur)
#             return 1
#         else:
#             return 0
#
#     total = 0
#     for hex_digit in hex:
#         total += hexadecimal_01A(remaining-1, cur+hex_digit,
#                                  True if hex_digit == '0' else has_0,
#                                  True if hex_digit == '1' else has_1,
#                                  True if hex_digit == 'A' else has_a)
#     return total

@cash_it
def hexadecimal_01A(remaining, has_0, has_1, has_a):
    if remaining == 0:
        if has_0 and has_1 and has_a:
            # print(cur)
            return 1
        else:
            return 0

    total = 0
    for hex_digit in hex:
        total += hexadecimal_01A(remaining-1,
                                 True if hex_digit == '0' else has_0,
                                 True if hex_digit == '1' else has_1,
                                 True if hex_digit == 'A' else has_a)
    return total

def p162(n_dijits=16):
    total = 0
    for n_digits in range(3, n_dijits+1):
        for starting_dig in hex[1:]:
            total += hexadecimal_01A(n_digits-1,
                            True if starting_dig == '0' else False,
                            True if starting_dig == '1' else False,
                            True if starting_dig == 'A' else False)
    return '{:02x}'.format(total).upper()

# def p000():
#     pass
#
#
if __name__ == '__main__':
    assert p162(5) == '27CE'
    ANSWER = p162()
    print("# hexadecimal numbers w/ 1, 0 and A: {}".format(ANSWER))


