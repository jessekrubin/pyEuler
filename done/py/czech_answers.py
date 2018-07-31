# coding=utf-8
import json as jasm
from importlib import import_module
from multiprocessing import Pool
from os import listdir

from operator import itemgetter
from time import time
from tqdm import tqdm
from pupy.decorations import tictoc

with open('../txt_files/solutions.txt') as f:
    SOLUTIONS = jasm.load(f)

PASSED, NO_SOL, NO_PFUNK, FAILED, SOL_IS_NONE = [], [], [], [], []

# VERBOSE = True
VERBOSE = False


def czech_answer(pn_str):
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
    # p_file = import_module("py.euler_{}".format(pn_str))
    p_file = import_module('euler_{}'.format(pn_str))
    # p_file = import_module(path(getcwd(), "euler_{}".format(pn_str)))
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
    try:
        assert p_ans == my_ans
    except AssertionError:
        if VERBOSE:
            print(pn_str, 'FAIL')
        return pn_str, 'FAIL'
    if VERBOSE:
        print("PASS: {} ({} ms)".format(pn_str, round(te)))
    return pn_str, te


def parse_results(results):
    PASSED = [(problem_n, time) for problem_n, time in results.items() if type(time) is not str]
    print("{} PASSED".format(len(PASSED)))

    if len(PASSED) == len(DONE):
        print("ALL R A O K!!")
    else:
        print("{} TESTS PASS".format(len(PASSED)))
        FAILED = [problem_n for problem_n in results
                  if results[problem_n] == 'FAIL']
        if len(FAILED) > 0:
            print("__FAILS__")
            print(FAILED)
        NO_SOL = [problem_n for problem_n, res in results.items()
                  if res == 'NO_SOL']
        if len(NO_SOL) > 0:
            print("__NO_SOL__")
            print(NO_SOL)
        SOL_IS_NONE = [problem_n for problem_n, res in results.items() if res == 'SOL_IS_NONE']
        if len(SOL_IS_NONE) > 0:
            print("__SOL_IS_NONE__")
            print(SOL_IS_NONE)
        NO_PFUNK = [problem_n for problem_n, res in results.items() if res == 'NO_PFUNK']
        if len(NO_PFUNK) > 0:
            print("__NO_PFUNK__\n", NO_PFUNK)
            print(NO_PFUNK)

    PASSED.sort(key=itemgetter(1), reverse=True)
    print("SOLUTIONS SLOWEST TO FASTEST")
    print(PASSED)


from sys import stderr, stdout

if __name__ == '__main__':
    DONE = [f[6:9] for f in listdir('./py')  # find all files in the done dir
            if f.startswith('euler_')  # for which the file start with 'euler_'
            and f.endswith('.py')]  # and ends with '.py'

    if False:
        test_results = {}
        for problem_n, uh in map(czech_answer, DONE):
            stdout.write("\r{} {}\n{}".format(problem_n, uh, len(test_results) / len(DONE)))
            test_results[problem_n] = uh
    elif True:
        p = Pool(processes=2)
        results = {}
        for problem_n, test_result in p.imap_unordered(czech_answer, DONE):
            write_to = stdout
            if type(test_result) != float:
                write_to = stderr
            else:
                test_result = tictoc.ftime(test_result)
            percent_checked = str(round((len(results)/len(DONE))*100))
            write_to.write("\r{} {}\n [[{}%]]".format(problem_n, test_result, percent_checked))
            results[problem_n] = test_result


        p.close()  ## close pool
        p.join()  ## join pool
        parse_results(results)
    else:
        p = Pool(processes=4)
        test_results = {problem_n: test_result
                        for problem_n, test_result in
                        tqdm(p.imap_unordered(czech_answer, DONE),
                             total=len(DONE),
                             desc="CHECKING SOLUTIONS",
                             ascii=True,
                             leave=True)}
        p.close()  ## close pool
        p.join()  ## join pool
        parse_results(test_results)
