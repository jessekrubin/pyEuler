# coding=utf-8
import json as jasm
from importlib import import_module
import pytest
from multiprocessing import Pool
from os import listdir, path
from sys import stderr, stdout

from operator import itemgetter
from time import time
from pupy.decorations import tictoc
import pytest


with open('../../txt_files/solutions.txt') as f:
    SOLUTIONS = jasm.load(f)

PASSED, NO_SOL, NO_PFUNK, FAILED, SOL_IS_NONE = [], [], [], [], []
VERBOSE = False
DONE = [str(f[6:9]) for f in listdir('.')  # find all files in the done dir
        if f.startswith('euler_')  # for which the file start with 'euler_'
        and f.endswith('.py')]  # and ends with '.py'

print(DONE)
@pytest.mark.parametrize('pn_str', DONE)
def test_prob(pn_str):
    """Checks if the project euler solutions in this repo are correct

    Args:
        pn_str (str): problem number string (ex: '001')

    Returns:
        run time (float): if the test_pupy passes
        failure message (str): if test_pupy fails to pass
            'NO_PFUNK': the problem file doesn have a pXXX() method
            'NO_SOL': the problem has no __sol__ variable
            'SOL_IS_NONE': the __sol__ variable for the problem is None
    """
    p_file = import_module('euler_{}'.format(pn_str))
    try:
        p_funk = getattr(p_file, 'p{}'.format(pn_str))
    except AttributeError:
        if VERBOSE:
            print(pn_str, 'NO_PFUNK')
        return pn_str, 'NO_PFUNK'
    try:
        p_ans = SOLUTIONS[pn_str]
    except KeyError:
        if VERBOSE:
            print(pn_str, 'NO_SOL')
        return pn_str, 'NO_SOL'
    if p_ans is None:
        if VERBOSE:
            print(pn_str, 'SOL_IS_NONE')
        return pn_str, 'SOL_IS_NONE'
    ts = time()
    my_ans = p_funk()
    te = time() - ts
    assert p_ans == my_ans
    # try:
    #     assert p_ans == my_ans
    # except AssertionError:
    #     if VERBOSE:
    #         print(pn_str, 'FAIL')
    #     return pn_str, 'FAIL'
    # if VERBOSE:
    #     print("PASS: {} ({} ms)".format(pn_str, round(te)))
    # return pn_str, te

if __name__ == '__main__':
    pytest.main()

