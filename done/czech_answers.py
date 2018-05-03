# coding=utf-8
from __future__ import with_statement
from os import listdir, getcwd
from time import time, sleep
from importlib import import_module
from tqdm import tqdm
from multiprocessing import Pool


def czech_answer(pn_str):
    p_file = import_module("done.euler_{}".format(pn_str))

    try: p_funk = getattr(p_file, 'p{}'.format(pn_str))
    except AttributeError: return 'NO_PFUNK'
    try: p_ans = p_file.__sol__
    except AttributeError: return 'NO_SOL'
    if p_ans is None: return 'SOL_IS_NONE'
    ts = time()
    my_ans = p_funk()
    te = (time() - ts)*1000
    try: assert p_ans == my_ans
    except AssertionError: return 'FAIL'
    return round(te)


if __name__ == '__main__':
    DONE = [f[6:9] for f in listdir(getcwd())  # find all files in the done dir
            if f.startswith('euler_')  # for which the file start with 'euler_'
            and f.endswith('.py')]  # and ends with '.py'

    p = Pool(processes=16)
    t_results = {DONE[done_index]:res for done_index, res in
                 tqdm(enumerate(p.imap_unordered(czech_answer, DONE)),
                      total=len(DONE),
                      ascii=True,
                      leave=True)}
    p.close()
    p.join()

    PASSED = [pn for pn in t_results if type(t_results[pn]) is not str]
    print("{} PASSED".format(len(PASSED)))


    FAILED = [pn for pn in t_results if t_results[pn] == 'FAIL']
    if len(FAILED)>0:
        print("__FAILS__")
        FAILED
    NO_SOL = [pn for pn in t_results if t_results[pn] == 'NO_SOL']
    if len(NO_SOL)>0:
        print("__NO_SOL__")
        print(NO_SOL)
    SOL_IS_NONE = [pn for pn in t_results if t_results[pn] == 'SOL_IS_NONE']
    if len(SOL_IS_NONE)>0:
        print("__SOL_IS_NONE__")
        print(SOL_IS_NONE)
    NO_PFUNK = [pn for pn in t_results if t_results[pn] == 'NO_PFUNK']
    if len(NO_PFUNK)>0:
        print("__NO_PFUNK__\n", NO_PFUNK)
        print(NO_PFUNK)
