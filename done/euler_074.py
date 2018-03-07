#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Digit factorial chains
Problem 74 
The number 145 is well known for the property that the sum of the factorial of
its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers
that link back to 169; it turns out that there are only three such loops that
exist:

169 >>> 363601 >>> 1454 >>> 169
871 >>> 45361 >>> 871
872 >>> 45362 >>> 872

It is not difficult to prove that EVERY starting number will eventually get
stuck in a loop. For example,

69 >>> 363600 >>> 1454 >>> 169 >>> 363601 (>>> 1454)
78 >>> 45360 >>> 871 >>> 45361 (>>> 871)
540 >>> 145 (>>> 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest
non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty
non-repeating terms?
"""

from lib.listless import digits_list
from math import factorial

dic = {}


def factorial_chain_length(starting_n):
    seen_nums = set()

    def recursing(n):
        next = sum(map(factorial, digits_list(n)))
        if next in seen_nums:
            return 1
        else:
            if n not in dic.keys():
                seen_nums.add(n)
                return recursing(next) + 1
            else:
                return dic[n]

    dic[starting_n] = recursing(starting_n)
    return dic[starting_n]


answer = 0
for i in range(1, 1000001):
    if factorial_chain_length(i) == 60:
        answer += 1

print("ANSWER: {}".format(answer))
