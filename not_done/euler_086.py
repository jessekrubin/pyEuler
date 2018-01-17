#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse and Graham Rubin
"""
Path sum: two ways
Problem 81
In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by only moving to the right and down, is indicated in bold red
and is equal to 2427.

[[131, 673, 234, 103,  18],
 [201,  96, 342, 965, 150],
 [630, 803, 746, 422, 111],
 [537, 699, 497, 121, 956],
 [805, 732, 524,  37, 331]]

Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by
80 matrix, from the top left to the bottom right by only moving right and
down.
"""
import os
from os import path

g1 = [[131, 673, 234, 103, 18],
      [201, 96, 342, 965, 150],
      [630, 803, 746, 422, 111],
      [537, 699, 497, 121, 956],
      [805, 732, 524, 37, 331]]


def min_path_sum(grid):
    print(grid)
    width = len(grid[0])
    height = len(grid)
    for i in range(width):
        for j in range(height):
            if i * j == 0:
                if i == 0:
                    print("herm")

    print(width)
    print(height)


min_path_sum(g1)
# cur_dir = os.getcwd()
# with open(path.join(cur_dir, r"text_files\p081_matrix.txt")) as file:
#     ls = file.readlines()
# print(ls)
