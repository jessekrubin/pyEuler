#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Crack-free Walls
Problem 215
Consider the problem of building a wall out of 2×1 and 3×1 bricks
(horizontal×vertical dimensions) such that, for extra strength, the gaps
between horizontally-adjacent bricks never line up in consecutive layers,
i.e. never form a "running crack".

For example, the following 9×3 wall is not acceptable due to the running crack
shown in red:

|# # #|# #|# #|# #|
|# #|# # #|# #|# #|
|# # #|# # #|# # #|

There are eight ways of forming a crack-free 9×3 wall, written W(9,3) = 8.

Calculate W(32,10).
"""
from __future__ import generators
from lib.maths import disjoint
from lib.decorations import cash_it
from itertools import combinations
from collections import defaultdict


def layer_cracks(remaining, legos=(2, 3), cur=None):
    if cur is None:
        for lego in legos:
            for layer in layer_cracks(remaining-lego, legos, [lego]):
                yield layer
    else:
        for n in [l for l in legos if l <= remaining]:
            for layer in layer_cracks(remaining-n, legos, cur+[n]): yield layer
        if remaining == 0: yield tuple(sum(cur[0:i]) for i in range(1, len(cur)))
        if remaining == 1: raise StopIteration


def W(width, height):
    HEIGHT = height
    WIDTH = width

    # BRICKS = set(layer for layer in layer_cracks(WIDTH) if layer is not None)
    BRICKS = set(layer for layer in layer_cracks(WIDTH))
    disjoints = defaultdict(set)
    for a, b in combinations(BRICKS, 2):
        if disjoint(a, b):
            disjoints[a].add(b)
            disjoints[b].add(a)

    @cash_it
    def layer_combos(remaining, cur):
        if remaining == 0: return 1
        return sum(layer_combos(remaining-1, d) for d in disjoints[cur])

    return sum(layer_combos(HEIGHT-1, layer) for layer in disjoints)


def p215():
    return W(32, 10)


if __name__ == '__main__':
    assert 8 == W(9, 3)
    ANSWER = p215()
    print("CRACK FREE WALLS: {}".format(ANSWER))
