# coding=utf-8

from os import path
from os import listdir
from time import time
import importlib
import json
with open('../txt_files/solutions.txt') as f:
    thing = json.load(f)

# print(thing)


def add_sol(p, ans = None):
    with open("euler_{}.py".format(p)) as f:
        lines = [l.strip('\n') for l in  f.readlines()]
    sol_ind = [i for i in range(len(lines)) if lines[i] == '"""']
    if ans is None:
        lines.insert(sol_ind[1]+1, "__sol__ = None")
    else:
        lines.insert(sol_ind[1]+1, "__sol__ = {}".format(ans))
    with open("euler_{}.py".format(p), 'wb') as f:
        f.writelines("\n".join(lines))

def set_sol(p, ans):
    with open("./done/euler_{}.py".format(p)) as f:
        lines = [l.strip('\n') for l in  f.readlines()]
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
    try:
        p_file = importlib.import_module("done.euler_{}".format(problem))
    except IOError:
        print("IO ERROR: prolly a text file")

    try:
        p_funk = getattr(p_file, 'p{}'.format(problem))
    except AttributeError as e:
        print("{} has no pXXX() method")
        add_pxxx(problem)

    try:
        p_ans = p_file.__sol__
    except AttributeError as e:
        print("{} has no __sol__ variable".format(problem))
        add_sol(problem)

    try:
        if p_ans is None:
            if problem in thing:
                set_sol(problem, thing[problem])
            raise ValueError()
        # p_ans = answers[problem]
        ts = time()
        my_ans = p_funk()
        te = time()
        assert p_ans == my_ans
        t_total = (te-ts)*1000
        print("p{} PASSED; {} ms".format(problem, t_total))
    except AssertionError as e: # failed test
        print("p{} FAILED".format(problem))
        print(p_funk(), p_ans)
    except ValueError as e:
        print("p{} __sol__ is None".format(problem))

def check_all_answers():
    DONE_PATH = r'.'
    DONE = [f[6:9] for f in listdir(DONE_PATH)
            if path.isfile(path.join(DONE_PATH, f))
            and f.startswith('euler_') and f.endswith('.py')]
    print("Checking {} problems.".format(len(DONE)))

    # for problem in DONE:
    #     check_answer(problem)
    map(check_answer, DONE)

    print("ALL PASSED")


check_all_answers()

