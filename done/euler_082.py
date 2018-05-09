#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Path sum: three ways
Problem 82
NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the
left column and finishing in any cell in the right column, and only moving up,
down, and right, is indicated in red and bold; the sum is equal to 994.

          [[131, 673, 234, 103, 18],
           [201,  96, 342, 965, 150],
           [630, 803, 746, 422, 111],
           [537, 699, 497, 121, 956],
           [805, 732, 524,  37, 331]]

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target
As..."), a 31K text file containing a 80 by 80 matrix, from the left column to
the right column.
"""


def min_path_three_ways(mat):
    mat = list(map(list, zip(*mat)))  # transpose lists so that we can just jump frum list to list
    h = len(mat)
    w = len(mat[0])
    solution = [mat[0][:]]
    for i in range(1, h):
        sweeper2 = [0] * w
        left = [solution[i - 1][0], (solution[i - 1][1] + mat[i][1])]
        right = [solution[i - 1][w - 1], (solution[i - 1][w - 2] + mat[i][w - 2])]
        sweeper2[0] = min(left)
        sweeper2[w - 1] = min(right)
        for j in range(1, w - 1):
            paths = []
            paths.append(solution[i - 1][j])
            if j > 0:  # check horizontal paths going one way
                for jj in range(j):
                    paths.append((solution[i - 1][jj]) + sum(mat[i][jj:j]))
            if j < (w - 1):  # check horizontal paths going the other way
                for jj in range(j + 1, w - 1):
                    paths.append((solution[i - 1][jj]) + sum(mat[i][j + 1:jj + 1]))
            sweeper2[j] = min(paths)
        for j in range(w):
            sweeper2[j] += mat[i][j]
        solution.append(sweeper2)
    return min(solution[-1])


def p082():
    lil_mat = [[131, 673, 234, 103, 18],
               [201, 96, 342, 965, 150],
               [630, 803, 746, 422, 111],
               [537, 699, 497, 121, 956],
               [805, 732, 524, 37, 331]]

    with open('../txt_files/p081_p082_p083_matrix.txt') as f:  # load the matrix
        big_mat = list(list(map(int, row.strip('\n').split(','))) for row in f.readlines())
    assert 994 == min_path_three_ways(lil_mat)  # check the small test case
    return min_path_three_ways(big_mat)


if __name__ == '__main__':
    answer = p082()
    print("Minimum path three ways: {}".format(answer))