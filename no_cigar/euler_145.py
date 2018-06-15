#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
How many reversible numbers are there below one-billion?
Problem 145
Some positive integers n have the property that the sum [ n + reverse(n) ]
consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and
409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and
904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?
"""
from pyximport import install
install()
from cypy145 import reverse, add_reverse, any_evens
from tqdm import tqdm


# def any_evens(n):
#     return any(c in '02468' for c in str(n))

def n_digit_reversibles(n_digits):
    r = set()
    for i in tqdm(range(10**(n_digits-1), 10**n_digits), ascii=True):
        # for i in tqdm(range(1, n), ascii=True):
        firstdig = (i//10**(n_digits-1))
        last = i % 10
        if (firstdig+last) % 2 != 0:
            if i % 10 != 0 and i not in r:  # and r not in seen:
                if not any_evens(add_reverse(i)):
                    # if any_evens(i):
                    r.add(i)
                    r.add(reverse(i))


    return len(r)


def reverseablesbelow(n=1000):
    t = 0
    for i in range(2, 9):
        t += (n_digit_reversibles(i))
        print(t)


reverseablesbelow()

n_digit_reversibles(3)

# def reversable_numbers_below(n):
#     r = set()
#     for i in tqdm(range(1, n), ascii=True):
#         if i%10!= 0 and i not in r: #and r not in seen:
#             if not any_evens(add_reverse(i)):
#             # if any_evens(i):
#                 r.add(i)
#                 r.add(reverse(i))
#             # else:
#     return len(r)#count


#
# # 608720
# # print(reversable_numbers_below(10))
# # print(reversable_numbers_below(100))
#
# for i in range(3, 9+1):
#     print(i, reversable_numbers_below(10**i))
