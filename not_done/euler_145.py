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


def reverse(n):
    reversed = 0
    while n > 0:
        reversed *= 10
        reversed += n % 10
        n //= 10
    return reversed


def is_reversible(n):
    if n % 10 == 0:
        return False
    soom = n + reverse(n)
    cur_dig = 0
    while soom > 0:
        cur_dig = soom % 10
        if cur_dig % 2 == 0:
            return False
        soom //= 10
    return True


def reversable_numbers_below(n):
    seen = set()
    count = 0
    for i in range(1, n):
        if i not in seen:
            if is_reversible(i):
                ri = reverse(i)
                if i == ri:
                    count += 1
                else:
                    seen.add(ri)
                    seen.add(i)
                    count += 2
    return count


# print(reversable_numbers_below(10))
print(reversable_numbers_below(100))
# print(reversable_numbers_below(1000))
print(reversable_numbers_below(10000))
print(reversable_numbers_below(100000))
print(reversable_numbers_below(1000000))
print(reversable_numbers_below(10000000))
print(reversable_numbers_below(100000000))
# print(reversable_numbers_below(1000000000))
