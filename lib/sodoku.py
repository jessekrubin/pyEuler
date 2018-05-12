#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - Biblioteca
from itertools import chain

from lib import xrange
from lib.decorations import cash_it


class SodokuError(ValueError):
    """

    """

    def __init__(self, message, row=None, col=None):
        self.message = message
        self.row, self.col = row, col
        super(SodokuError, self).__init__(message, row, col)


class Sodoku(object):
    """Sodoku class

    [ 0,  1,  2,  3,  4,  5,  6,  7,  8]
    [ 9, 10, 11, 12, 13, 14, 15, 16, 17]
    [18, 19, 20, 21, 22, 23, 24, 25, 26]
    [27, 28, 29, 30, 31, 32, 33, 34, 35]
    [36, 37, 38, 39, 40, 41, 42, 43, 44]
    [45, 46, 47, 48, 49, 50, 51, 52, 53]
    [54, 55, 56, 57, 58, 59, 60, 61, 62]
    [63, 64, 65, 66, 67, 68, 69, 70, 71]
    [72, 73, 74, 75, 76, 77, 78, 79, 80]
    """

    def __init__(self, board):
        self.is_solved = False
        self.board = board.replace('.', '0')

    def solve(self):
        """

        """
        if 17 > sum(1 for n in self.board if n != '0'):
            raise SodokuError("not enough info")
        full_set = '123456789'
        d = {i:("".join(c for c in full_set)
                if self.board[i] == '0'
                else self.board[i])
             for i in xrange(81)}
        d = Sodoku.update_dictionary(d)
        tf, d = Sodoku.reduce_dictionary(d)
        if not tf:
            raise SodokuError("check_unsolvable")
        a = [d[ind] for ind in xrange(81)]
        self.board = "".join(a)
        self.is_solved = True

    def euler_096_three_digit_number(self):
        """

        Returns:

        """
        if not self.is_solved:
            self.solve()
        return int(self.board[0:3])

    @staticmethod
    def first_unknown(d):
        """

        Args:
            d:

        Returns:

        """
        for i in xrange(81):
            if len(d[i]) > 1:
                return i

    @staticmethod
    def unsolvable(rcbd):
        """

        Args:
            rcbd:

        Returns:

        """
        return any(len(v) == 0 for v in rcbd.values())

    @staticmethod
    def check_unsolvable(d):
        """

        Args:
            d:

        Returns:

        """
        nd = {k:v for k, v in d.items()}
        for rcb in xrange(9):
            box = {str(n):[ind for ind in Sodoku.box_inds(*divmod(rcb, 3))
                           if str(n) in d[ind]]
                   for n in xrange(1, 10)}
            row = {str(n):[ind for ind in Sodoku.row_inds(rcb)
                           if str(n) in d[ind]]
                   for n in xrange(1, 10)}
            col = {str(n):[ind for ind in Sodoku.col_inds(rcb)
                           if str(n) in d[ind] or str(n) == d[ind]]
                   for n in xrange(1, 10)}
            if Sodoku.unsolvable(box) or Sodoku.unsolvable(row) or Sodoku.unsolvable(col):
                raise SodokuError("UNSOLVABLE")
        return nd

    @staticmethod
    def update_dictionary(d):
        """

        Args:
            d:

        Returns:

        """
        nd = {k:v for k, v in d.items()}
        for i in xrange(81):
            if len(nd[i]) == 1:
                for nay in Sodoku.neighbors(i):
                    if len(nd[nay]) != 1 and nd[i] in nd[nay]:
                        nd[nay] = nd[nay].replace(nd[i], '')
        return nd

    @staticmethod
    def reduce_dictionary(d):
        """

        Args:
            d:

        Returns:

        """
        if all(len(v) == 1 for v in d.values()):
            return True, d
        try:
            d = Sodoku.check_unsolvable(d)
        except SodokuError:
            return False, d
        d = Sodoku.update_dictionary(d)
        if any(len(v) == 0 for k, v in d.items()):
            return False, d
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

    # def __str__(self):
    #
    #     header = "  S   O   D   O   K   U  "
    #     top_border = "╔═══════╦═══════╦═══════╗"
    #     mid_border = "╠═══════╬═══════╬═══════╣"
    #     bot_border = "╚═══════╩═══════╩═══════╝"
    #     top_boxes = "\n".join(
    #             "║ {} {} {} ║ {} {} {} ║ {} {} {} ║".format(*self.row(l))
    #             for l in range(0, 3))
    #     mid_boxes = "\n".join(
    #             "║ {} {} {} ║ {} {} {} ║ {} {} {} ║".format(*self.row(l))
    #             for l in range(3, 6))
    #     bot_boxes = "\n".join(
    #             "║ {} {} {} ║ {} {} {} ║ {} {} {} ║".format(*self.row(l))
    #             for l in range(6, 9))
    #     strings = [
    #         header, top_border, top_boxes, mid_border, mid_boxes, mid_border,
    #         bot_boxes, bot_border
    #         ]
    #     return "\n".join(strings)
    @staticmethod
    def hasdup(d):
        """

        Args:
            d:

        Returns:

        """
        for i in xrange(81):
            if len(d[i]) == 1:
                for n in Sodoku.neighbors(i):
                    if d[n] == d[i]:
                        return True
        return False

    def get_oneline_str(self):
        """

        Returns:

        """
        return self.board

    @staticmethod
    def neighbors(index, size=9):
        """

        Args:
            index:
            size:

        Returns:

        """
        return {ni for ni in chain(Sodoku.row_inds(index//size),
                                   Sodoku.col_inds(index%size),
                                   Sodoku.cell_box(index))}-{index}

    @staticmethod
    def row_inds(n, bsize=9):
        """

        Args:
            n:
            bsize:

        Returns:

        """
        return {i for i in xrange(n*bsize, n*bsize+bsize)}

    @staticmethod
    def col_inds(n, bsize=9):
        """

        Args:
            n:
            bsize:

        Returns:

        """
        return {i for i in xrange(n, bsize**2, bsize)}

    @staticmethod
    def box_inds(box_r, box_c, bsize=9):
        """

        Args:
            box_r:
            box_c:
            bsize:

        Returns:

        """
        return {i*bsize+j
                for i in xrange((box_r*3), (box_r*3)+3)
                for j in xrange((box_c*3), (box_c*3)+3)}

    @staticmethod
    @cash_it
    def cell_box(index, bsize=9):
        """

        Args:
            index:
            bsize:

        Returns:

        """
        for box_r in xrange(3):
            for box_c in xrange(3):
                box = Sodoku.box_inds(box_r, box_c)
                if index in box:
                    return box