#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Counting block combinations I
Problem 114
A row measuring seven units in length has red blocks with a minimum length of
three units placed on it, such that any two red blocks (which are allowed to
be different lengths) are separated by at least one black square. There are
exactly seventeen ways of doing this.

(1, 1, 1, 1, 1, 1, 1),
(3, 1, 1, 1, 1), (1, 3, 1, 1, 1), (1, 1, 3, 1, 1), (1, 1, 1, 3, 1),
(1, 1, 1, 1, 3), (3, 1, 3),
(4, 1, 1, 1), (1, 4, 1, 1), (1, 1, 4, 1), (1, 1, 1, 4),
(5, 1, 1), (1, 5, 1), (1, 1, 5),
(1, 6), (6, 1),
(7)

How many ways can a row measuring fifty units in length be filled?
NOTE: Although the example above does not lend itself to the possibility, in
general it is permitted to mix block sizes. For example, on a row measuring
eight units in length you could use red (3), black (1), and red (4).
"""

from pupy.decorations import cash_it


@cash_it
def block_combinations(remaining, last_one=True):
    if remaining == 0:
        return 1
    else:
        blockcount = 0
        blockcount += block_combinations(remaining-1, True)
        if last_one:
            for i in range(3, remaining+1):
                blockcount += block_combinations(remaining-i, False)
        return blockcount


def p114():
    return block_combinations(50)


if __name__ == '__main__':
    assert block_combinations(7) == 17
    ANSWER = p114()
    print("# block combinations: {}".format(ANSWER))
