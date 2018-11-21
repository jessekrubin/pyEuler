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
from itertools import combinations, count

with open('../../txt_files/p098_words.txt') as f: # load the matrix
    words = [word.strip('"') for word in f.readline().split(',')]

d = {}
for w in words:
    so = ''.join(c for c in sorted(w))
    if so in d:
        d[so].append(w)
    else:
        d[so] = [w]

anagrams = list(v for v in d.values() if len(v) > 1)
longest_anna_gram = max(len(a[0]) for a in anagrams)
shortest = min(len(a[0]) for a in anagrams)

squares = {i:set() for i in range(longest_anna_gram+1)}
s = []
for i in count(1):
    ii = i*i
    if i*i >= 1000000000:
        break
    else:
        iis = str(ii)
        squares[len(iis)].add(iis)

def is2(a, b, n):
    pass
    nb = b
    digitsused = set()
    for p, q in zip(a, n):
        if q in digitsused:
            return
        nb = nb.replace(p, q)
        digitsused.add(q)
    if nb[0] == '0':
        return
    if nb not in squares[len(a)]:
        return
    return nb
    
def isit(a, b):
    l = len(a)
    for square in squares[l]:
        r = is2(a, b, square)
        if r is not None:
            yield square
            yield r

things = list()

for an in anagrams:
    for cb in combinations(an, 2):
        things.extend(isit(*cb))


# isit('RACE', 'CARE')
# is2('RACE', 'CARE', '9216')
if __name__ == '__main__':

    nums = map(int, things)
    maxn = max(nums)
    print("ANSWER", maxn)



