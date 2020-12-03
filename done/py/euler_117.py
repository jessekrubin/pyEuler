#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Red, green, and blue tiles
Problem 117
Using a combination of black square tiles and oblong tiles chosen from: red
tiles measuring two units, green tiles measuring three units, and blue tiles
measuring four units, it is possible to tile a row measuring five units in
length in exactly fifteen different ways.

How many ways can a row measuring fifty units in length be tiled?

NOTE: This is related to Problem 116.
"""

from pupy.maths import partitions_gen, n_permutations_with_replacements


def red_green_AND_blue(row_size):
    parts = list(p for p in partitions_gen(row_size, 1, 4))
    arrangements = 0
    for part in parts:
        arrangements += n_permutations_with_replacements(part)
    return arrangements


def p117():
    return red_green_AND_blue(50)


if __name__ == '__main__':
    ANSWER = p117()
    print("# arrangements: {}".format(ANSWER))
