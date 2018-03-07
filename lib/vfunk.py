from math import sqrt, acos


def length(vector):
    return sqrt(dotproduct(vector, vector))


def angle(v1, v2):
    return acos(
        dotproduct(v1, v2) / (length(v1) * length(v2)))

def dotproduct(v1, v2):
    return sum((a * b) for a, b in zip(v1, v2))


def cross_prod_2d(v1: tuple or list, v2: tuple or list) -> int:
    """Cross product of two 2d vectors

    :param v1: first vector
    :param v2: second vector
    :return: cross product
    """
    return (v1[0] * v2[1]) - (v1[1] * v2[0])