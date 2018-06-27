# coding=utf-8
from __future__ import division, print_function
import pyximport; pyximport.install()
from time import time
from bib.decorations import tictoc

l = [i for i in range(1, 100000)]

def _bib_test():
    from bib.maths import iter_product
    ti = time()
    iter_product(l)
    te = time()
    return tictoc.ftime(ti, te)

def _cbib_test():
    from cbib.maths import iter_product
    ti = time()
    iter_product(l)
    te = time()
    return tictoc.ftime(ti, te)



def test_iter_product():
    print(_bib_test())
    print(_cbib_test())


test_iter_product()

# t = 1
# for n in l:
#     t *= n
