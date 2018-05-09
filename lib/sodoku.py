#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - py_euler
from lib.decorations import cash_muney
from itertools import chain


class SodokuError(ValueError):

    def __init__(self, message, row=None, col=None):
        self.message = message
        self.row, self.col = row, col
        super(SodokuError, self).__init__(message, row, col)


class Sodoku(object):

    def __init__(self, board):
        self.board = board
        self.solutions = []
        self.nz = [i for i in range(81) if board[i] != '0']
        self.z = [i for i in range(81) if board[i] == '0']

    def solve(self):
        if 17 > sum(1 for n in self.board if n != '0'):
            raise SodokuError("not enough info")
        full_set = '123456789'
        d = {i:("".join(c for c in full_set)
                if self.board[i] == '0'
                else self.board[i])
             for i in range(81)}
        d = Sodoku.update_dictionary(d)
        tf, d = Sodoku.reduce_dictionary(d)
        if tf == False:
            raise SodokuError("hidden_singles")

        print(d)
        a = [d[ind] for ind in range(81)]
        print("".join(a))

        self.board = "".join(a)

    @staticmethod
    def first_unknown(d):
        for i in range(81):
            if len(d[i]) > 1:
                return i

    # @staticmethod
# def hidden_singles(d):
#     for boxr in range(3):
#         for boxc in range(3):
#             hs = {str(n):{ind for ind in Sodoku.box_inds(boxr, boxc)
#                           if ind in d and str(n) in d[ind]}
#                   for n in range(1, 10)}
#             # print(hs)
#             for num, inds in hs.items():
#                 if len(inds) == 1:
#                     nd = {k:v for k, v in d.items()}
#                     nd[inds.pop()] = num
#                     return nd
    @staticmethod
    def unsolvable(rcbd):
        return any(len(v)==0 for v in rcbd.values())
        # print("RCB")
        # print(rcbd)


    @staticmethod
    def hidden_singles(d):
        nd = {k:v for k, v in d.items()}
        for rcb in range(9):
            box = {str(n):[ind for ind in Sodoku.box_inds(*divmod(rcb, 3))
                           if str(n) in d[ind]]
                   for n in range(1, 10)}
            row = {str(n):[ind for ind in Sodoku.row_inds(rcb)
                           if str(n) in d[ind]]
                   for n in range(1, 10)}
            col = {str(n):[ind for ind in Sodoku.col_inds(rcb)
                           if str(n) in d[ind]]
                   for n in range(1, 10)}
            if Sodoku.unsolvable(box) or Sodoku.unsolvable(row) or Sodoku.unsolvable(col):
                raise SodokuError("UNSOLVABLE")
            print(Sodoku.unsolvable(row))
            print(Sodoku.unsolvable(col))
            #
            # print("___")
            # print(rcb)
            # print(col)
            # print(box)
            # print(row)
            # if any(len(v)==0 for v in chain(box.values(), row.values(), col.values())):
        return nd

    @staticmethod
    def update_dictionary(d):
        nd = {k:v for k, v in d.items()}
        for i in range(81):
            if len(nd[i]) == 1:
                for nay in Sodoku.neighbors(i):
                    if len(nd[nay]) != 1 and nd[i] in nd[nay]:
                        nd[nay] = nd[nay].replace(nd[i], '')
        return nd

    @staticmethod
    def reduce_dictionary(d):
        if all(len(v) == 1 for v in d.values()):
            return True, d
        d = Sodoku.hidden_singles(d)
        d = Sodoku.update_dictionary(d)

        if any(len(v) == 0 for k, v in d.items()):
            # raise SodokuError("UNSOLVABLE")
            return False, d
        print(any(len(v) == 0 for k, v in d.items()))
        print(d)
        fz = Sodoku.first_unknown(d)
        if fz is None:
            if Sodoku.hasdup(d): return False, d
            return Sodoku.reduce_dictionary(d)
        for poss in d[fz]:
            nd = {k:v for k, v in d.items()}
            nd[fz] = str(poss)
            if not Sodoku.hasdup(nd):
                valid, ret = Sodoku.reduce_dictionary(nd)
                if valid:
                    return valid, ret
        return False, d

    @staticmethod
    def hasdup(d):
        for i in range(81):
            if len(d[i]) == 1:
                for n in Sodoku.neighbors(i):
                    if d[n] == d[i]:
                        return True
        return False

    @classmethod
    def from_oneline_str(cls, strang):
        s = strang.replace('.', '0')
        # return Sodoku(board=[n for n in s])
        return Sodoku(board=strang.replace('.', '0'))

    def get_oneline_str(self):
        return self.board

    @staticmethod
    @cash_muney
    def neighbors(index, size=9):
        return {ni for ni in chain(Sodoku.row_inds(index//size),
                                   Sodoku.col_inds(index%size),
                                   Sodoku.cell_box(index))}-{index}

    @staticmethod
    @cash_muney
    def row_inds(n, bsize=9):
        return {i for i in range(n*bsize, n*bsize+bsize)}

    @staticmethod
    @cash_muney
    def col_inds(n, bsize=9):
        return {i for i in range(n, bsize**2, bsize)}

    @staticmethod
    # @cash_muney
    def box_inds(box_r, box_c, bsize=9):
        return {i*bsize+j
                for i in range((box_r*3), (box_r*3)+3)
                for j in range((box_c*3), (box_c*3)+3)}

    @staticmethod
    @cash_muney
    def cell_box(index, bsize=9):
        for box_r in range(3):
            for box_c in range(3):
                box = Sodoku.box_inds(box_r, box_c)
                if index in box:
                    return box


# test_board = '256489173'\
#              '374615982'\
#              '981723456'\
#              '593274861'\
#              '7128.6549'\
#              '468591327635147298127958634849362715'
# test_solution = '256489173374615982981723456593274861712836549468591327635147298127958634849362715'
#
# s = Sodoku.from_oneline_str(test_board)
# s.solve()
#
# print(Sodoku.neighbors(40))
# [ 0,  1,  2,  3,  4,  5,  6,  7,  8]
# [ 9, 10, 11, 12, 13, 14, 15, 16, 17]
# [18, 19, 20, 21, 22, 23, 24, 25, 26]
# [27, 28, 29, 30, 31, 32, 33, 34, 35]
# [36, 37, 38, 39, 40, 41, 42, 43, 44]
# [45, 46, 47, 48, 49, 50, 51, 52, 53]
# [54, 55, 56, 57, 58, 59, 60, 61, 62]
# [63, 64, 65, 66, 67, 68, 69, 70, 71]
# [72, 73, 74, 75, 76, 77, 78, 79, 80]

# assert set([30, 31, 32]+[39, 41]+[48, 49, 50]+[4, 13, 22, 31, 49, 58, 67, 76]+[36, 37, 38, 39, 41, 42, 43,
#                                                                                44]) == Sodoku.neighbors(40)
#
# test_b = '....41....6.....2...2......32.6.........5..417.......2......23..48......5.1..2...'
# sodo = Sodoku.from_oneline_str(test_b)
# sodo.solve()
#
# test_board = '..2.3...8.....8....31.2.....6..5.27..1.....5.2.4.6..31....8.6.5.......13..531.4..'
# test_solution = '672435198549178362831629547368951274917243856254867931193784625486592713725316489'
# assert len(test_board) == len(test_solution)
# s = Sodoku.from_oneline_str(test_board)
# s.solve()
# s_solved = s.get_oneline_str()
# print(s_solved)
