#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
"""

from lib.decorations import cash_it

combs = set()
from copy import copy

# def block_combos(remaining, cur=None):
#     if remaining == 0:
#         # print(tuple(cur))
#         # combs.add(tuple(cur))
#         return tuple(cur)
#     elif 0 < remaining < 3:
#         a = copy(cur)
#         a.append(1)
#         block_combos(remaining-1, a)
#     elif cur is None:
#         cur = []
#         cp = copy(cur)
#         cp.append(1)
#         block_combos(remaining-1, cp)
#     another = copy(cur)
#     another.append(1)
#     block_combos(remaining-1, another)
#     if len(cur) == 0 or cur[-1] == 1:
#         for i in range(3, remaining+1):
#             cp = copy(cur)
#             cp.append(i)
#             block_combos(remaining-i, cp)

thing = []
def block_combos(remaining, thingy=False):
    if remaining==0:
        return ''
    if remaining < 3:
        return '1'+block_combos(remaining-1)
    if thingy:
        return '1'+block_combos(remaining-1)
    else:
        shit = set()
        for i in range(1, remaining):
            if i == 1:
                a = '1'+block_combos(remaining-1, thingy=True)

            if i>2:
                b = str(1)+block_combos(remaining-i)
                shit.add(b)



    # if remaining == 0:
    #     # print(cur)
    #     return cur
    #     # cur
    # elif 0 < remaining < 3:
    #     a = copy(cur)
    #     a += '1'
    #     return '1' + block_combos(remaining-1, a)
    # elif cur == '':
    #     cp = copy(cur)
    #     cp += '1'
    #     block_combos(remaining-1, cp)
    # another = copy(cur)
    # another += '1'
    # block_combos(remaining-1, another)
    # if len(cur) == 0 or cur[-1] == '1':
    #     for i in range(3, remaining+1):
    #         cp = copy(cur)
    #         # cp.append(i)
    #         cp += str(i)
    #         ans = str(i)+block_combos(remaining-i)




r = 7
a = block_combos(r)
print(a)
print(combs)
print(thing)
print(len(combs))
# r = 50
# block_combos(r)
# print(combs)
# print(len(combs))
