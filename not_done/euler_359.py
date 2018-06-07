#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Jesse Rubin ~ project Euler ~
"""
Problem Name
prob #

Prompt
"""
from functools import wraps
from bib.decorations import cash_it
# 71328803586048 == (2**27) * (2**12)
PRODUCT = 71328803586048
PRODUCT_PAIRS = set(tuple(sorted((a, PRODUCT//a)))
                    for a in ((2**twoexp)*(3**threeexp)
                              for threeexp in range(12+1)
                              for twoexp in range(27+1)))

@cash_it
def is_square(n):
    for i in count(1):
        sqi = i*i
        if sqi == n: return True
        elif sqi > n: return False




SQ = [i*i for i in range(1000)]
from itertools import *

from collections import defaultdict
# d = defaultdict(list)
# for i in count(1):
#     if i > 5000000:
#         break
#     fr = None
#     for floor in count(1):
#         if (len(d[floor])>0 and is_square(d[floor][-1] + i)) or len(d[floor])==0:
#             d[floor].append(i)
#             fr = tuple(sorted((floor, len(d[floor]))))
#             if fr in PRODUCT_PAIRS:
#                 print("YEAH")
#
#             break
#     if i %100 == 0:
#         print(i, fr)
occupant_d = {}.setdefault(default=0)
room_d = {}.setdefault(default=0)
for i in count(1):
    if i > 5000000:
        break
    fr = None
    for floor in count(1):
        if (floor in occupant_d and floor in room_d and is_square(occupant_d[floor]+i)) or (occupant_d[floor])==0:
            occupant_d[floor].append(i)
            fr = tuple(sorted((floor, len(occupant_d[floor]))))
            print("YEAH")

        if fr in PRODUCT_PAIRS:
            break
    if i %100 == 0:
        print(i, fr)
        # elif len(d[floor])==0:
        #     d[floor].append(i)
        #     break


print(occupant_d[1][0])
print(occupant_d[1][1])
print(occupant_d[2][0])

def p000():
    pass


if __name__ == '__main__':
    ANSWER = p000()
    print("ANSWER: {}".format(ANSWER))
