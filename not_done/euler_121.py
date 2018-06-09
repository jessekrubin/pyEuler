#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Disc game prize fund
Problem 121
A bag contains one red disc and one blue disc. In a game of chance a player
takes a disc at random and its colour is noted. After each turn the disc is
returned to the bag, an extra red disc is added, and another disc is taken at
random.

The player pays £1 to play and wins if they have taken more blue discs than
red discs at the end of the game.

If the game is played for four turns, the probability of a player winning is
exactly 11/120, and so the maximum prize fund the banker should allocate for
winning in this game would be £10 before they would expect to incur a loss.
Note that any payout will be a whole number of pounds and also includes the
original £1 paid to play the game, so in the example given the player actually
wins £9.

Find the maximum prize fund that should be allocated to a single game in
which fifteen turns are played.
"""
from __future__ import division
from bib.maths import repermutations

bag = 'rb'


from collections import Counter

def dgame():
    thing = []
    t = 0
    wins = []
    totalturns = 4
    c = Counter()

    def _rec(rturns, s, cb='rb'):

        if rturns == 0:
            thing.append(s)
            print(s, repermutations(s))
            print(s.count('r')>s.count('b'))
            if (s.count('r')>s.count('b')): wins.append(s)

        else:
            # ts1 = ''.join(d for d in s) + 'r'
            # _rec(rturns-1, ts1)
            for c in cb:
                ts = ''.join(d for d in s) + c
                _rec(rturns-1, ts, cb+'b')

#
#
#     _rec(4-1,'r')
    _rec(4-1,'b')
    # print(thing)
#     c = Counter(thing)
#     print(c)
#     print(sum(v for v in c.values()))

# t = sum(repermutations(n) for n in thing)
# print(t)
# tr, tb = 0, 0
# def dgame():
#     thing = []
#     t = 0
#     wins = []
#     totalturns = 4
#     c = Counter()
#
#     def _rec(rturns, s, cb='rb'):
#
#         if rturns == 0:
#             thing.append(s)
#             print(s, repermutations(s))
#             print(s.count('r')>s.count('b'))
#             if (s.count('r')>s.count('b')): wins.append(s)
#
#         else:
#             # ts1 = ''.join(d for d in s) + 'r'
#             # _rec(rturns-1, ts1)
#             for c in cb:
#                 ts = ''.join(d for d in s) + c
#                 _rec(rturns-1, ts, cb+'b')
#
#
#
#     _rec(4-1,'r')
#     _rec(4-1,'b')
#     print(thing)
#     c = Counter(thing)
#     print(c)
#     print(sum(v for v in c.values()))

    # t = sum(repermutations(n) for n in thing)
    # print(t)
    # tr, tb = 0, 0
    # for n in thing:
    #     reds, blues = 0, 0
    #     for c in n:
    #         if c == 'r':
    #             reds += 1
    #         if c == 'b':
    #             blues += 1
    #     if reds > blues:
    #         tr += 1
    #     else:
    #         tb += 1

        # print(reds, blues)



dgame()
