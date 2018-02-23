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

g1 = [[131, 673, 234, 103,  18],
      [201,  96, 342, 965, 150],
      [630, 803, 746, 422, 111],
      [537, 699, 497, 121, 956],
      [805, 732, 524,  37, 331]]


def min_path(grid):
    w = len(grid[0])
    h = len(grid)

    def coord_val(place):
        return grid[place[0]][place[1]]

    sol_grid = [[0] * w for i in range(h)]
    sol_grid[0][0] = coord_val((0, 0))

    def sol_coord_val(place):
        return sol_grid[place[0]][place[1]]

    def set_solgrid(place, val):
        sol_grid[place[0]][place[1]] = val

    def printgrid():
        print("_____________")
        for r in sol_grid:
            print(r)

    def level_coordinates(level):
        side = [(i, level) for i in range(level, h)]
        top = [(level, i) for i in range(level, w)]
        return side + top

    def calc_level(level):
        coords = sorted(level_coordinates(level))
        if level == 0:
            for coord in coords:
                if coord == (0, 0):
                    print(coord)
                    set_solgrid(coord, (coord_val(coord)))
                    # set_solgrid(coord, (coord_val(coord) + coord_val( (coord[0] - 1, coord[1]))))
                else:
                    if coord[0] == 0:
                        set_solgrid(coord, (coord_val(coord) + coord_val((coord[0], coord[1]-1))))
                    else:
                        set_solgrid(coord, (coord_val(coord) + coord_val((coord[0]-1, coord[1]))))
        else:
            for coord in coords:
                coordval = coord_val(coord)
                uno = (coordval + sol_coord_val((coord[0] - 1, coord[1])))
                dos = (coordval + sol_coord_val((coord[0], coord[1] - 1)))
                set_solgrid(coord, min([uno, dos]))
            # for coord in top:
            #     uno = (coord_val(coord) + sol_coord_val(
            #         (coord[0] - 1, coord[1])))
            #     dos = (coord_val(coord) + sol_coord_val(
            #         (coord[0], coord[1] - 1)))
            #     set_solgrid(coord, min([uno, dos]))

    for i in range(h):
        calc_level(i)
        printgrid()

    # allcoords = set([(i, j) for i in range(w) for j in range(h)])
    printgrid()


min_path(g1)
