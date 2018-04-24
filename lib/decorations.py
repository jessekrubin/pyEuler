#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler
"""
Decorations used by me!!!
"""
from cProfile import Profile
from functools import wraps
from inspect import getfile
from time import time


def cash_muney(funk):
    """
    for when you want that lru cach money but are working w py2

    :param funk:
    :return:
    """
    cash_money = {}
    @wraps(funk)
    def wrapper(*argz):
        if argz in cash_money:
            return cash_money[argz]
        else:
            rv = funk(*argz)
            cash_money[argz] = rv
            return rv
    return wrapper

def cprof(funk):
    """
    cProfiling decorator
    src: https://zapier.com/engineering/profiling-python-boss/

    :param funk:
    :return:
    """

    @wraps(funk)
    def profiled_funk(*args, **kwargs):
        profile = Profile()
        try:
            profile.enable()
            ret_val = funk(*args, **kwargs)
            profile.disable()
        finally:
            print("__CPROFILE__")
            profile.print_stats()
        return ret_val

    return profiled_funk

class tictoc(object):
    """
    Timing decorator object

    :param runs: number of runs to time over (defaults to 1)
    """

    def __init__(self, runs=1):
        self.runs = runs

    def __str__(self, t_total, funk, args_string):
            return('__TICTOC__\n'
                   '    file: {}\n'
                   '    funk: {}\n'
                   '    args: {}\n'
                   '    time: {} ms\n'
                   '    runs: {}\n'.format(getfile(funk),
                                          funk.__name__,
                                          args_string,
                                          t_total * 1000,
                                          self.runs))

    def __call__(self, funk):
        @wraps(funk)
        def wrapper(*args, **kwargs):
            self.args = str(args)
            ts = time()
            for i in range(self.runs):
                result = funk(*args, **kwargs)
            te = time()
            t_total = (te - ts) / self.runs
            print(self.__str__(t_total, funk, str(args)))
            return result

        return wrapper

