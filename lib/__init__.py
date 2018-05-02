#  !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
__author__ = "Jesse K. Rubin"
__license__ = "GPL"
__version__ = "NaN"

from cProfile import Profile
from functools import wraps
from inspect import getfile
from time import time

try: xrange  # python 2
except NameError: xrange = range  # python 3
