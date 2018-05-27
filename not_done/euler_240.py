#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Problem Name
prob #

Prompt
"""

from itertools import *
from heapq import nlargest
from bib.decorations import cash_it

@cash_it
def recurse_top_dice(target_sum, remaining, n_sides, n_top_dice, dice):
    # SET UP INCASE NO INIT

    print(dice)
    if remaining == 0:
        if sum(dice) == target_sum:
            # print("PLUS")
            return 1
        else:
            # print(dice, "zilch")
            # print("no")
            return 0
    # if len(dice)==n_top_dice and max(dice)==7 and min(dice)<7:
    #     return 0
        # pass
    else:
        t = 0
        for i in range(1, n_sides+1):
            a = nlargest(n_top_dice, dice+(i, ))
            if sum(a)<=target_sum:
                t += recurse_top_dice(target_sum, remaining-1, n_sides, n_top_dice, tuple(a))
        return t
#
# @cash_it
# def recurse_top_dice(target_sum, remaining, n_sides, n_top_dice, dice):
#     # SET UP INCASE NO INIT
#
#     if remaining == 0:
#         # if sum(dice) == target_sum:
#         if sum(dice)== target_sum:
#             print(dice)
#             return 1
#         else:
#             return 0
#     else:
#         t = 0
#         for i in range(1, n_sides+1):
#             a = sorted(nlargest(n_top_dice, dice+(i, )))
#             t += recurse_top_dice(target_sum, remaining-1, n_sides, n_top_dice, tuple(a))
#         return t

#
# @cash_it
# def recurse_top_dice(target_sum, total_dice, remaining, n_sides, n_top_dice, botop, top_sum):
#     # SET UP INCASE NO INIT
#
#     if remaining == 0:
#         # if sum(dice) == target_sum:
#         # print(top_sum)
#         if top_sum == target_sum:
#             print(botop)
#             return 1
#         return 0
#     else:
#         t = 0
#         for i in range(1, n_sides+1):
#             # a = sorted(nlargest(n_top_dice, dice+(i, )))
#
#             if total_dice-remaining<n_top_dice: # if dont have to start checking the top
#                 botop = botop if botop<i else i
#                 t+= recurse_top_dice(target_sum, total_dice, remaining-1, n_sides, n_top_dice, botop, top_sum+i)
#             else: #
#                 if i > botop:
#                     new_top_sum = top_sum-botop+i
#                     t += recurse_top_dice(target_sum, total_dice, remaining-1, n_sides, n_top_dice, i, new_top_sum)
#                 else:
#                     t += recurse_top_dice(target_sum, total_dice, remaining-1, n_sides, n_top_dice, botop, top_sum)
#         return t


def top_dice(n_dice, n_sides, n_top, target_sum):
    total = 0
    for starter in range(1, n_sides+1):
        total += recurse_top_dice(target_sum, n_dice-1, n_sides, n_top, (starter,))
        # total += recurse_top_dice(target_sum, n_dice, n_dice-1, n_sides, n_top, starter, starter)
    return total


print(top_dice(n_dice=5, n_sides=6, n_top=3, target_sum=15))
print(top_dice(n_dice=20, n_sides=12, n_top=10, target_sum=70))
# print(top_dice(5, 6, 3, 15))




# def recurse_top_dice()




def p240():
    pass


if __name__ == '__main__':
    p240()
