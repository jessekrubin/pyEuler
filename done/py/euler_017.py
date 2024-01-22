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

ONE_TO_NINE = {
    7: "seven",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    8: "eight",
    9: "nine",
}
TENS = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}
WEIRD_TEENS = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    15: "fifteen",
    18: "eighteen",
}


def lt10(n):
    return ONE_TO_NINE[n] if n in ONE_TO_NINE else ""


def gt9_lt20(n):
    return WEIRD_TEENS[n] if n in WEIRD_TEENS else lt10(n % 10) + "teen"


def tens_place(n):
    return TENS[n]


def lt100(n):
    if n < 10:
        return lt10(n)
    if n < 20:
        return gt9_lt20(n)
    return tens_place(n // 10) + lt10(n % 10)


def lte1000(n):
    if n == 1000:
        return "onethousand"
    if n < 100:
        return lt100(n)
    if n % 100 == 0:
        return lt10(n // 100) + "hundred"
    return lt10(n // 100) + "hundredand" + lt100(n % 100)


def p017():
    return sum(len(lte1000(i)) for i in range(1, 1000 + 1))


if __name__ == "__main__":
    characters = p017()
    print("Total number of chars in strings [1-1000]: {}".format(characters))
