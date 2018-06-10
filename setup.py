# coding=utf-8
from distutils.core import setup
from Cython.Build import cythonize


setup(name='pyEuler',
      packages=['bib', 'done/py', 'no_cigar'],
      ext_modules=cythonize("bib/cybib/*.pyx"),
      author='jessekrubin',
      author_email='jessekrubin@gmail.com',
      description='project euler solutions')

# def main():
#     setup(name='pyEuler',
#           packages=['bib', 'done/py', 'no_cigar'],
#           ext_modules=cythonize("bib/*.pyx"),
#           author='jessekrubin',
#           author_email='jessekrubin@gmail.com',
#           description='project euler solutions')
#
#
# if __name__ == '__main__':
#     main()
