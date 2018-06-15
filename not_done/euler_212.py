# -*- coding: utf-8 -*-
# ~ Jesse Rubin ~ project Euler ~
"""
Combined Volume of Cuboids
Problem 212 
An axis-aligned cuboid, specified by parameters { (x0,y0,z0), (dx,dy,dz) }, consists of all points (X,Y,Z) such that x0 ≤ X ≤ x0+dx, y0 ≤ Y ≤ y0+dy and z0 ≤ Z ≤ z0+dz. The volume of the cuboid is the product, dx × dy × dz. The combined volume of a collection of cuboids is the volume of their union and will be less than the sum of the individual volumes if any cuboids overlap.

Let C1,...,C50000 be a collection of 50000 axis-aligned cuboids such that Cn has parameters

x0 = S6n-5 modulo 10000
y0 = S6n-4 modulo 10000
z0 = S6n-3 modulo 10000
dx = 1 + (S6n-2 modulo 399)
dy = 1 + (S6n-1 modulo 399)
dz = 1 + (S6n modulo 399)

where S1,...,S300000 come from the "Lagged Fibonacci Generator":

For 1 ≤ k ≤ 55, Sk = [100003 - 200003k + 300007k3]   (modulo 1000000)
For 56 ≤ k, Sk = [Sk-24 + Sk-55]   (modulo 1000000)

Thus, C1 has parameters {(7,53,183),(94,369,56)}, C2 has parameters {(2383,3563,5079),(42,212,344)}, and so on.

The combined volume of the first 100 cuboids, C1,...,C100, is 723581599.

What is the combined volume of all 50000 cuboids, C1,...,C50000 ?
"""
from __future__ import division, print_function
from copy import copy
from bib import xrange
from bib.maths import repermutations
from bib.listless import list_product
from bib.decorations import cash_it
from bib.maths import Vuple


@cash_it
def lfg(k):
    if 1 <= k <= 55:
        return (100003 - (200003 * k) + (300007 * (k**3))) % 1000000
    else:
        return lfg(k - 24) + lfg(k - 55)


def cuboid_gen(n):
    x0 = lfg(6 * n - 5) % 10000
    y0 = lfg(6 * n - 4) % 10000
    z0 = lfg(6 * n - 3) % 10000
    dx = 1 + lfg(6 * n - 2) % 399
    dy = 1 + lfg(6 * n - 1) % 399
    dz = 1 + lfg(6 * n - 0) % 399
    return x0, y0, z0, dx, dy, dz


class Cuboid(object):
    def __init__(self, toop):
        self.min_xyz = Vuple(toop[:3])
        self.dxyz = Vuple(toop[3:])
        self.max_xyz = self.min_xyz + Vuple(toop[3:])
        self.vol = list_product(self.dxyz)

    def disjoint(self, other):
        print(self.min_xyz, self.max_xyz)
        print(other.min_xyz, other.max_xyz)
        if all(self.max_xyz[i] > other.min_xyz[i] for i in range(3)):
            return True
        elif all(other.max_xyz[i] > self.min_xyz[i] for i in range(3)):
            return True
        return False

    def intersection(self, other):
        if not self.disjoint(other):
            return 0
        if all(self.max_xyz[i] > other.min_xyz[i] for i in range(3)):
            return list_product(self.max_xyz - other.min_xyz)
        elif all(other.max_xyz[i] > self.min_xyz[i] for i in range(3)):
            return list_product(other.max_xyz - self.min_xyz)

    def min_pt(self):
        return self.min_xyz

    def __contains__(self, pt):
        return all(self.min_xyz[i] < pt[i] < self.max_xyz[i] for i in range(3))

    def max_pt(self):
        return self.max_xyz

    def in_zy(self, x_val):
        return self.min_xyz[0] < x_val < self.max_xyz[0]

    def yz_planes(self):
        return (i for i in range(self.min_xyz[0], self.max_xyz[0]))

    def yz_inds(self):
        return set((i, j) for i in range(self.min_xyz[1], self.max_xyz[1])
                   for j in range(self.min_xyz[2], self.max_xyz[2]))

    def z_line(self):
        return set(i for i in range(self.min_xyz[2], self.max_xyz[2]))

    def allinds(self):
        return ((i, j, k) for i in range(self.min_xyz[0], self.max_xyz[0])
                for j in range(self.min_xyz[1], self.max_xyz[1])
                for k in range(self.min_xyz[2], self.max_xyz[2]))

    def __str__(self):
        return ' '.join((str(self.min_xyz), str(self.max_xyz)))

    def __repr__(self):
        return ' '.join((str(self.min_xyz), str(self.max_xyz)))

        # elif all(other.max_xyz[i] > self.min_xyz[i] for i in range(3)):


