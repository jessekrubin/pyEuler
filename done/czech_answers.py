# coding=utf-8
from importlib import import_module
from multiprocessing import Pool
from operator import itemgetter
from os import getcwd, listdir
from time import time
from tqdm import tqdm
import json as jasm

with open('../txt_files/solutions.txt') as f:
    SOLUTIONS = jasm.load(f)

def czech_answer(pn_str):
    """Checks if the project euler solutions in this repo are correct

    Args:
        pn_str (str): problem number string (ex: '001')

    Returns:
        run time (float): if the test_fest passes
        failure message (str): if test_fest fails to pass
            'NO_PFUNK': the problem file doesn have a pXXX() method
            'NO_SOL': the problem has no __sol__ variable
            'SOL_IS_NONE': the __sol__ variable for the problem is None
    """
    p_file = import_module("done.euler_{}".format(pn_str))
    try: p_funk = getattr(p_file, 'p{}'.format(pn_str))
    except AttributeError: return 'NO_PFUNK'
    try: p_ans = SOLUTIONS[pn_str]
    except KeyError: return 'NO_SOL'
    if p_ans is None: return 'SOL_IS_NONE'
    ts = time()
    my_ans = p_funk()
    te = (time()-ts)*1000
    try: assert p_ans == my_ans
    except AssertionError: return 'FAIL'
    return round(te)


if __name__ == '__main__':
    DONE = [f[6:9] for f in listdir(getcwd())  # find all files in the done dir
            if f.startswith('euler_')  # for which the file start with 'euler_'
            and f.endswith('.py')]  # and ends with '.py'


    p = Pool(processes=8)
    t_results = {DONE[done_index]:res for done_index, res in
                 tqdm(enumerate(p.imap(czech_answer, DONE)),
                      total=len(DONE),
                      ascii=True,
                      leave=True)}
    p.close()
    p.join()

    PASSED = [(pn, time) for pn, time in t_results.items() if type(time) is not str]
    print("{} PASSED".format(len(PASSED)))

    if len(PASSED) == len(DONE):
        print("ALL R A O K!!")
    else:
        print("{} TESTS PASS".format(len(PASSED)))
        FAILED = [pn for pn, res in t_results.items() if res == 'FAIL']
        if len(FAILED) > 0:
            print("__FAILS__")
            print(FAILED)
        NO_SOL = [pn for pn, res in t_results.items() if res == 'NO_SOL']
        if len(NO_SOL) > 0:
            print("__NO_SOL__")
            print(NO_SOL)
        SOL_IS_NONE = [pn for pn, res in t_results.items() if res == 'SOL_IS_NONE']
        if len(SOL_IS_NONE) > 0:
            print("__SOL_IS_NONE__")
            print(SOL_IS_NONE)
        NO_PFUNK = [pn for pn, res in t_results.items() if res == 'NO_PFUNK']
        if len(NO_PFUNK) > 0:
            print("__NO_PFUNK__\n", NO_PFUNK)
            print(NO_PFUNK)

    PASSED.sort(key=itemgetter(1), reverse=True)
    print("SOLUTIONS SLOWEST TO FASTEST")
    print(PASSED)
