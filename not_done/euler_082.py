#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
"""
from lib.decorations import tictoc
from pprint import pprint

lil_mat = [[131, 673, 234, 103, 18],
           [201,  96, 342, 965, 150],
           [630, 803, 746, 422, 111],
           [537, 699, 497, 121, 956],
           [805, 732, 524,  37, 331]]

with open('../txt_files/p082_matrix.txt') as f: # load the matrix
    big_mat = list(list(map(int, row.strip('\n').split(','))) for row in f.readlines())


lil_mat = [list(reversed(line)) for line in lil_mat]

[121, 1086, 533, 489, 368]
[355, 697, 1279, 986, 892]
[1028, 793, 1596, 1685, 1624]
[1125, 994, 1624, 2161, 2429]

def min_path_three_ways(sol_grid):
    printing = False
    # size of the grid
    size = len(sol_grid)
    outerswep = [0] * size
    for col in range(1, size):
        sweeper2 = outerswep
        if printing:
            print("___")
            print("COL", col)
            pprint(sol_grid)
        for row in range(0, size):

            vals = [sol_grid[row][col-1]]
            # if row == 0:
            #     vals.append(sol_grid[row+1][col-1] + sol_grid[row+1][col])
            # if row == (size - 1):
            #     vals.append(sol_grid[row-1][col-1] + sol_grid[row-1][col])
            # else:

            # try:
            #     vals.append(sol_grid[row+1][col-1] + sol_grid[row+1][col])
            # except:
            #     pass
            # try:
            #     vals.append(sol_grid[row-1][col-1] + sol_grid[row-1][col])
            # except:
            #     pass
            try:
                vals.append(outerswep[row+1] + sol_grid[row+1][col])
            except:
                pass
            try:
                vals.append(outerswep[row-1] + sol_grid[row-1][col])
            except:
                pass
            sweeper2[row] = (min(vals))
        for row in range(0, size):
            if row == 3 and col == 4:
                print(row)
            sol_grid[row][col] += sweeper2[row]
        outerswep = sweeper2
        if printing:
            print("GRID UPDATED COL")
            print("")
            print(sweeper2)
            pprint(sol_grid)
    print(outerswep)
    print(min(outerswep))
    lascol = ([sol_grid[r][size-1] for r in range(size)])
    return min(lascol)

def p083():
    lil_test = min_path_three_ways(lil_mat) # check the small test case
    print(lil_test)
    return min_path_three_ways(big_mat)

if __name__ == '__main__':
    answer = p083()
    print("Minimum path two ways: {}".format(answer))
