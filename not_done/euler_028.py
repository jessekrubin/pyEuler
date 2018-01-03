#!/usr/bin/env python

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


class grid(object):
    def __init__(self, size):
        self.size = size
        self.array = grid.make_grid(size)
        self.center_xy = size // 2
        self.nw_diag = [(i, i) for i in range(self.center_xy)]
        self.se_diag = [(i, i) for i in range(self.center_xy + 1, self.size)]
        self.ne_diag = [(i, self.size - i - 1) for i in range(self.center_xy)]
        self.sw_diag = [(self.size - i - 1, i) for i in range(self.center_xy)]
        # print(self.nw_diag)
        # print(self.ne_diag)
        # print(self.se_diag)
        # print(self.sw_diag)
        self.spiral()

    @staticmethod
    def make_grid(size):
        retlist = []
        for i in range(size):
            retlist.append([size * (i) + (j) for j in range(size)])
        return retlist

    def spiral_step(self, current):
        return current

    def spiral(self):
        print(self.__str__())
        cur_xy = (self.center_xy, self.center_xy)
        for i in range(self.size**2):
            self.array[cur_xy[0]][cur_xy[1]] = 1
            cur_xy = self.spiral_step(cur_xy)
        print(self.__str__())

    def __str__(self):
        return "".join([str(line) + "\n" for line in self.array])


grid5 = grid(5)
print(grid5)
size = 5


def east(x, y):
    return x + 1, y


def south(x, y):
    return x, y - 1


def west(x, y):
    return x - 1, y


def north(x, y):
    return x, y + 1


dirs = [east, south, west, north]


def spiral_coords(end):
    from itertools import cycle
    _moves = cycle(dirs)
    n = 1
    pos = 0, 0
    times_to_move = 1
    squid = []
    poss = []

    while True:
        squid.append(n)
        poss.append(pos)
        for _ in range(2):
            move = next(_moves)
            for _ in range(times_to_move):
                if n >= end:
                    return
                pos = move(*pos)
                n += 1
        times_to_move += 1

    print(squid)
    print(poss)
    return squid


print(spiral_coords(25))


def main():
    thingy = spiral_coords(25)
    print(thingy)


if __name__ == "__main__":
    main()
