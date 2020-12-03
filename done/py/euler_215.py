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
from pupy.maths import disjoint
from pupy.decorations import cash_it
from itertools import combinations
from collections import defaultdict


@cash_it
def brick_cracks(remaining, legos=(2, 3), cur_layer=None):
    """

    Args:
        remaining (int): Spaces to fill
        legos (tuple): lego brick sizes to use
        cur_layer (tuple): current layer

    Yields:
        tuple: permutations of brick combinations

    """
    if cur_layer is None:
        for lego in legos:
            for layer in brick_cracks(remaining - lego, legos, tuple([lego])):
                yield layer
    else:
        for n in [l for l in legos if l <= remaining]:
            for layer in brick_cracks(
                remaining - n, legos, tuple(list(cur_layer) + [n])
            ):
                yield layer
        if remaining == 0:
            yield tuple(sum(cur_layer[0:i]) for i in range(1, len(cur_layer)))
        if remaining == 1:
            StopIteration


def W(width, height):
    cracks = set(layer for layer in brick_cracks(width))  # crack/brick layers
    disjoints = defaultdict(set)  # disjoint layer combos dictionary
    for a, b in combinations(cracks, 2):  # for each crack combination...
        if disjoint(a, b):  # valid if cracks are disjoint...
            disjoints[a].add(b)  # add b to the disjoing-crack-layers to a
            disjoints[b].add(a)  # add a to the disjoing-crack-layers to b

    @cash_it  # cache / memozation decorator for recurssive function
    def layer_combos(remaining, cur):
        """Count layer combos using the disjoint sets dictionary"""
        if remaining == 0:
            return 1
        return sum(layer_combos(remaining - 1, d) for d in disjoints[cur])

    # return count of all layer combos for each starting layer
    return sum(layer_combos(height - 1, layer) for layer in disjoints)


def p215():
    return W(32, 10)


if __name__ == '__main__':
    assert 8 == W(9, 3)
    ANSWER = p215()
    print("CRACK FREE WALLS: {}".format(ANSWER))
