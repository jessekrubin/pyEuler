# coding=utf-8
from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = 'Hello world app',
    ext_modules = cythonize("euler_075.pyx")
)
# python setup.py build_ext --inplace.
