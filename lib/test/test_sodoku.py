#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - py_euler sodoku tests
"""
testing my sodoku solver

ty sudopedia
http://sudopedia.enjoysudoku.com/Invalid_Test_Cases.html
http://sudopedia.enjoysudoku.com/Valid_Test_Cases.html
"""

from lib.sodoku import Sodoku, SodokuError
from pytest import raises

class Test_SodokuMethods(object):
    def test_oneline_load_n_ret(self):
        b = '974236158638591742125487936316754289742918563589362417867125394253649871491873625'
        s = Sodoku.from_oneline_str(b)
        ret = s.get_oneline_str()
        assert ret == b

    # def test_get_row(self):




class Test_Not_Enough_Info(object):
    def test_empty_board(self):
        # empty board
        test_board= '.................................................................................'
        s = Sodoku.from_oneline_str(test_board)
        with raises(SodokuError):
            s.solve()

    def test_one_cell_given(self):
        # one cell
        test_board='........................................1........................................'
        s = Sodoku.from_oneline_str(test_board)
        with raises(SodokuError):
            s.solve()

    def test_lt16_cells_given(self):
        # less than 16 values
        test_board = '...........5....9...4....1.2....3.5....7.....438...2......9.....1.4...6..........'
        s = Sodoku.from_oneline_str(test_board)
        with raises(SodokuError):
            s.solve()

class Test_Duplicate(object):

    def test_duplicate_col(self):
        badcol='6.159.....9..1............4.7.314..6.24.....5..3....1...6.....3...9.2.4......16..'
        sbc = Sodoku.from_oneline_str(badcol)
        with raises(SodokuError):
            sbc.solve()

    def test_duplicate_row(self):
        badrow='.4.1..35.............2.5......4.89..26.....12.5.3....7..4...16.6....7....1..8..2.'
        sbr = Sodoku.from_oneline_str(badrow)
        with raises(SodokuError):
            sbr.solve()

    def test_duplicate_box(self):
        badbox = '..9.7...5..21..9..1...28....7...5..1..851.....5....3.......3..68........21.....87'
        sbb = Sodoku.from_oneline_str(badbox)
        with raises(SodokuError):
            sbb.solve()



class Test_Unsolvable(object):
    def test_row_unsolvable(self):
        pass
    def test_col_unsolvable(self):
        pass
    def test_box_unsolvable(self):
        pass
    def test_square_unsolvable(self):
        pass




class TestValidCases(object):
    def test_already_solved(self):
        b = '974236158638591742125487936316754289742918563589362417867125394253649871491873625'
        s = Sodoku.from_oneline_str(b)
        assert Sodoku.is_solved(s.board)

    def test_one_empty_square(self):
        test_board= '2564891733746159829817234565932748617128.6549468591327635147298127958634849362715'
        test_solution = '256489173374615982981723456593274861712836549468591327635147298127958634849362715'
        assert len(test_board) == len(test_solution)
        s = Sodoku.from_oneline_str(test_board)
        s.solve()
        assert s.get_oneline_str() == test_solution

    # def test_hidden_singles(self):
    #     test_board = '..2.3...8.....8....31.2.....6..5.27..1.....5.2.4.6..31....8.6.5.......13..531.4..'
    #     test_solution = '672435198549178362831629547368951274917243856254867931193784625486592713725316489'
    #     assert len(test_board) == len(test_solution)
    #     s = Sodoku.from_oneline_str(test_board)
    #     s.solve()
    #     assert test_solution == s.get_oneline_str()

    def test_naked_singles(self):
        test_board = '3.542.81.4879.15.6.29.5637485.793.416132.8957.74.6528.2413.9.655.867.192.965124.8'
        test_solution = '365427819487931526129856374852793641613248957974165283241389765538674192796512438'
        assert len(test_board) == len(test_solution)
        s = Sodoku.from_oneline_str(test_board)
        s.solve()
        assert test_solution == s.get_oneline_str()
