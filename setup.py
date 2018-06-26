# coding=utf-8
from distutils.core import setup
from Cython.Build import cythonize
from sys import argv


def main():
    """run setup"""
    try:
        setup(
            name='pyEuler',
            packages=['bib', 'done/py', 'no_cigar'],
            ext_modules=cythonize(
                ("bib/*.pyx",
                 "cbib/*.pyx",
                 "no_cigar/*.pyx")),
            author='jessekrubin',
            author_email='jessekrubin@gmail.com',
            description='project euler solutions',
            requires=['tqdm', 'cython']
        )
    except:
        setup(
            name='pyEuler',
            packages=['bib', 'done/py', 'no_cigar'],
            author='jessekrubin',
            author_email='jessekrubin@gmail.com',
            description='project euler solutions',
            requires=['tqdm']
        )


if __name__ == '__main__':
    # if len(argv) == 1:
    #     argv.append('install')
    #     argv.append('build_ext')
    #     argv.append('--inplace')
    #     print(argv)
    main()
