# coding=utf-8
# Jesse Rubin - project Euler
"""
testing the pytriplets function/gen I made
"""
from bib.maths import pytriple_gen, pytriple_gen_2

lt100 = {(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29),
         (9, 40, 41), (12, 35, 37), (11, 60, 61), (28, 45, 53), (33, 56, 65),
         (13, 84, 85), (16, 63, 65), (48, 55, 73), (39, 80, 89), (36, 77, 85),
         (65, 72, 97)}

gt100_lt300 = {(20, 99, 101), (60, 91, 109), (15, 112, 113), (44, 117, 125),
               (88, 105, 137), (17, 144, 145), (24, 143, 145), (51, 140, 149),
               (85, 132, 157), (119, 120, 169), (52, 165, 173), (19, 180, 181),
               (57, 176, 185), (104, 153, 185), (95, 168, 193), (28, 195, 197),
               (84, 187, 205), (133, 156, 205), (21, 220, 221), (140, 171, 221),
               (60, 221, 229), (105, 208, 233), (120, 209, 241), (32, 255, 257),
               (23, 264, 265), (96, 247, 265), (69, 260, 269), (115, 252, 277),
               (160, 231, 281), (161, 240, 289), (68, 285, 293)}

lt300 = set.union(lt100, gt100_lt300)


def test_pytriplets_c_lt100():
    """Testing pytriples with c values less than 100"""
    assert {t for t in pytriple_gen(100)} == lt100


def test_pytriplets_c_lt300():
    """Testing pytriples with c values less than 100"""
    p_set = {t for t in pytriple_gen(300)}
    assert lt300 == p_set


def test_pytriplets_2_c_lt100():
    """Testing pytriples with c values less than 100"""
    vals = set()
    gen = pytriple_gen_2()
    while len(vals) < len(lt100):
        next_val = next(gen)
        print(next_val)
        vals.add(next(gen))
    assert vals == lt100


def test_pytriplets_2_c_lt300():
    """Testing pytriples with c values less than 100"""
    vals = set()
    gen = pytriple_gen_2()
    while len(vals) < len(lt300):
        vals.add(next(gen))
    assert vals == lt300


test_pytriplets_2_c_lt100()
test_pytriplets_2_c_lt300()