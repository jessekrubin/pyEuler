#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler
"""
Decorations
"""
from cProfile import Profile
from functools import wraps
from inspect import getfile
from io import open
from os import path, getcwd
from time import time


class tictoc(object):

    def __init__(self, runs=1, save=False):
        self.runs = runs
        self.save = save

    def __call__(self, funk):
        @wraps(funk)
        def wrapper(*args, **kwargs):
            ts = time()
            for i in range(self.runs):
                result = funk(*args, **kwargs)
            te = time()
            t_total = (te - ts) / self.runs

            if self.save:
                prob_n = getfile(funk)[-6:-3]
                with open(path.join(getcwd(), "./tictoc/pytriplets_gen{}.tictoc".format(prob_n)), "a") as tictoc_file:
                    tictoc_file.write(
                            'ARGS:{}_KWARGS:{}_TIME:{}_TRIALS:{}\n'.format(str(args),
                                                                           str(kwargs),
                                                                           str(t_total),
                                                                           str(self.runs)))
            print('__TICTOC__\n'
                  '    file: {}\n'
                  '    funk: {}\n'
                  '    args: {}\n'
                  '    time: {} ms\n'
                  '    runs: {}\n'.format(getfile(funk),
                                          funk.__name__,
                                          str(args),
                                          t_total * 1000,
                                          self.runs
                                          ))
            return result

        return wrapper

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