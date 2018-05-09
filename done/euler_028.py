#!/usr/bin/env python
# coding=utf-8
# Jesse Rubin - project Euler
"""
Number spiral diagonals
Problem 28
Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?
"""


class Grid(object):

    def __init__(self, size):
        self.sum_diags = 1
        self.size = size
        self.center_xy = size // 2
        self.nw_diag = set([(i, i) for i in range(self.center_xy)])
        self.se_diag = set([(i, i) for i in range(self.center_xy + 1, self.size)])
        self.ne_diag_real = set([(i, self.size - i - 1) for i in range(self.center_xy)])
        self.ne_diag = set([(i, self.size - i)
                            for i in range(self.center_xy)])
        self.sw_diag = set([(self.size - i - 1, i)
                            for i in range(self.center_xy)])
        if self.size > 3:
            self.ne_diag.remove((0, self.size))
        self.array = Grid.make_grid(size)
        self.direction = 1
        self.diags_sum = 0
        self.spiral()

    @staticmethod
    def make_grid(size):
        retlist = []
        for i in range(size):
            retlist.append([0 for _ in range(size)])
        return retlist

    def update_direction(self, x, y):
        if x == self.center_xy and y == self.center_xy + 1:
            self.direction = 0
        else:
            if (x, y) in self.se_diag:
                self.direction = 3
            if (x, y) in self.ne_diag:
                self.direction = 0
            if (x, y) in self.nw_diag:
                self.direction = 1
            if (x, y) in self.sw_diag:
                self.direction = 2

    def spiral_step(self, x, y):
        self.update_direction(x, y)
        if self.direction == 1:
            return self.west(x, y)
        if self.direction == 2:
            return self.south(x, y)
        if self.direction == 3:
            return self.east(x, y)
        if self.direction == 0:
            return self.north(x, y)

    def spiral(self):
        cur_x, cur_y = self.center_xy, self.center_xy
        for i in range(self.size ** 2):
            self.array[cur_x][cur_y] = i + 1
            cur_x, cur_y = self.spiral_step(cur_x, cur_y)

    def __str__(self):
        return "".join([str(line) + "\n" for line in self.array])

    @staticmethod
    def west(x, y):
        return x, y + 1

    @staticmethod
    def north(x, y):
        return x + 1, y

    @staticmethod
    def east(x, y):
        return x, y - 1

    @staticmethod
    def south(x, y):
        return x - 1, y

    def diag_sum(self):
        for coords in set.union(self.ne_diag_real, self.nw_diag, self.se_diag, self.sw_diag):
            self.sum_diags += self.array[coords[0]][coords[1]]
        return self.sum_diags


def p028():
    grid1001 = Grid(1001)
    return grid1001.diag_sum()


if __name__ == '__main__':
    grid3 = Grid(3)
    assert 25 == grid3.diag_sum()
    grid5 = Grid(5)
    assert 101 == grid5.diag_sum()
    ANSWER = p028()
    print("Answer: {}".format(ANSWER))