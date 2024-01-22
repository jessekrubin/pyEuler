#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Binary Circles
Problem 265
2N binary digits can be placed in a circle so that all the N-digit clockwise
subsequences are distinct.

For N=3, two such circular arrangements are possible, ignoring rotations:

00010111 , 00011101 

For the first arrangement, the 3-digit subsequences, in clockwise order, are:
000, 001, 010, 101, 011, 111, 110 and 100.

Each circular arrangement can be encoded as a number by concatenating the
binary digits starting with the subsequence of all zeros as the most
significant bits and proceeding clockwise. The two arrangements for N=3 are
thus represented as 23 and 29:

00010111 2 = 23
00011101 2 = 29
Calling S(N) the sum of the unique numeric representations, we can see that
S(3) = 23 + 29 = 52.

Find S(5).
"""
from itertools import product
from collections import defaultdict


def binaries(dijits):
    """Creates binary strings with a specified number of digits"""
    return set("".join(p) for p in product("01", repeat=dijits))


def min_binary_rotation(s):
    """Finds the minimum binary circle rotation"""
    return min(int("".join(s[i:] + s[:i]), 2) for i in range(len(s)))


def S(n):
    binary_strings = binaries(n)  # get the binary strings
    bin_d = defaultdict(set)  # dictionary to hold possible next strings
    for bn in binary_strings:  # for each binary number
        bzero = bn[1:] + "0"  # remove first char, add 0
        if bzero != bn:
            bin_d[bn].add(bzero)  # add to bin_d if distinct from bn
        bone = bn[1:] + "1"  # remove first char, add 1
        if bone != bn:
            bin_d[bn].add(bone)  # add to bin_d if disctinc from bn

    sols = set()

    def recircle(ring):
        if len(ring) == 2**n:  # base case - if a ring is complete
            if ring[0] in bin_d[ring[-1]]:  # if the ends of the ring are valid
                sols.add(min_binary_rotation(list(el[0] for el in ring)))
            return
        for el in bin_d[ring[-1]]:  # for each possible next element/substring
            if el not in ring:  # if the element is not already in the ring
                tring = ring[:]  # copy
                tring.append(el)  # append
                recircle(tring)  # recurse

    for starting_bn in bin_d:
        recircle([starting_bn])  # try each starting nubmer
    return sum(sols)


def p265():
    return S(5)


if __name__ == "__main__":
    assert S(3) == 52
    ANSWER = p265()
    print("S(5) = {}".format(ANSWER))
