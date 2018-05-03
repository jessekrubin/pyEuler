# coding=utf-8
from os import path, listdir, getcwd
from time import time
from importlib import import_module
import json

# with open('../txt_files/solutions.txt') as f:
#     thing = json.load(f)
# print(thing)


def add_sol(p, ans=None):
    with open("euler_{}.py".format(p)) as f:
        lines = [l.strip('\n') for l in f.readlines()]
    sol_ind = [i for i in range(len(lines)) if lines[i] == '"""']
    if ans is None:
        lines.insert(sol_ind[1]+1, "__sol__ = None")
    else:
        lines.insert(sol_ind[1]+1, "__sol__ = {}".format(ans))
    with open("euler_{}.py".format(p), 'wb') as f:
        f.writelines("\n".join(lines))


def set_sol(p, ans):
    with open("./done/euler_{}.py".format(p)) as f:
        lines = [l.strip('\n') for l in f.readlines()]
    sol_ind = [i for i in range(len(lines)) if lines[i] == '"""']
    lines[sol_ind[1]+1] = "__sol__ = {}".format(ans)
    with open("euler_{}.py".format(p), 'wb') as f:
        f.writelines("\n".join(lines))


def add_pxxx(p):
    pxxx_lines = ['def p{}():'.format(p),
                  '    pass',
                  '',
                  'if __name__ == \'__main__\':',
                  '    ANSWER = p{}()'.format(p),
                  '    print(\"Answer: {}\".format(ANSWER))']
    with open("euler_{}.py".format(p), 'a') as f:
        f.write('\n'.join(pxxx_lines))


def check_answer(problem):
    p_file = import_module("done.euler_{}".format(problem))

    try:
        p_funk = getattr(p_file, 'p{}'.format(problem))
    except AttributeError:
        print("{} has no pXXX() method")
        add_pxxx(problem)

    try:
        p_ans = p_file.__sol__
    except AttributeError:
        print("NO __sol__ VARIABLE FOUND FOR euler_{}.py".format(problem))

    try:
        if p_ans is None: raise ValueError()
        ts = time()
        my_ans = p_funk()
        te = time()
        assert p_ans == my_ans
        t_total = (te-ts)*1000
        print("p{} PASSED; {} ms".format(problem, t_total))
    except AssertionError as e:  # failed test
        print("p{} FAILED".format(problem))
        print(p_funk(), p_ans)
    except ValueError as e:
        print("p{} __sol__ is None".format(problem))


def check_all_answers():
    DONE_PATH = getcwd()
    DONE = [f[6:9] for f in listdir(DONE_PATH)
            if f.startswith('euler_') and f.endswith('.py')]
    print("{} PYTHON PROBLEM SOLUTIONS FOUND".format(len(DONE)))
    for p in DONE: check_answer(p)

    print("ALL PASSED")


check_all_answers()
