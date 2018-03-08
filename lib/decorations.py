#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler
import json
from functools import wraps


class json_cash:

    def __init__(self, filename):
        print(filename)
        self.filename = filename
        self.method_input = input

    def __call__(self, func):
        # this is called by Python with the completed def
        @wraps(func)
        def wrapper(*args, **kwds):
            try:
                print(self.filename)
                with open(self.filename) as stored:
                    data = json.load(stored)
            except IOError:
                data = func(*args, **kwds)
                with open(self.filename, 'w') as stored:
                    json.dump(data, stored)
            return data
        return wrapper