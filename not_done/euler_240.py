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


allrolls = 6**5
print(allrolls)
for c in product((1, 2, 3, 4, 5, 6), repeat=3):
    if sum(c)==15:
        print(c)

# def top_dice(target_sum, remaining, n_sides, n_top_dice, bottom_of_the_top):
#     if target_sum==0 and remaining==0:
#         return 1
#     if remaining == 0 and target_sum != 0:
#         return 0
#     else:
#         total = 0
#         for i in range(1, 6+1):
#             total += top_dice()


def top_dice(target_sum, remaining, n_sides, n_top_dice, top):
    if target_sum==0 and remaining==0:
        print(top)
        return 1
    if remaining == 0 and target_sum != 0:
        return 0
    else:
        total = 0
        for i in range(1, 6+1):
            print(remaining, n_sides, n_top_dice, top)
            tc = 
            # total += top_dice()
        return total

for start in range(1, 7):
    target_sum = 15
    a = top_dice(target_sum, 5, 6, 3, tuple([start]))
    print(a)




# def top_dice()




def p000():
    pass


if __name__ == '__main__':
    p000()
