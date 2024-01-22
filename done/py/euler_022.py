#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin ~ Project Euler
"""
Name scores
Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is  ### you can fit just about this much in
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN      ###
would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

from pupy.cheese import string_score


def p022():
    with open(r"../../txt_files/p022_names.txt", "r") as file:
        names = file.readline().strip('"').split('","')
    names.sort()
    return sum(i + 1 * string_score(names[i]) for i in range(len(names)))


# txt_files/p022_names.txt
if __name__ == "__main__":
    assert 53 == string_score("COLIN")
    total_score = p022()
    print("Total: {}".format(total_score))
