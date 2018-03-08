#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler

class json_cache(object):

    def __init__(self, json_filepath):
        self.json_filepath = json_filepath

    def __call__(self, fn, *args, **kwargs):
        def new_func(*args, **kwargs):
            print "Function has been decorated.  Congratulations."
            return fn(*args, **kwargs)
        return new_func