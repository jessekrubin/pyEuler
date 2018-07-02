#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - py_euler
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
logic, although it may be necessary to employ "guess and test_pupy" methods in order
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

from pupy.sodoku import Sodoku
from pupy.listless import chunks


def sol3d(grid):
    print(grid[0])
    s = Sodoku("".join(grid[1:]))
    s.solve()
    print(s.board)
    return int(s.board[0:3])


def p096():
    with open('../txt_files/p096_sodoku.txt', 'r') as f:
        f_lines = [line.strip('\n') for line in f.readlines()]
    sodoku_boards = [chunk for chunk in chunks(f_lines, 10)]
    return sum(Sodoku("".join(s[1:])).euler_096_three_digit_number()
               for s in sodoku_boards)
    # for s in sodokus:
    #     print(s)


if __name__ == '__main__':
    unsolved = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
    solved = '483921657967345821251876493548132976729564138136798245372689514814253769695417382'
    test_sodoku = Sodoku(unsolved)
    test_sodoku.solve()
    assert test_sodoku.get_oneline_str() == solved
    ANSWER = p096()
    print("3-DIGIT NUMBERS SUM: {}".format(ANSWER))