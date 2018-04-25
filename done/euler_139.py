#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Pythagorean tiles
Problem 139
Let (a, b, c) represent the three sides of a right angle triangle with integral
length sides. It is possible to place four such triangles together to form a
square with length c.

For example, (3, 4, 5) triangles can be placed together to form a 5 by 5
square with a 1 by 1 hole in the middle and it can be seen that the 5 by 5
square can be tiled with twenty-five 1 by 1 squares.


However, if (5, 12, 13) triangles were used then the hole would measure 7 by 7
and these could not be used to tile the 13 by 13 square.

Given that the perimeter of the right triangle is less than one-hundred
million, how many Pythagorean triangles would allow such a tiling to take
place?
"""

from lib.maths import pytriple_gen


def pytiles(max_perimeter):
    """
    we are looking for triangles where the hypotenuse is divisible by the side
    length of the inner square, which is the difference in the RAT legs,

    :param max_perimeter: max right triangle perimeter
    :return: number of triangles
    """
    count = 0
    for tri in pytriple_gen(max_perimeter // 2):
        if tri[2] % (tri[1] - tri[0]) == 0:
            count += (max_perimeter // sum(tri))
    return count


def p139():
    assert 9 == pytiles(100)
    assert 99 == pytiles(1000)
    sol = pytiles(10 ** 8)
    print("# py-try-angles: {}".format(sol))


if __name__ == '__main__':
    p139()
