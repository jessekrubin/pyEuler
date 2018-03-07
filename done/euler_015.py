#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Lattice paths
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

def calc_next_row(row):
    row_size = len(row)
    next_row = [1] + [0, ] * (row_size - 1)
    for i in range(1,row_size):
        next_row[i] += row[i] + next_row[i-1]
    return next_row

size = 20
grid = []
first_row = [1, ] * size
grid.append(first_row)
while(len(grid) < 22):
    grid.append(calc_next_row(grid[-1]))

ANSWER = grid[-1][-1]
print("Number of paths: {}".format(ANSWER))

