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

def path_sum_three_wayz(mat, starting):
    rows = len(mat)
    cols = len(mat[0])
    start = starting
    finish = (rows-1, cols-1)
    visited = set()
    current = {start}
    solution = {}
    solution[start] = mat[0][0]

    def adjacents(p):
        r, c = p
        adj = set()
        if r > 0:
            adj.add((r-1, c))
        if r < rows-1:
            adj.add((r+1, c))
        # if c > 0:
        #     adj.add((r, c-1))
        if c < rows-1:
            adj.add((r, c+1))
        return adj

    def iterat(current):
        next = set()
        for point in current:
            visited.add(point)
            naybors = adjacents(point)
            for naybor in naybors:
                nval = (mat[naybor[0]][naybor[1]])
                if naybor in solution:
                    new = solution[point] + nval
                    if solution[naybor] > new:
                        solution[naybor] = new
                else:
                    solution[naybor] = solution.get(naybor, nval) + solution[point]
                next.add(naybor)
        return next

    # def
        # for i in range(rows*cols):
    for i in range((rows+cols)+4):
        # while finish not in solution:
        current = iterat(current)
    # thing = [solution[tuple((r, cols))] for r in range(rows)]
    # print(thing)
    return min([solution[(i, cols-1)] for i in range(rows)])
        # print(thing)
        # return solution[finish]


def path_sum_three_ways(mat):
    size = len(mat)
    thing = []
    for i in range(size):
        stuf = (path_sum_three_wayz(mat, (i,0)))
        thing.append(stuf)
        print(thing)
        print(min(thing))

print(path_sum_three_ways(lil_mat))
print(path_sum_three_ways(big_mat))

lil_mat = [list(reversed(line)) for line in lil_mat]

# [121, 1086, 533, 489, 368]
# [355, 697, 1279, 986, 892]
# [1028, 793, 1596, 1685, 1624]
# [1125, 994, 1624, 2161, 2429]
# def min_path_three_ways(sol_grid):
#     printing = False
#     # size of the grid
#     size = len(sol_grid)
#     for col in range(1,size):
#         sweeper2 = []
#         if printing:
#             print("___")
#             print("COL", col)
#             pprint(sol_grid)
#         for row in range(0, size):
#             vals = [sol_grid[row][col-1]]
#             if row == 0:
#                 vals.append(sol_grid[row+1][col-1] + sol_grid[row+1][col])
#             elif row == (size - 1):
#                 vals.append(sol_grid[row-1][col-1] + sol_grid[row-1][col])
#             else:
#                 vals.append(sol_grid[row+1][col-1] + sol_grid[row+1][col])
#                 vals.append(sol_grid[row-1][col-1] + sol_grid[row-1][col])
#             # if row < size-2:
#             #     vals.append(sol_grid[row+1][col-1] + sol_grid[row+1][col])
#
#             # sol_grid[row][col] += min(vals)
#             sweeper2.append(min(vals))
#         for row in range(0, size):
#             sol_grid[row][col] += sweeper2[row]
#         if printing:
#             print("GRID UPDATED COL")
#             print("")
#             print(sweeper2)
#             pprint(sol_grid)
#
#     lascol = ([sol_grid[r][size-1] for r in range(size)])
#     return min(lascol)
#
# def p083():
#     lil_test = min_path_three_ways(lil_mat) # check the small test case
#     print(lil_test)
#     return min_path_three_ways(big_mat)
#
# if __name__ == '__main__':
#     answer = p083()
#     print("Minimum path two ways: {}".format(answer))
