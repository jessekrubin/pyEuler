#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Non-is_bouncy numbers
Problem 113
Working from left-to-right if no digit is exceeded by the digit to its left it
is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a
decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a
"bouncy" number; for example, 155349.

As n increases, the proportion of bouncy numbers below n increases such that
there are only 12951 numbers below one-million that are not bouncy and only
277032 non-bouncy numbers below 10**10.

How many numbers below a googol (10**100) are not bouncy?
"""
from lib.listless import digits_list


def is_bouncy(n):
    digits = digits_list(n)
    increasing = False
    decreasing = False
    for i in range(0, len(digits)-1):
        if digits[i+1] < digits[i]:
            increasing = True
        elif digits[i+1] > digits[i]:
            decreasing = True
        if increasing and decreasing:
            return True
    return False


def is_inc(n):
    digits = digits_list(n)
    for i in range(0, len(digits)-1):
        if digits[i+1] < digits[i]:
            return False
    return True


def is_dec(n):
    digits = digits_list(n)
    for i in range(0, len(digits)-1):
        if digits[i+1] > digits[i]:
            return False
    return True


incs = []
decs = []
both = []
for i in range(1, 10**6):
    # print(i, is_bouncy(i), is_inc(i), is_dec(i))
    if is_inc(i) and is_dec(i):
        both.append(i)
    elif is_inc(i) and not is_dec(i):
        incs.append(i)
    elif is_dec(i) and not is_inc(i):
        decs.append(i)

print(incs)
print(decs)
print(both)
print(len(incs))
print(len(decs))
print(len(both))
print((len(incs)+len(decs)-len(both)))
print(len(set.union(incs, decs, both)))

# def increasing(last, remaining_digits):
#     if remaining_digits==0:
#         return 10 - last
#     else:
#         retval = 0
#         for i in range(last, 10):
#             retval += increasing(i, remaining_digits-1)
#         return retval
#
# def decreasing(last, remaining_digits):
#     if remaining_digits==0:
#         return last
#     else:
#         retval = 0
#         for i in range(0, last+1):
#             retval += decreasing(i, remaining_digits-1)
#         return retval
#
#
# inc = (increasing(1, 6))
# print(inc, inc+inc)
# inc = (increasing(1, 10))
# print(inc, inc+inc)
# dec = (decreasing(9, 6))

# def num_nums(last, remaining_digits):
#     if remaining_digits == 0:
#         return 1
#     else:
#         ret_val = 0
#         for i in range(10 - (last)):
#             ret_val += num_nums(i, remaining_digits - 1)
#         return ret_val

# print(num_nums(1, 10))

# def is_bouncy(n):
#     digits = digits_list(n)
#     increasing = False
#     decreasing = False
#     for i in range(0, len(digits) - 1):
#         if digits[i + 1] < digits[i]:
#             increasing = True
#         elif digits[i + 1] > digits[i]:
#             decreasing = True
#         if increasing and decreasing:
#             return True
#     return False
#
#
# def find_proportion(percent):
#     i = 100
#     bouncy_count = 0
#     while True:
#         i += 1
#         if is_bouncy(i):
#             bouncy_count += 1
#         if bouncy_count / i == (percent / 100):
#             return i
#
#
# percentage = 90
# answer = find_proportion(percentage)
# print("Least num for which {}% of numbers are is_bouncy: {}".format(percentage, answer))
# percentage = 99
# answer = find_proportion(percentage)
# print("Least num for which {}% of numbers are is_bouncy: {}".format(percentage, answer))
