# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Triangle containment
Problem 102
Three distinct from_points are plotted at random on a Cartesian plane, for
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
from pupy.maths import Trigon


def p102():
    # open file and put into list
    with open(r'../../txt_files/p102_triangles.txt') as f:
        triangles = [
            tuple(map(int, j.split(',')))
            for j in [i.strip('\n') for i in f.readlines()]
        ]
    # check if (0, 0) in triangle for triangle in the list
    return sum(1 for tri in triangles if (0, 0) in Trigon.from_points(tri))


if __name__ == '__main__':
    ANSWER = p102()
    print("# triangles: {}".format(ANSWER))
