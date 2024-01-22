#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Roman numerals
Problem 89
For a number written in Roman numerals to be considered valid there are basic
rules which must be followed. Even though the rules allow some numbers to be
expressed in more than one way there is always a "best" way of writing a
particular number.

For example, it would appear that there are at least six ways of writing the
number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last
example is considered to be the most efficient, as it uses the least number
of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'),
contains one thousand numbers written in valid, but not necessarily minimal,
Roman numerals; see About... Roman Numerals for the definitive rules for this
problem.

Find the number of characters saved by writing each of these in their minimal
form.

Note: You can assume that all the Roman numerals in the file contain no more
than four consecutive identical units.
"""


def further_shrink(roman_str):
    roman_str = roman_str.replace("DCCCC", "CM")
    roman_str = roman_str.replace("LXXXX", "XC")
    roman_str = roman_str.replace("VIIII", "IX")
    roman_str = roman_str.replace("CCCC", "CD")
    roman_str = roman_str.replace("XXXX", "XL")
    roman_str = roman_str.replace("IIII", "IV")
    return roman_str


def saved_chars_better(roman):
    return len(roman) - len(further_shrink(roman))


def p089():
    with open("../../txt_files/p089_roman_nums.txt") as f:  # load the roman numerals
        numerals = [numeral.strip("\n") for numeral in f.readlines()]

    return sum(map(saved_chars_better, numerals))


if __name__ == "__main__":
    answer = p089()
    print("Characters saved {}".format(answer))
