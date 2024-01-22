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

lil_mat = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331],
]

with open(r"../../txt_files/p081_p082_p083_matrix.txt") as f:  # load the matrix
    big_mat = [list(map(int, row.strip("\n").split(","))) for row in f.readlines()]


def min_path_two_ways(grid):
    # size of the grid
    sol_grid = grid
    size = len(sol_grid)

    # handle the first row
    for i in range(1, size):
        sol_grid[0][i] += sol_grid[0][i - 1]

    # handle the first column
    for j in range(1, size):
        sol_grid[j][0] += sol_grid[j - 1][0]

    # for each box not in the first row and the first column in 'Z' order
    for i in range(1, size):
        for j in range(1, size):
            # take the min
            sol_grid[i][j] += min(sol_grid[i - 1][j], sol_grid[i][j - 1])

    # return the last value
    return sol_grid[size - 1][size - 1]


def p081():
    return min_path_two_ways(big_mat)


if __name__ == "__main__":
    assert min_path_two_ways(lil_mat) == 2427  # check the small test_pupy case
    answer = p081()
    print("Minimum path two ways: {}".format(answer))
