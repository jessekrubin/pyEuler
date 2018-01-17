#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin ~ Project Euler
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""


def one_nine(n: int):
    if n == 1:
        return "one"
    elif n == 2:
        return "two"
    elif n == 3:
        return "three"
    elif n == 4:
        return "four"
    elif n == 5:
        return "five"
    elif n == 6:
        return "six"
    elif n == 7:
        return "seven"
    elif n == 8:
        return "eight"
    elif n == 9:
        return "nine"
    return ""


def tens_place(n):
    if n == 2:
        return "twenty"
    elif n == 3:
        return "thirty"
    elif n == 4:
        return "forty"
    elif n == 5:
        return "fifty"
    elif n == 6:
        return "sixty"
    elif n == 7:
        return "seventy"
    elif n == 8:
        return "eighty"
    return "ninety"


def one_ninenine(n):
    """returns strings for numbers 1 - 99"""
    if n < 10:
        return one_nine(n)
    else:
        if n == 10:
            return "ten"
        elif n == 11:
            return "eleven"
        elif n == 12:
            return "twelve"
        elif n == 13:
            return "thirteen"
        elif n == 15:
            return "fifteen"
        elif n == 18:
            return "eighteen"
        elif n < 20:
            a, b = divmod(n, 10)
            return one_nine(b) + "teen"
        else:
            a, b = divmod(n, 10)
            return tens_place(a) + " " + one_nine(b)


def write_num_as_string(n):
    if n == 1000:
        return "one thousand"
        else:
        a, b = divmod(n, 100)
        if a == 0:
            return one_ninenine(n)
        elif n % 100 == 0:
            return one_nine(a) + " hundred "

        else:
            return one_nine(a) + " hundred and " + one_ninenine(b)


characters = 0
for i in range(1, 1001):
    # print("~~~")
    # print(i)
    # print(write_num_as_string(i))
    # print(len(write_num_as_string(i)))
    # print((write_num_as_string(i).replace(" ", "")))
    # print(len(write_num_as_string(i).replace(" ", "")))
    characters += len(write_num_as_string(i).replace(" ", ""))

print("total number of chars in strings [1-1000]:")
print(characters)
