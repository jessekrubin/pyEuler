# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler

"""
Coded triangle numbers
Problem 42
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so
the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle words?
"""

from pupy.cheese import string_score


def p042():
    with open(r"../../txt_files/p042_words.txt") as f:
        words = [s.strip('"') for s in f.readlines()[0].split(",")]

    word_scores = map(string_score, words)
    max_word_score = max(map(string_score, words))

    i = 2
    cur_triangle_num = 1
    triangle_numbers_below_max = []
    while cur_triangle_num <= max_word_score:
        triangle_numbers_below_max.append(cur_triangle_num)
        cur_triangle_num += i
        i += 1
    return sum([1 for i in word_scores if i in triangle_numbers_below_max])


if __name__ == "__main__":
    answer = p042()
    print("# coded triangle numbers: {}".format(answer))
