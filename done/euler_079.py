#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Passcode derivation
Problem 79
A common security method used for online banking is to ask the user for three 
random characters from a passcode. For example, if the passcode was 531278, they
 may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file 
so as to determine the shortest possible secret passcode of unknown length.
"""

passcode_nums = [
    319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629,
    168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290, 719, 680,
    318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316,
    729, 380, 319, 728, 716
]


class Graph(object):
    def __init__(self, digits):
        self.dig_dictionary = {}
        for d in digits:
            self.dig_dictionary[d] = set()

    def add_edge(self, first, second):
        self.dig_dictionary[first].add(second)

    def print_graph(self):
        setlists = []
        for key in self.dig_dictionary:
            print(key)
            print(self.dig_dictionary[key])
            setlists.append((self.dig_dictionary[key]))

    def make_guess(self):
        otherdict = {}
        for k in self.dig_dictionary:
            otherdict[len(self.dig_dictionary[k])] = k

        nums = []
        nums2 = []
        for o in otherdict:
            nums.append(o)
            nums2.append(otherdict[o])

        nums = nums.sort()
        guess = []
        for i in range(len(otherdict.keys())):
            guess.append(otherdict[i])
        guess.reverse()
        return guess


def digits_list(n):
    return [int(i) for i in [j for j in str(n)]]


def guess_passcode(keys):
    digits = set()
    for k in keys:
        for n in (digits_list(k)):
            digits.add(n)

    g = Graph(digits)
    for k in keys:
        digs = digits_list(k)
        g.add_edge(digs[0], digs[1])
        g.add_edge(digs[0], digs[2])
        g.add_edge(digs[1], digs[2])

    g.print_graph()
    guess_list = g.make_guess()
    guess_strings = [str(j) for j in guess_list]
    guess = "".join(guess_strings)
    return guess


print("password guess: {}".format(guess_passcode(passcode_nums)))
