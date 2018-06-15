# coding=utf-8
from __future__ import division, print_function
import pyximport; pyximport.install()
import bib.maths
# import bib.cy_maths
from bib.cybib.cy_amazon_prime import prime_gen as cy_prime_gen
from bib.decorations import tictoc


# def test_n_time_reverse():
#     @tictoc()
#     def _py_reverse():
#         return [bib.maths.reverse(i) for i in range(1000, 999999)]

#     @tictoc()
#     def _cy_reverse():
#         return [bib.cy_maths.reverse(i) for i in range(1000, 999999)]

#     pyreversed = _py_reverse()
#     cyreversed = _cy_reverse()
#     # print(len(pyreversed))


def test_prime_gen():
    def _cy_prime_gen(n):
        return list(cy_prime_gen(n))

    for exp in range(3, 7):
        n = 10**exp
        cy_primes = _cy_prime_gen(n)


if __name__ == '__main__':
    test_prime_gen()
    # test_n_time_reverse()