ca = (0, 0, 0, 4, 4, 4)
cb = (2, 2, 2, 10, 10, 10)
ca = Cuboid(ca)
cb = Cuboid(cb)

# print(cb.yz_inds())
allset = (cb.allinds())
# print("ASKDJFASL")
# print(ca.disjoint(cb))
# print(ca.intersection(cb))
from collections import defaultdict
from itertools import *
# firsthund = [Cuboid(cuboid_gen(i)) for i in range(1, 100 + 1)]
firsthund = [ca, cb]

# for a, b in combinations(firsthund, 2):
#     if a.disjoint(b):
#         print(a, b)
sss = [c.allinds() for c in firsthund]

# firsthund = [ca, cb]
# sheeet = []
# for cube in firsthund:
#     sheeet.extend(list(cube.allinds()))
#     print(cube)


# print(firsthund)
# lll = []
# for i in range(0, len(firsthund), 2):
#     print(i / len(firsthund))
#     s1 = firsthund[i].allinds()
#     s2 = firsthund[i + 1].allinds()
#     lll.append(set.union(s1, s2))

# firsthund = [ca, cb]
# print(len(firsthund))
# print(firsthund)
# minx = min(c.min_pt()[0] for c in firsthund)
# maxx = max(c.max_pt()[0] for c in firsthund)
# print(minx, maxx)

# def scan_line(cube_inds):
#     # print(yi, cube_inds)
#     zinds = set()
#     for c in cube_inds:
#         zinds.update(firsthund[c].z_line())
#     # print(zinds)
#     return len(zinds)

# def scan_plane(xi, icuboid):
#     # ydict = defaultdict(set)
#     # for ci in icuboid:
#     #     for yi in firsthund[ci].z_line():
#     #         ydict[yi].add(ci)

#     # # print(ydict)
#     # vt = 0
#     # for yi, ciset in ydict.items():
#     #     vt += scan_line(ciset)
#     # return vt
#     volcount = 0
#     inds = set()
#     for ic in icuboid:
#         c = firsthund[ic]
#         sss = c.yz_inds()
#         inds.update(sss)
#     # print(len(inds))

#     return len(inds)
#     # for yi in range(miny, maxy):

#     # print(maxy, miny)
#     # pts = set()
#     # for yi in range(miny, maxy):

#     # ll = {(xi, yi, zi)
#     #       for yi in range(miny, maxy + 1) for zi in range(minz, maxz + 1)
#     #       if any((xi, yi, zi) in firsthund[i] for i in icuboid)}
#     # return ll

#     # print(ll)

# # for each cuboid make a dictionary that holds what cuboids are in what yz planes
# xdict = defaultdict(set)
# for ci in range(len(firsthund)):
#     for xi in firsthund[ci].yz_planes():
#         xdict[xi].add(ci)

# print(xdict)

# tvol = 0
# for xi, ciset in xdict.items():
#     v = scan_plane(xi, ciset)
#     tvol += v
#     print(xi, tvol)
#     # tvol += len(v)
#     # print(len(v), tvol)

#     # print(v, tvol)

# # print(xi, c)

# # ucubes = set()

# # def add_cuboid(c):
# #     p1, p2 = c[:3], c[3:]
# #     pv1 = Vuple(p1)
# #     pv2 = Vuple(p2)
# #     print(p1, p2)
# #     x0, y0, z0 = p1
# #     dx, dy, dz = p2
# #     # pts = set()
# #     # for x1 in range(dx):
# #     #     for y1 in range(dy):
# #     #         # for z1 in range(min(z0, dz), max(z0, dz)):
# #     #         for z1 in range(dz):
# #     pts = set(
# #         tuple((pv1 + Vuple((x1, y1, z1)))) for x1 in range(dx)
# #         for y1 in range(dy) for z1 in range(dz))
# #     # for x1 in range(dx):
# #     #     for y1 in range(dy):
# #     #         # for z1 in range(min(z0, dz), max(z0, dz)):
# #     #         for z1 in range(dz):
# #     #             pts.add(tuple((pv1 + Vuple((x1, y1, z1)))))
# #     ucubes.update(pts)
