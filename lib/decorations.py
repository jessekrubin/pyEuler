#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler
"""
Decorations
"""
from cProfile import Profile
from functools import wraps
from time import time, perf_counter
from json import load, dump
from io import open
from os import path, getcwd
from inspect import getfile
import timeit



class tictoc:
    def __init__(self, n_trials=1):
        self.n_trials=n_trials

    def __call__(self, funk):
        @wraps(funk)
        def wrapper(*args, **kwargs):
            ts = time()
            for i in range(self.n_trials):
                result = funk(*args, **kwargs)
            te = time()
            t_total = (te-ts)/self.n_trials
            prob_n = getfile(funk)[-6:-3]
            with open("./tictoc/p{}.tictoc".format(prob_n), "a") as tictoc_file:
                tictoc_file.write(
                    'ARGS:{}_KWARGS:{}_TIME:{}_TRIALS:{}\n'.format(str(args),
                                                                   str(kwargs),
                                                                   str(t_total),
                                                                   str(self.n_trials)))
            print('{} ~ {} ~ {} ms'.format(getfile(funk), funk.__name__, t_total*1000))
            return result

        return wrapper


class json_cash:
    def __init__(self, cash_dir):
        self.cache_dir = cash_dir
        self.cache = {}

    def __call__(self, funk):

        @wraps(funk)
        def wrapper(*args, **kwargs):
            cache_file_path = path.join(self.cache_dir, funk.__name__ + ".json")
            try:
                with open(cache_file_path, 'r', encoding='utf-8') as stored:
                    self.cache[args] = load(stored)
            except IOError:
                pass

            if args in self.cache:
                return self.cache[str(args)]
            else:
                val = funk(*args, **kwargs)
                self.cache[str(args)] = val
                with open(cache_file_path, 'w', encoding='utf-8') as stored:
                    print(self.cache)
                    dump(self.cache, stored, indent=2)
                return val
            return data

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