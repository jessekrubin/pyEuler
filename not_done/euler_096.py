#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Su Doku
Problem 96

Su Doku (Japanese meaning number place) is the name given to a popular puzzle
concept. Its origin is unclear, but credit must be attributed to Leonhard Euler
who invented a similar, and much more difficult, puzzle idea called Latin
Squares. The objective of Su Doku puzzles, however, is to replace the blanks
(or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box
contains each of the digits 1 to 9. Below is an example of a typical starting
puzzle grid and its solution grid.

            0 0 3 0 2 0 6 0 0                4 8 3 9 2 1 6 5 7
            9 0 0 3 0 5 0 0 1                9 6 7 3 4 5 8 2 1
            0 0 1 8 0 6 4 0 0                2 5 1 8 7 6 4 9 3
            0 0 8 1 0 2 9 0 0                5 4 8 1 3 2 9 7 6
            7 0 0 0 0 0 0 0 8                7 2 9 5 6 4 1 3 8
            0 0 6 7 0 8 2 0 0                1 3 6 7 9 8 2 4 5
            0 0 2 6 0 9 5 0 0                3 7 2 6 8 9 5 1 4
            8 0 0 2 0 3 0 0 9                8 1 4 2 5 3 7 6 9
            0 0 5 0 1 0 3 0 0                6 9 5 4 1 7 3 8 2

A well constructed Su Doku puzzle has a unique solution and can be solved by
logic, although it may be necessary to employ "guess and test" methods in order
to eliminate options (there is much contested opinion over this). The
complexity of the search determines the difficulty of the puzzle; the example
above is considered easy because it can be solved by straight forward direct
deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'),
contains fifty different Su Doku puzzles ranging in difficulty, but all with
unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the
top left corner of each solution grid; for example, 483 is the 3-digit number
found in the top left corner of the solution grid above.
"""

grid = """003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300"""

solved_grid = """483921657
967345821
251876493
548132976
729564138
136798245
372689514
814253769
695417382"""


with open('../txt_files/p096_sodoku.txt', 'r') as f:
    l = [line.strip('\n') for line in f.readlines()]
    sodokus = [[[int(c) for c in n] for n in l[(i*10)+1:(i*10)+10]] for i in range(len(l)//10)]

g = grid.split('\n')
s = solved_grid.split('\n')


sodoku = [[int(n) for n in l] for l in grid.split('\n')]
print(sodoku)
from collections import Counter

class Sodoku:
    ALL = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def __init__(self, board, dict = None):
        self.board = board
        self.num_zeros = sum(sum(1 for n in l if n == 0) for l in self.board)
        if dict is not None:
            self.d = dict
        else:
            all_set = {i+1 for i in range(9)}
            self.d = {(r, c): {i+1 for i in range(9)}
                      for r in range(9) for c in range(9) if self.board[r][c] == 0}

            for r in range(9):
                for c in range(9):
                    if self.board[r][c] > 0:
                         # print(self.board)
                         self.dict_update(r, c, self.board[r][c])

            # print(self.d)
            # print(self)

    def dictionary_update(self):
        for k, v in self.d.items():
            if len(v) == 1:
                self.board[k[0]][k[1]] = v

    def __str__(self):

        header = "  S   O   D   O   K   U  "
        top_border = "╔═══════╦═══════╦═══════╗"
        mid_border = "╠═══════╬═══════╬═══════╣"
        bot_border = "╚═══════╩═══════╩═══════╝"
        top_boxes = "\n".join(
            "║ {} {} {} ║ {} {} {} ║ {} {} {} ║".format(*self.row(l))
            for l in range(0, 3))
        mid_boxes = "\n".join(
            "║ {} {} {} ║ {} {} {} ║ {} {} {} ║".format(*self.row(l))
            for l in range(3, 6))
        bot_boxes = "\n".join(
            "║ {} {} {} ║ {} {} {} ║ {} {} {} ║".format(*self.row(l))
            for l in range(6, 9))
        strings = [
            header, top_border, top_boxes, mid_border, mid_boxes, mid_border,
            bot_boxes, bot_border
        ]
        return "\n".join(strings)

    def row(self, n):
        return self.board[n]

    def rowset(self, n):
        # thing = {self.d[(n, i)] for i in range(9) if len(self.d[(n, i)]) == 1}
        a = {*self.board[n]}
        # print(thing, a)
        return a

    def col(self, n):
        return [self.board[r][n] for r in range(9)]

    def colset(self, n):
        # return {self.board[r][n] for r in range(9)}
        return {*self.col(n)}

    def box(self, r, c):
        # if r > 2:
        r //= 3
        # if c > 2:
        c //= 3

        box = [self.row(i)[c * 3:3+(c*3)] for i in range(r*3, (r*3) + 3)]

        # print(box)
        return box


    def boxset(self, r, c):
        box =  self.box(r, c)
        return {n for sublist in box for n in sublist if n > 0}

    def cell_possibilities(self, r, c):
        if self.board[r][c] == 0:
            rowset = self.rowset(r)
            colset = self.colset(c)
            boxset = self.boxset(r, c)
            pos = ({i for i in range(10)} - set.union(colset, rowset, boxset))
            return pos

        else:
            return set(self.board[r][c])

    @staticmethod
    def box_inds(r, c):
        r //= 3
        c //= 3
        return {(i, j)
                for i in range((r * 3), (r * 3) + 3)
                for j in range((c * 3), (c * 3) + 3)}

    @staticmethod
    def row_inds(r):
        return {(r, j) for j in range(9)}

    @staticmethod
    def col_inds(c):
        return {(i, c) for i in range(9)}

    @staticmethod
    def affected_inds(r, c):
        boxbuds = Sodoku.box_inds(r, c)
        rowbuds = Sodoku.row_inds(r)
        colbuds = Sodoku.col_inds(c)
        return set.union(boxbuds, rowbuds, colbuds)

    def dict_update(self, r, c, val):
        check = Sodoku.affected_inds(r, c).intersection(self.d.keys())
        for cell in check:
            if cell in self.d and len(self.d[cell])>0:
                if val in self.d[cell]:
                    self.d[cell].remove(val)

    def set_cell(self, r, c, val):
        del self.d[(r, c)]
        self.board[r][c] = val
        self.dict_update(r, c, val)

    def reduce_dictionary(self):
        # print(any(1 == len(v) for k, v in self.d.items()))
        while any(1 == len(v) for k, v in self.d.items()):
            for k in list(self.d.keys()):
                if k in self.d:
                    if len(self.d[k]) == 1:
                        val = self.d[k].pop()
                        self.set_cell(*k, val)

            self.d = {k: v for k, v in self.d.items() if len(v) > 0} # clean up the dictionary of empty sets

            for i in range(3):
                for j in range(3):
                    boxinds = self.box_inds(i, j).intersection(self.d.keys())
                    couttttt = self.box_cell_count(boxinds)
                    for k, v in couttttt.items():
                        if v == 1:
                            for ind in boxinds:
                                if ind in self.d and k in self.d[ind]:
                                    # print(ind, self.d[ind])
                                    self.set_cell(*ind, k)
                                    self.reduce_dictionary()
                        if v == 2:
                            # print("TOOOOOO")
                            # print(k, v)
                            xxx = set()
                            yyy = set()
                            for ind in boxinds:
                                if ind in self.d and k in self.d[ind]:
                                    xxx.add(ind[0])
                                    yyy.add(ind[1])
                                    # print(ind, self.d[ind])
                                    # self.set_cell(*ind, k)
                                    # self.reduce_dictionary()
                            # print(xxx, yyy)
                            if len(xxx) == 1:
                                # print(xxx)
                                thing = self.row_inds(xxx.pop()).intersection(self.d.keys()) - boxinds
                                for cell in thing:
                                    if cell in self.d and len(self.d[cell])>0:
                                        if k in self.d[cell]:
                                            self.d[cell].remove(k)
                            if len(yyy) == 1:
                                # print(yyy)
                                thing = self.col_inds(yyy.pop()).intersection(self.d.keys()) - boxinds
                                for cell in thing:
                                    if cell in self.d and len(self.d[cell])>0:
                                        if k in self.d[cell]:
                                            self.d[cell].remove(k)

    def box_cell_count(self, inds):
        ccc = Counter()
        for ind in inds:
            if ind in self.d:
                for n in self.d[ind]:
                    ccc[n] += 1

        return ccc

    def printcells(self):
        for c_row in range(3):
            for c_col in range(3):
                inds = self.box_inds(c_row, c_col).intersection(self.d.keys())
                self.box_cell_count(inds)

    @staticmethod
    def is_solved(board):
        must_be = {i+1 for i in range(9)}
        s = Sodoku(board)
        for r in range(9):
            if s.rowset(r) != must_be:
                return False
            if s.colset(r) != must_be:
                return False
        for r in range(3):
            for c in range(3):
                if s.boxset(r, c) != must_be:
                    return False
        return True



    def solve(self):
        self.reduce_dictionary()
        if Sodoku.is_solved(self.board):
            print("SOLUTION FOUND")
            # print(self)
        else:
            print("NO SOLVE YET")
            print(self)
            print(self.d)

        return self.board
            # cell, p = self.d.popitem()
            # for k, v in self.d.items():
            #     for poss in v:
            #         print(self)
            #         print(cell, p)
            #         pboard = [row[:] for row in self.board]
            #         pboard[cell[0]][cell[1]] = poss
            #         ssss = Sodoku(pboard, self.d.copy())
            #         ssss.solve()
            #         aaaa= Sodoku.is_solved(pboard)
            #         # print(ssss)
            #         if len(ssss.d) == 0:
            #             return ssss.board


            # potential = Sodoku(self.board, self.d)

s1 = Sodoku(sodoku)
print("___")
# print(s1.row(1))
# print(s1.col(1))
# print(s1.box(0, 0))
# print(s1.boxset(0, 0))
# print(s1)
s1.solve()
print(s1)

ssss = Sodoku(sodokus[1])
ssss.solve()
print(ssss)
cccccoutnter = 0
for i in range(len(sodokus)-20):
    cccccoutnter += 1
    print("puzzle num ", cccccoutnter)
    ssss = Sodoku(sodokus[i])
    print(ssss)
    ssss.solve()
    print(ssss)
