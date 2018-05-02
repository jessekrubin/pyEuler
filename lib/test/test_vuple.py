# coding=utf-8
# Jesse Rubin - project Euler
"""
testing the toople class I have made
"""
from lib.maths import Vuple


class Test_Vuple(object):

    def test_gt(self):
        a = Vuple((12, 3))
        b = Vuple((7, 5))
        assert a > b

    def test_add(self):
        a = Vuple((12, 3))
        b = Vuple((7, 5))
        assert Vuple((19, 8)) == a+b

    def test_sub(self):
        a = Vuple((12, 3))
        b = Vuple((7, 5))
        assert Vuple((5, -2)) == a-b
        assert Vuple((-5, 2)) == b-a

    # def test_mul(self):
    #     a = Vuple((12, 3))
    #     b = Vuple((7, 5))
    #     print(a*b)

    # assert Vuple((5, -2)) == a - b
    # assert Vuple((-5, 2)) == b - a
