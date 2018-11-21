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

SOLUTIONS = {'001': 233168,
             '002': 4613732,
             '003': 6857,
             '004': 906609,
             '005': 232792560,
             '006': 25164150,
             '007': 104743,
             '008': 23514624000,
             '009': 31875000,
             '010': 142913828922,
             '011': 70600674,
             '012': 76576500,
             '013': 5537376230,
             '014': 837799,
             '015': 137846528820,
             '016': 1366,
             '017': 21124,
             '018': 1074,
             '019': 171,
             '020': 648,
             '021': 31626,
             '022': 871198282,
             '023': 4179871,
             '024': 2783915460,
             '025': 4782,
             '026': 983,
             '027': -59231,
             '028': 669171001,
             '029': 9183,
             '030': 443839,
             '031': 73682,
             '032': 45228,
             '033': 100,
             '034': 40730,
             '035': 55,
             '036': 872187,
             '037': 748317,
             '038': 932718654,
             '039': 840,
             '040': 210,
             '041': 7652413,
             '042': 162,
             '043': 16695334890,
             '044': 5482660,
             '045': 1533776805,
             '046': 5777,
             '047': 134043,
             '048': 9110846700,
             '049': 296962999629,
             '050': 997651,
             '052': 142857,
             '053': 4075,
             '054': 376,
             '055': 249,
             '056': 972,
             '057': 153,
             '058': 26241,
             '059': 107359,
             '060': 26033,
             '061': None,
             '062': 127035954683,
             '063': 49,
             '067': 7273,
             '068': 6531031914842725,
             '069': 510510,
             '071': 428570,
             '072': 303963552391,
             '073': 7295372,
             '074': 402,
             '075': 161667,
             '076': 190569291,
             '077': 71,
             '079': 73162890,
             '080': 40886,
             '081': 427337,
             '082': 260324,
             '083': 425185,
             '085': 2772,
             '087': 1097343,
             '089': 743,
             '090': 1217,
             '092': 8581146,
             '094': 518408346,
             '095': 14316,
             '096': 24702,
             '097': 8739992577,
             '099': 709,
             '102': 228,
             '107': 259679,
             '109': None,
             '112': 1587000,
             '113': 51161058134250,
             '114': 16475640049,
             '115': 168,
             '116': 20492570929,
             '117': 100808458960497,
             '118': 44680,
             '119': 248155780267521,
             '123': 21035,
             '124': 21417,
             '125': 2906969179,
             '139': 10057761,
             '162': '3D58725572C62302',
             '164': 378158756814587,
             '172': 227485267000992000,
             '173': 1572729,
             '174': 209566,
             '178': 126461847755,
             '179': 986262,
             '187': 17427258,
             '191': 1918080160,
             '205': 0.5731441,
             '206': 1389019170,
             '215': 806844323190414,
             '218': 0,
             '265': 209110240768,
             '347': 11109800204052,
             '493': 6.818741802}

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
