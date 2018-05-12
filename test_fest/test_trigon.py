# coding=utf-8
# Jesse Rubin - project Euler
"""
testing the pytriplets function/gen I made
"""
from lib.biblioteca import Trigon, Vuple, pytriple_gen


class TestTrigon(object):

    def test_triangle_area_half(self):
        t2 = [(1, 0), (0, 1), (0, 0)]
        assert 0.5 == Trigon(*t2).area()

    def test_origin_in_triangle(self):
        pts = [(-340, 495), (-153, -910), (835, -947)]
        tri = Trigon.from_points(pts)
        assert (0, 0) in tri
        assert tri.contains_origin()

    def test_point_on_perimeter(self):
        pts = [(-340, 495), (-153, -910), (835, -947)]
        tri = Trigon.from_points(pts)
        assert tri.is_perimeter_point(pts[0])

    def test_origin_not_in_triangle(self):
        tri = Trigon((-175, 41), (-421, -714), (574, -645))
        assert Vuple((0, 0)) not in tri
        assert tri.contains_origin() == False


class TestPytriplesGen(object):
    # primatives less than 100
    lt100 = {(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25),
             (20, 21, 29), (9, 40, 41), (12, 35, 37), (11, 60, 61),
             (28, 45, 53), (33, 56, 65), (13, 84, 85), (16, 63, 65),
             (48, 55, 73), (39, 80, 89), (36, 77, 85), (65, 72, 97)}
    lt300 = {(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25),
             (20, 21, 29), (9, 40, 41), (12, 35, 37), (11, 60, 61),
             (28, 45, 53), (33, 56, 65), (13, 84, 85), (16, 63, 65),
             (48, 55, 73), (39, 80, 89), (36, 77, 85), (65, 72, 97),
             (20, 99, 101), (60, 91, 109), (15, 112, 113), (44, 117, 125),
             (88, 105, 137), (17, 144, 145), (24, 143, 145), (51, 140, 149),
             (85, 132, 157), (119, 120, 169), (52, 165, 173), (19, 180, 181),
             (57, 176, 185), (104, 153, 185), (95, 168, 193), (28, 195, 197),
             (84, 187, 205), (133, 156, 205), (21, 220, 221), (140, 171, 221),
             (60, 221, 229), (105, 208, 233), (120, 209, 241), (32, 255, 257),
             (23, 264, 265), (96, 247, 265), (69, 260, 269), (115, 252, 277),
             (160, 231, 281), (161, 240, 289), (68, 285, 293)}

    def test_pytriplets_c_lt100(self):
        """
        Testing the primative pytriplet generator
        """
        p_set = {t for t in pytriple_gen(100)}
        assert self.lt100 == p_set

    def test_pytriplets_c_lt300(self):
        p_set = {t for t in pytriple_gen(300)}
        assert self.lt300 == p_set
