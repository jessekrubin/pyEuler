#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Magic 5-gon ring
Problem 68 
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and
each line adding to nine.


Working clockwise, and starting from the group of three with the numerically
lowest external node (4,3,2 in this example), each solution can be described
uniquely. For example, the above solution can be described by the set:
4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11,
and 12. There are eight solutions in total.

                        Total	Solution Set
                        9	4,2,3; 5,3,1; 6,1,2
                        9	4,3,2; 6,2,1; 5,1,3
                        10	2,3,5; 4,5,1; 6,1,3
                        10	2,5,3; 6,3,1; 4,1,5
                        11	1,4,6; 3,6,2; 5,2,4
                        11	1,6,4; 5,4,2; 3,2,6
                        12	1,5,6; 2,6,4; 3,4,5
                        12	1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum
string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form
16- and 17-digit strings. What is the maximum 16-digit string for a "magic"
5-gon ring?
"""

from itertools import combinations, permutations

from bib.listless import rotate

# Looking for the max 16 digit string for the magic 5-gon ring means that
# the 10 must be on the outside.
one_to_ten = [i+1 for i in range(10)]

triplets = {}
for t in combinations(one_to_ten, 3):
    triplets.setdefault(sum(t), []).append(t)

triplets = {k:v for k, v in triplets.items() if 13 < k < 20}


def rotate_ring(ring):
    while ring[0][0] != min(r[0] for r in ring):
        ring = rotate(ring)
    return ring


def rotate_ring(ring):
    while ring[0][0] != min(r[0] for r in ring):
        ring = rotate(ring)
    return ring


def five_gon(ring, remaining_combos):
    if len(ring) == 5:
        # check if valid
        if all(ring[i][2] == ring[(i+1)%5][1] for i in range(5)):
            return ring
        return
    else:
        last = ring[-1]
        lastlast = last[-1]
        # outer_ring = [r[0] for r in ring]
        haslastlast = [c for c in remaining_combos if lastlast in c]
        for comb in haslastlast:
            ans = []
            for p in permutations(comb):
                if p[1] == lastlast:
                    without = remaining_combos[:]
                    without.remove(comb)
                    outer_ring = [r[0] for r in ring]
                    without = [c for c in without if all(n not in c for n in outer_ring)]
                    tempring = ring[:]
                    tempring.append(p)
                    ans.append(five_gon(tempring, without))

            return [a for a in ans if a != None]


def magic_5_gon(sum, combos):
    has10 = [c for c in combos if 10 in c]
    rings = []
    for combo in has10:
        not_tens = list(perm for perm in permutations(combo) if perm[0] == 10)
        without = combos[:]
        without.remove(combo)
        for p in not_tens:
            ring = five_gon([p], without)
            if ring != None:
                rings.extend(i for i in ring)

    ringo = []
    for layer1 in rings:
        for layer2 in layer1:
            for layer3 in layer2:
                for layer5 in layer3:
                    ringo.append(layer5)

    rings = [rotate_ring(ring) for ring in ringo if ring != None]
    return max(rings)


def p068():
    rings = {k:magic_5_gon(k, v) for k, v in triplets.items()}
    rings = [int("".join(["".join([str(n) for n in piece]) for piece in ring]))
             for sum, ring in rings.items()]
    return max(rings)


if __name__ == '__main__':
    ans = p068()
    print("MAX 5 GON: {}".format(ans))