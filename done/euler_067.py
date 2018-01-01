#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Maximum path sum II
Problem 67
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""
import os.path
from os import path

lil_string_triangle = """3
7 4
2 4 6
8 5 9 3"""


# CODE FROM PROBLEM 18
def triangle_lists(s):
    lines = s.split("\n")
    listlist = [line.split(" ") for line in lines]
    lists = []
    for l in listlist:
        lists.append(list(map(int, l)))
    return (lists)


def max_two_rows(upper, lower):
    # print("++++++")
    # print(upper)
    # print(lower)
    new_upper = list([0] * len(upper))
    for i in range(len(upper)):
        # print(i)
        new_upper[i] = max([upper[i] + lower[i], upper[i] + lower[i + 1]])
    # print(new_upper)
    return new_upper


def tri_max_fast(l):
    cur_row = l[len(l) - 1]
    for i in range(len(l) - 2, -1, -1):
        # print(i)
        # print(cur_row)
        # print(l[i])
        cur_row = max_two_rows(l[i], cur_row)
    return max(cur_row)


little_tri = triangle_lists(lil_string_triangle)

#open file and put into list
cur_dir = (os.getcwd())
with open(path.join(cur_dir, r'text_files/p067_triangle.txt'), 'r') as f:
    # triangles = [
    #     tuple(map(int, j.split(',')))
    #     for j in [i.strip('\n') for i in f.readlines()]
    # ]
    lines = tuple([
        tuple(map(int, j.split(' ')))
        for j in [i.strip('\n') for i in f.readlines()]
    ])

big_tri = lines

answer = tri_max_fast(little_tri)
print("Little Triangle MAX PATH: {}".format(answer))

answer2 = tri_max_fast(big_tri)
print("Big Triangle MAX PATH: {}".format(answer2))