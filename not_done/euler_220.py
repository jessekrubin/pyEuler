#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Heighway Dragon
Problem 220
Let D0 be the two-letter string "Fa". For n≥1, derive Dn from Dn-1 by the
string-rewriting rules:

"a" → "aRbFR"
"b" → "LFaLb"

Thus, D0 = "Fa", D1 = "FaRbFR", D2 = "FaRbFRRLFaLbFR", and so on.

These strings can be interpreted as instructions to a computer graphics
program, with "F" meaning "draw forward one unit", "L" meaning "turn left 90
degrees", "R" meaning "turn right 90 degrees", and "a" and "b" being ignored.
The initial position of the computer cursor is (0,0), pointing up
towards (0,1).

Then Dn is an exotic drawing known as the Heighway Dragon of order n. For
example, D(10) is shown below; counting each "F" as one step, the highlighted
spot at (18,16) is the position reached after 500 steps.


What is the position of the cursor after 10**12 steps in D**50 ?
Give your answer in the form x,y with no spaces.
"""
from __future__ import division
from bib import xrange
from bib.decorations import cash_it, Jasm
from bib.maths import Vuple
from itertools import combinations


# @Jasm('../txt_files/highway_dragon.txt')
@cash_it
def d(n):
    if n == 0:
        return 'Fa'
    else:
        dragon = d(n-1)
        if len(dragon) >= 10**10:
            dragon = dragon[:10**10]
        return ''.join("aRbFR" if c == 'a' else "LFaLb" if c == 'b' else c for c in dragon)


assert 'Fa' == d(0)
assert 'FaRbFR' == d(1)
assert 'FaRbFRRLFaLbFR' == d(2)

# def ddd(n):
l = []
target = 2



def highway_dragon(max_order=50, steps=10**16):
    dirs = {
        0:Vuple((0, 1)),
        1:Vuple((1, 0)),
        2:Vuple((0, -1)),
        3:Vuple((-1, 0))
    }

    def clockwise(heading):
        if heading == 3:
            return 0
        else:
            return heading +1

    def counterclockwise(heading):
        if heading == 0:
            return 3
        else:
            return heading-1

    def dee(cur_order, highway, pos=Vuple((0, 0)), heading = 0, step=0):
        for h in highway:
            # print(h)
            if h == 'F':
                pos += dirs[heading]
                step += 1
                print(step, pos, heading)
                # if step == steps:
            if h == 'L':
                heading = counterclockwise(heading)
            if h == 'R':
                heading = clockwise(heading)
            if cur_order < max_order:
                if h == 'a':
                    pos, step, heading = dee(cur_order+1, 'aRbFR', pos, heading, step)
                if h == 'b':
                    pos , step, heading = dee(cur_order+1, 'LFaLb', pos, heading, step)
        return pos, step, heading
    curlevel = 0
    start = 'Fa'
    d = ''
    dee(0, start)

highway_dragon()
    # else:

    # return 'Fa' if n == 0 else ''.join("aRbFR" if c == 'a' else "LFaLb" if c == 'b' else c for c in d(n-1))
# print(d(50))
