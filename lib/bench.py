from cProfile import Profile
from functools import wraps
from time import time


def tictoc(funk):

    @wraps(funk)
    def timed(*args, **kw):
        ts = time()
        result = funk(*args, **kw)
        te = time()
        print('%r  %2.4f ms' % (funk.__name__, (te - ts) * 1000))
        return result
    return timed

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