# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Triangle containment
Problem 102
Three distinct points are plotted at random on a Cartesian plane, for 
which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ
does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file
containing the co-ordinates of one thousand "random" triangles, find the number
of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example 
given above.
"""

import numpy as np

# open file and put into list
with open(r'text_files/p102_triangles.txt') as f:
    triangles = [
        tuple(map(int, j.split(',')))
        for j in [i.strip('\n') for i in f.readlines()]
    ]


def triangle_area(v1, v2):
    return abs(np.cross(v1, v2)) / 2


def origin_trianlges(a, b, c):
    return triangle_area(a, b) + triangle_area(b, c) + triangle_area(a, c)


def origin_in_trianlge(l):
    # print(l)
    a = np.array([l[0], l[1]])
    b = np.array([l[2], l[3]])
    c = np.array([l[4], l[5]])
    ab = np.array([(l[2] - l[0]), (l[3] - l[1])])
    ac = np.array([(l[4] - l[0]), (l[5] - l[1])])

    if triangle_area(ab, ac) != origin_trianlges(a, b, c):
        return False
    return True

    # print(a)
    # print(b)
    # print(c)
    # print(ab)
    # print(ac)
    # print(big_t)
    # print(tri_t)


answer = sum([1 for i in list(map(origin_in_trianlge, triangles)) if i])
print("# triangles: {}".format(answer))
