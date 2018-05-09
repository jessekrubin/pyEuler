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


# class Sodoku(object):


from lib.listless import chunks
from lib.decorations import cash_muney

from itertools import chain
from collections import defaultdict


class Sodoku(object):

    def __init__(self, board, check_duplicates=True):
        self.board = board
        self.SIZE = int(len(board)**(0.5))
        self.size = int(self.SIZE**(0.5))
        self.ID = {i for i in range(1, self.SIZE+1)}
        self.NEIGH = self.make_neighbors_dict(self.SIZE)
        self.ROW = {i:set(self.get_row(i)) for i in range(9)}
        self.COL = {i:set(self.get_col(i)) for i in range(9)}
        self.BOX = {i:set(self.get_box(i)) for i in range(9)}
        self.BOXID = {ind:i for i in range(9) for ind in Sodoku.box_inds(i)}
        if check_duplicates: self.check_duplicates()
        # self.D = {i:{j for j in range(1, 10)}-{board[e] for e in self.NEIGH[i]}
        #           for i in range(self.SIZE*self.SIZE)
        #           if self.board[i] == 0}
        self.D = {}

    def possibilities(self, ind):
        taken = set.union(self.BOX[self.BOXID[ind]],
                          self.ROW[ind//self.SIZE],
                          self.COL[ind%self.SIZE])
        p = {i for i in range(1, self.SIZE+1)}-taken
        return p
        # if len(p) == 0 and self.board[ind]==0:
        #     raise SodokuError("NO POSSIBILITIES AT INDEX: {}".format(ind))
        # return p

    def hidden_singles(self):
        for boxi in range(9):
            self.box_hidden_singles(boxi)

    def box_hidden_singles(self, boxi):
        remaining = (set(i for i in range(1, self.SIZE+1))-set(self.BOX[boxi]))
        print(" ")
        print("BOX", boxi)
        print(self.BOX)
        print(self.BOX[boxi])
        print(self.D)
        n_row = {i:{ib//self.SIZE for ib in Sodoku.box_inds(boxi)
                    if ib in self.D and i in self.D[ib]}
                 for i in remaining}

        n_cols = {i:{ib%self.SIZE for ib in Sodoku.box_inds(boxi)
                     if ib in self.D and i in self.D[ib]}
                  for i in remaining}
        # for i in range(1, 10) if i not in self.BOX[boxi]}
        # print(remaining)
        # print(n_row)
        # print(n_cols)
        # print("HIDDEN SINGLE")
        for n in remaining:
            if len(n_cols[n]) == 1 and len(n_row[n]) == 1:
                # print(n_row[n], n_cols[n])
                self.set_cell(n_row[n].pop(), n_cols[n].pop(), n)

            elif len(n_cols[n]) == 1 and len(n_row[n]) != 1:
                # print(n_cols[n])
                self.COL[n_cols[n].pop()].add(n)
                self.update_dictionary()
            elif len(n_cols[n]) != 1 and len(n_row[n]) == 1:
                self.ROW[n_cols[n].pop()].add(n)
                self.update_dictionary()
                # self.set_cell()

    def set_cell(self, r, c, value):
        # ind = (rowcol[0]*self.SIZE)+rowcol[1] if type(rowcol)==tuple else rowcol
        ind = self.SIZE*r+c
        self.board[ind] = value
        bi = self.BOXID[ind]
        print("")
        print("setval", value)
        print("r, c, ind, boxin", r, c, ind, bi)
        if ind in self.D:
            del self.D[ind]
        self.ROW[r].add(value)
        self.COL[c].add(value)
        self.BOX[bi].add(value)

        # singles = {k:v for k, v in self.D.items() if len(v)==1}
        # self.update_dictionary()
        # singles = {k:v for k, v in self.D.items() if len(v)==1}
        # for i in range(self.SIZE**2):
        #     if i in self.D and len(self.D[i])==1:
        #         nrow, ncol = divmod(i, self.SIZE)
        #         self.set_cell(nrow, ncol, self.D[i].pop())

        self.update_dictionary()

        # print(singles)
        # for n, nset in self.D.items():
        #     if len(nset) == 1:bnm

        # new = self.update_dictionary()
        # for k in self.D:
        #     if self.D[k] != new[k]:
        #         print("YEAH FUCK")
        #         print(self.D[k])
        #         print(new[k])
        # self.D = new

        # print(len(self.D))

    # def update_dictionary(self):
    #     return {index:self.possibilities(index) for index in self.D.keys()}
    def update_dictionary(self):
        self.D = {index:self.possibilities(index)
                  for index in range(self.SIZE**2)
                  if self.board[index] == 0}


    def check_duplicates(self):
        for i in range(9):
            if len(self.ROW[i]) != len(self.get_row(i)): raise SodokuError("invalid row")
            if len(self.COL[i]) != len(self.get_col(i)): raise SodokuError("invalid col")
            if len(self.BOX[i]) != len(self.get_box(i)): raise SodokuError("invalid box")

    @staticmethosodoku.pyd
    def make_neighbors_dict(board_size):
        neighbors = defaultdict(set)
        for i in range(9):
            box = set(Sodoku.box_inds(i, board_size))
            for n in box:
                # self.NEIGH[n] = box-{n}
                neighbors[n].update(box-{n})

        for i in range(9):
            row = set(Sodoku.row_inds(i, board_size))
            for row_n in row:
                neighbors[row_n].update(row-{row_n})

        for i in range(9):
            col = set(Sodoku.col_inds(i, board_size))
            for col_number in col:
                neighbors[col_number].update(col-{col_number})

        return neighbors
        # self.NEIGH[col_number].update(e for e in set(j for j in col if j != col_number))

    @classmethod
    def from_oneline_str(cls, strang):
        s = strang.replace('.', '0')
        return Sodoku(board=[int(n) for n in s])

    def get_oneline_str(self):
        return "".join(str(n) for n in self.board)

    def get_row(self, r):
        return [e for e in self.board[r*9:r*9+9] if e != 0]

    def get_col(self, c):
        return [e for e in self.board[c:81:9] if e != 0]

    def get_box(self, b):
        return [self.board[i] for i in Sodoku.box_inds(b) if self.board[i] != 0]

    def prints(self):
        for r in chunks(self.board, 9):
            print(r)

    @staticmethod
    def is_solved(board):
        expected = set(i for i in range(1, 10))
        if sum(board) == 405:  # fast check
            return all(set(board[rc:81:9]) == expected and
                       set(board[rc*9:rc*9+9]) == expected and
                       set(board[i] for i in Sodoku.box_inds(rc)) == expected
                       for rc in range(9))
        return False

    def solve(self):
        self.D = {i:self.possibilities(i)
                  for i in range(self.SIZE*self.SIZE)
                  if self.board[i] == 0}

        print("solving")
        self.prints()
        nonzero = sum(1 for e in self.board if e != 0)

        # check if ther is enough information
        if nonzero <= 16: raise SodokuError("non enough info")

        if Sodoku.is_solved(self.board): return
        print(self.D)

        print([len(v) for v in self.D.values()])
        print([(v) for v in self.D.values()])
        while any(len(self.D[k])<2 for k in self.D):
            self.hidden_singles()
            # print(self.D)
            for i in range(self.SIZE**2):

                if i in self.D:
                    if len(self.D[i])==0 and self.board[i]>0:
                        del self.D[i]
                    if len(self.D[i])==1:
                        nrow, ncol = divmod(i, self.SIZE)
                        self.set_cell(nrow, ncol, self.D[i].pop())
                    # elif len(self.D[i])==0 and self.board[i]>0:
            self.update_dictionary()

        print("SOLVED???")
        print(self.D)
        self.prints()

        # start to do the recursing stuff

    # def __str__(self):
    #     return "\n".join(str(l) for l in self.arr)

    @staticmethod
    def row_inds(n, bsize=9):
        return [i for i in range(n*bsize, n*bsize+bsize)]

    @staticmethod
    def col_inds(n, bsize=9):
        return [i for i in range(n, bsize**2, bsize)]

    @staticmethod
    def box_inds(row_col, bsize=9):
        box_r, box_c = row_col if type(row_col) == tuple else divmod(row_col, 3)
        return [i*bsize+j
                for i in range((box_r*3), (box_r*3)+3)
                for j in range((box_c*3), (box_c*3)+3)]

    @staticmethod
    def cell_box_inds(cell_index, board_size=9):
        return Sodoku.box_inds(cell_index//board_size)

    # a = []
    # for r in range(3):
    #     for c in range(3):
    #         a.append(Sodoku.box_inds((r, c)))
    # for rc in range(9):
    #     print(divmod(rc, 3))
    #     Sodoku.box_inds(rc)
    #
    # ninenineboardsum = sum([i for i in range(1, 10)])*9
    # print(ninenineboardsum)

# [ 0,  1,  2,  3,  4,  5,  6,  7,  8]
# [ 9, 10, 11, 12, 13, 14, 15, 16, 17]
# [18, 19, 20, 21, 22, 23, 24, 25, 26]
# [27, 28, 29, 30, 31, 32, 33, 34, 35]
# [36, 37, 38, 39, 40, 41, 42, 43, 44]
# [45, 46, 47, 48, 49, 50, 51, 52, 53]
# [54, 55, 56, 57, 58, 59, 60, 61, 62]
# [63, 64, 65, 66, 67, 68, 69, 70, 71]
# [72, 73, 74, 75, 76, 77, 78, 79, 80]
