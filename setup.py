# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(name='pyEuler',
      version='1.0',
      description='project euler problem solutions',
      long_description='coming soon',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy'
          ],
      keywords='project euler python',
      repository='https://github.com/jessekrubin/pyEulerj',
      author_email='jessekrubin@gmail.com',
      author='jessekrubin',
      license='MIT',
      packages=find_packages(),
      install_requires=['pytest'],
      include_package_data=True,
      zip_safe=False
      )



