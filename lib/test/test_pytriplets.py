# coding=utf-8
# Jesse Rubin - project Euler
"""
testing the pytriplets function/gen I made
"""

from lib.maths import pytriple_gen


def test_pytriplets_c_lt100():

    """
    Testing the primative pytriplet generator
    """

    # primatives less than 100
    lt100 = {(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25),
             (20, 21, 29), (9, 40, 41), (12, 35, 37), (11, 60, 61),
             (28, 45, 53), (33, 56, 65), (13, 84, 85), (16, 63, 65),
             (48, 55, 73), (39, 80, 89), (36, 77, 85), (65, 72, 97)}
    p_set = {t for t in pytriple_gen(100)}
    assert lt100 == p_set

def test_pytriplets_c_lt300():
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

    p_set = {t for t in pytriple_gen(300)}
    assert lt300 == p_set

    # non primatives test
    ########### not_done yet
    # non_prim_lt100 = {(6, 8, 10), (9, 12, 15), (12, 16, 20),
    #                   (15, 20, 25), (10, 24, 26), (18, 24, 30),
    #                   (16, 30, 34), (21, 28, 35), (15, 36, 39),
    #                   (24, 32, 40), (27, 36, 45), (14, 48, 50),
    #                   (30, 40, 50), (24, 45, 51), (20, 48, 52),
    #                   (33, 44, 55), (40, 42, 58), (36, 48, 60),
    #                   (25, 60, 65), (39, 52, 65), (32, 60, 68),
    #                   (42, 56, 70), (24, 70, 74), (21, 72, 75),
    #                   (45, 60, 75), (30, 72, 78), (48, 64, 80),
    #                   (18, 80, 82), (40, 75, 85), (51, 68, 85),
    #                   (60, 63, 87), (54, 72, 90), (35, 84, 91),
    #                   (57, 76, 95)}
    # np_set = {t for t in pytriple_gen(100, primatives_only=False)}
    # print(len(non_prim_lt100), len(np_set))
    # print(non_prim_lt100 - np_set)
    # print(np_set)

