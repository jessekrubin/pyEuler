# coding=utf-8
# Jesse Rubin - project Euler
"""
testing the toople class I have made
"""
from bib.maths import Vuple


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

    def test_mag(self):
        assert 5.0 == Vuple.mag((3, 4))
        assert 5 == Vuple((3, 4)).get_mag()

    def test_mul_scalar(self):
        v = Vuple((3, 4))
        v = (v*2)
        assert (6, 8) == v

    def test_imul_scalar(self):
        v = Vuple((3, 4))
        v *= 2
        assert (6, 8) == v

    def test_div_scalar(self):
        v = Vuple((6, 8))/2
        assert (3, 4) == v

    def test_idiv_scalar(self):
        v = Vuple((6, 8))
        v /= 2
        assert (3, 4) == v

    def test_unit_vuple(self):
        v = Vuple((3, 4))
        assert (0.6, 0.8) == Vuple.unit_vuple(v)
        v = Vuple((3, 4))
        assert (0.6, 0.8) == v.normalize()

    def test_angle_radians(self):
        v1 = Vuple((10, 10))
        v2 = Vuple((1, 0))
        assert 3.1415926535897936 == (4*Vuple.angle(v1, v2))

    def test_angle_degrees(self):
        v1 = Vuple((10, 10))
        v2 = Vuple((1, 0))
        assert 45 == round(Vuple.angle(v1, v2, radians=False))
