# coding=utf-8
from distutils.core import setup
from Cython.Build import cythonize
from sys import argv

if len(argv) == 1:
    argv.append('install')


def main():
    """run setup"""
    setup(name='pyEuler',
          packages=['bib', 'done/py', 'no_cigar'],
          ext_modules=cythonize(("bib/cybib/*.pyx", "no_cigar/*.pyx")),
          author='jessekrubin',
          author_email='jessekrubin@gmail.com',
          description='project euler solutions',
          requires=['tqdm', 'cython'])


if __name__ == '__main__':
    if len(argv) == 1:
        argv.append('install')
    main()
