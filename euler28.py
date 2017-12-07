#!/usr/bin/env python
# Jesse Rubin - project Euler

# Number spiral diagonals
# Problem 28
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

import numpy as np
from itertools import cycle


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
