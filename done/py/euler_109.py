# -*- coding: utf-8 -*-
# ~ Jesse Rubin ~ project Euler ~
"""
Darts
http://projecteuler.net/problem=109
In the game of darts a player throws three darts at a target board which is
split into twenty equal sized sections numbered one to twenty. The score of a
dart is determined by the number of the region that the dart lands in. A dart
landing outside the red/green outer ring scores zero. The black and cream
regions inside this ring represent single scores. However, the red/green outer
ring and middle ring score double and treble scores respectively.

At the centre of the board are two concentric circles called the bull region,
or bulls-eye. The outer bull is worth 25 points and the inner bull is a double,
worth 50 points.

There are many variations of rules but in the most popular game the players
will begin with a score 301 or 501 and the first player to reduce their
running total to zero is a winner. However, it is normal to play a "doubles
out" system, which means that the player must land a double (including the
double bulls-eye at the centre of the board) on their final dart to win; any
other dart that would reduce their running total to one or lower means the
score for that set of three darts is "bust". When a player is able to finish on
their current score it is called a "checkout" and the highest checkout is 
170: T20 T20 D25 (two treble 20s and double bull).

There are exactly eleven distinct ways to checkout on a score of 6:

                            ╔════╦════╦════╗
                            ║ D3 ║    ║    ║
                            ║ D1 ║ D2 ║    ║
                            ║ S2 ║ D2 ║    ║
                            ║ D2 ║ D1 ║    ║
                            ║ S4 ║ D1 ║    ║
                            ║ S1 ║ S1 ║ D2 ║
                            ║ S1 ║ T1 ║ D1 ║
                            ║ S1 ║ S3 ║ D1 ║
                            ║ D1 ║ D1 ║ D1 ║
                            ║ D1 ║ S2 ║ D1 ║
                            ║ S2 ║ S2 ║ D1 ║
                            ╚════╩════╩════╝
{((1, 2), (1, 2), (2, 1)),
((1, 1), (1, 3), (2, 1)),
((2, 1), (2, 1), (2, 1)),
((1, 1), (1, 1), (2, 2)),
((1, 2), (2, 1), (2, 1)),
(2, 3),
((1, 4), (2, 1)),
((2, 1), (2, 2)),
((1, 1), (3, 1), (2, 1)),
((1, 2), (2, 2))} 10

Note that D1 D2 is considered different to D2 D1 as they finish on different
doubles. However, the combination S1 T1 D1 is considered the same as T1 S1 D1.
In addition we shall not include misses in considering combinations; for
example, D3 is the same as 0 D3 and 0 0 D3. Incredibly there are 42336 distinct
ways of checking out in total. How many distinct ways can a player checkout 
with a score less than 100?
"""

from operator import mul
from functools import reduce
from collections import defaultdict
from itertools import combinations_with_replacement, permutations

SCORES = [(1, 25), (2, 25)] + [(m, n) for m in range(1, 4) for n in range(1, 21)]


# bullseye and double-bullseye
# (1, 25), (2, 25),
# singles
# (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9),
# (1, 10), (1, 11), (1, 12), (1, 13), (1, 14), (1, 15), (1, 16), (1, 17),
# (1, 18), (1, 19), (1, 20),
# doubles
# (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9),
# (2, 10), (2, 11), (2, 12), (2, 13), (2, 14), (2, 15), (2, 16), (2, 17),
# (2, 18), (2, 19), (2, 20),
# triples
# (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9),
# (3, 10), (3, 11), (3, 12),(3, 13), (3, 14), (3, 15), (3, 16), (3, 17),
# (3, 18), (3, 19), (3, 20)


def darts_score(d_toop):
    return sum(reduce(mul, d) for d in d_toop)


def p109(MAX_CHECKOUT=99):
    CHECKOUTS = defaultdict(set)

    # ONE THROW
    CHECKOUTS.update({darts_score((d,)): {(d,)} for d in SCORES if d[0] == 2})

    # TW0 THROWS
    for combo in combinations_with_replacement(SCORES, 2):
        for d1, d2 in permutations(combo, 2):
            if d2[0] == 2:
                CHECKOUTS[darts_score((d1, d2))].add((d1, d2))

    # THREE THROWS
    for combo in combinations_with_replacement(SCORES, 3):
        for d1, d2, d3 in permutations(combo, 3):
            if d3[0] == 2 and d1 <= d2:
                CHECKOUTS[darts_score((d1, d2, d3))].add((d1, d2, d3))

    # forget the ones gt the max val
    return sum(len(v) for k, v in CHECKOUTS.items() if k < MAX_CHECKOUT + 1)


if __name__ == '__main__':
    ANSWER = p109()
    print("{} possible checkouts for scores lt 100 exist".format(ANSWER))
