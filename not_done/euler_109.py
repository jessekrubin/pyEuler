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

Note that D1 D2 is considered different to D2 D1 as they finish on different
doubles. However, the combination S1 T1 D1 is considered the same as T1 S1 D1.
In addition we shall not include misses in considering combinations; for
example, D3 is the same as 0 D3 and 0 0 D3. Incredibly there are 42336 distinct
ways of checking out in total. How many distinct ways can a player checkout 
with a score less than 100?
"""
from itertools import *
from bib.maths import Vuple
from collections import Counter
from collections import defaultdict, namedtuple
points = [(1, 25),
          (2, 25)] + [(m, n) for m in range(1, 4) for n in range(1, 21)]

vals = Counter(a * b for a, b in points)

vpts = [Vuple(toop) for toop in points]
# 38182

print(vals)


def checkoutsf(score):
    c = set()
    # def checkout(score, l):
    #     if score==0 and l[-1][0]==2:
    #         c.add(tuple(l))
    #     elif score>1 and len(l)==1:
    #         for v in vpts:
    #             # checkout(score-v.product(), sorted(l)+[v])
    #             checkout(score-v.product(), l+[v])
    #     elif score>1 and len(l)==2:
    #         for v in vpts:
    #             checkout(score-v.product(), sorted(l)+[v])
    g = 0

    def checkout(score, l):
        global g
        if score == 0 and l[-1][0] == 2:
            return 1
            c.add(tuple(l))
        if score <= 0:
            return 0
        elif score > 1 and len(l) == 1:
            for v in vpts:
                checkout(score - v.product(), l + [v])
        elif score > 1 and len(l) == 2:
            for v in vpts:
                checkout(score - v.product(), sorted(l) + [v])

    for vpt in vpts:
        checkout(score - vpt.product(), [vpt])
    return len(c)


def sp(l):
    return sum(p.product() for p in l)


from bib.maths import partitions_gen

thing = [m * n for m in range(1, 21) for n in range(1, 4)] + [25, 50]
cs = set()
for combosize in range(1, 4):
    for combo in combinations(thing, combosize):
        if sum(combo) < 100:
            cs.add(combo)

print(cs)

#
# for i in range(2, 100):
#     t = 0
#     for part in cs:
#         if sum(part)<=3:
#             s = set()
#             for perm in permutations(part):
#                 if perm[-1]!= 1:
#                     s.add(perm)
#             t+=len(s)
#     print((t))
#

# def p109(checkout_lim = 100):
# ones = set(p for p in vpts if p[0]==2)
#
# twos = set()
# for permutation in permutations(vpts, 2):
#     if sp(permutation)<100:
#         twos.add(permutation)
#
#
# print(twos)
# a = len(set.union(ones, twos))

# t = 0
# for i in range(2, 100):
#     t+=(checkoutsf(i))
# return t

# if __name__ == '__main__':
#     ANSWER = p109()
#     print("CHECKOUTS: {}".format(ANSWER))
