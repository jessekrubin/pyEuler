# coding=utf-8
from setuptools import setup
from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='pyEuler',
    packages=['bib', 'done/py', 'no_cigar'],
    ext_modules=cythonize("bib/*.pyx"),
    author='jessekrubin',
    author_email='jessekrubin@gmail.com',
    description='project euler solutions')


def main():
    pass


if __name__ == '__main__':
    main()