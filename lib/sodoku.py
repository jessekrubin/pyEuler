#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - py_euler
from collections import Counter
from lib.listless import chunks
from math import sqrt


class SodokuError(ValueError):
    def __init__(self, message, row=None, col=None):
        self.message = message
        self.row, self.col = row, col
        super(SodokuError, self).__init__(message, row, col)

class Sodoku(object):
    ALL = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def __init__(self, board):
        self.board = board
        self.size = len(board)
        self.n_empty = sum(sum(1 for n in l if n == 0) for l in self.board)
        self.d = {(r, c):self.cell_possibilities(r, c)
                  for r in range(self.size)
                  for c in range(self.size)
                  if self.board[r][c] == 0}


    @classmethod
    def from_multiline_string(strang):
        print(strang)

    @classmethod
    def from_oneline_str(cls, strang):
        s = strang.replace('.', '0')
        board_size = int(sqrt(len(s)))
        return Sodoku(board = [chunk for chunk in chunks([int(n) for n in s], board_size)])

    def get_oneline_str(self):
        return "".join(("".join(str(n) for n in row) for row in self.board))

    def __str__(self):
        return "\n".join(str(l) for l in self.board)

    def row(self, n):
        return self.board[n]

    def rowset(self, n):
        # thing = {self.d[(n, i)] for i in range(9) if len(self.d[(n, i)]) == 1}
        # noinspection Annotator
        a = {*self.board[n]}
        # print(thing, a)
        return a

    def col(self, n):
        return [self.board[r][n] for r in range(9)]

    def colset(self, n):
        # return {self.board[r][n] for r in range(9)}
        # noinspection Annotator
        return {*self.col(n)}

    def box(self, r, c):
        # if r > 2:
        r //= 3
        # if c > 2:
        c //= 3

        box = [self.row(i)[c * 3:3 + (c * 3)] for i in range(r * 3, (r * 3) + 3)]

        # print(box)
        return box

    def boxset(self, r, c):
        box = self.box(r, c)
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

    def dictionary_update(self):
        for k, v in self.d.items():
            if len(v) == 1:
                self.board[k[0]][k[1]] = v

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
            if cell in self.d and len(self.d[cell]) > 0:
                if val in self.d[cell]:
                    self.d[cell].remove(val)

    def set_cell(self, r, c, val):
        del self.d[(r, c)]
        self.board[r][c] = val
        self.dict_update(r, c, val)

    def reduce_dictionary(self):
        while any(1 == len(v) for k, v in self.d.items()):
            for k in list(self.d.keys()):
                if k in self.d:
                    if len(self.d[k]) == 1:
                        val = self.d[k].pop()
                        # noinspection Annotator
                        self.set_cell(*k, val)

            self.d = {k: v for k, v in self.d.items() if len(v) > 0}  # clean up the dictionary of empty sets

            for i in range(3):
                for j in range(3):
                    boxinds = self.box_inds(i, j).intersection(self.d.keys())
                    couttttt = self.box_cell_count(boxinds)
                    for k, v in couttttt.items():
                        if v == 1:
                            for ind in boxinds:
                                if ind in self.d and k in self.d[ind]:
                                    # print(ind, self.d[ind])
                                    # noinspection Annotator
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
                                    if cell in self.d and len(self.d[cell]) > 0:
                                        if k in self.d[cell]:
                                            self.d[cell].remove(k)
                            if len(yyy) == 1:
                                # print(yyy)
                                thing = self.col_inds(yyy.pop()).intersection(self.d.keys()) - boxinds
                                for cell in thing:
                                    if cell in self.d and len(self.d[cell]) > 0:
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
        must_be = {i + 1 for i in range(9)}
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
        if (self.size**2)-self.n_empty <= 16:
            # raise ValueError("Not enough info to solve")
            raise SodokuError("Not enough info to solve")
        self.reduce_dictionary()
        print(self.board)
        if Sodoku.is_solved(self.board):
            return self.board
        # else:
        #     print("NO SOLVE YET")
        #     print(self)
        #     print(self.d)

        # return self.board
        # cell, pytriple_gen = self.d.popitem()
        # for k, v in self.d.items():
        #     for poss in v:
        #         print(self)
        #         print(cell, pytriple_gen)
        #         pboard = [row[:] for row in self.board]
        #         pboard[cell[0]][cell[1]] = poss
        #         ssss = Sodoku(pboard, self.d.copy())
        #         ssss.solve()
        #         aaaa= Sodoku.is_solved(pboard)
        #         # print(ssss)
        #         if len(ssss.d) == 0:
        #             return ssss.board

        # potential = Sodoku(self.board, self.d)

