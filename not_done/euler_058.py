#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Spiral primes
Problem 58
Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the
side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?
"""

from lib.octopus_prime import is_prime

class Grid(object):
    def __init__(self, size):
        self.sum_diags = 1
        self.size = size
        self.center_xy = size // 2
        self.nw_diag = set([(i, i) for i in range(self.center_xy)])
        self.se_diag = set([(i, i)
                            for i in range(self.center_xy + 1, self.size)])
        self.ne_diag_real = set([(i, self.size - i - 1)
                                 for i in range(self.center_xy)])
        self.ne_diag = set([(i, self.size - i)
                            for i in range(self.center_xy)])
        self.sw_diag = set([(self.size - i - 1, i)
                            for i in range(self.center_xy)])
        if self.size > 3:
            self.ne_diag.remove((0, self.size))

        self.op_diag = list((self.size - i -1, i) for i in range(self.size))
        self.main_diag = list((i, i) for i in range(self.size))
        self.all_diag_coords = set(self.main_diag + self.op_diag)
        self.array = Grid.make_grid(size)
        self.direction = 1
        self.diags_sum = 0
        self.diag_numbers = set()
        self.num_diag_nums = 2*self.size - 1
        self.spiral()


    def grid_info(self):
        rows = [str(row) for row in self.array]
        rows.append("num numbers on diag: {}".format(self.num_diag_nums))
        rows.append("diags: {}".format(self.diag_numbers))
        rows.append("diag coords: {}".format(self.all_diag_coords))
        print("\n".join(rows))

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

    def diag_primes(self):
        num_diag_primes = [self.array[coord[0]][coord[1]] for coord in self.all_diag_coords]
        hermy = sum(1 for num in num_diag_primes if is_prime(num)) -1
        ratio = hermy / self.num_diag_nums
        return ratio

# grid3 = Grid(3)
# grid3.grid_info()
#
#
# grid7 = Grid(7)
# grid7.grid_info()
# grid7.diag_primes()

ratio = 0.62
i = 3
while(ratio > 0.10):
    grid = Grid(i)
    ratio = grid.diag_primes()
    i += 2

print(i)
