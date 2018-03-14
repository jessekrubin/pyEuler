#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Anagramic squares
Problem 98
By replacing each of the letters in the word CARE with 1, 2, 9, and 6
respectively, we form a square number: 1296 = 36^2. What is remarkable
is that, by using the same digital substitutions, the anagram, RACE, also forms
a square number: 9216 = 96^2. We shall call CARE (and RACE) a square anagram
word pair and specify further that leading zeroes are not permitted, neither
may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, find all the square
anagram word pairs (a palindromic word is NOT considered to be an anagram of
itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
"""

from math import sqrt

with open('../txt_files/p098_words.txt') as f: # load the matrix
    words = [word.strip('"') for word in f.readline().split(',')]

max_word_length = max(len(word) for word in words) # get the max word length


max_square = int(sqrt(10**max_word_length)+1)

squares = set(i**2 for i in range(1, max_square))
# print(squares)
print(len(squares))







