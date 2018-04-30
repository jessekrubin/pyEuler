# coding=utf-8

from os import path
from os import listdir
import importlib



def add_sol(p):


def check_answers():
    # with open("answers.txt") as f: answers = json.load(f)
    # print(answers)
    DONE_PATH = r'./done'
    DONE = [f[6:9] for f in listdir(DONE_PATH)
            if path.isfile(path.join(DONE_PATH, f))
            and f.startswith('euler_') and f.endswith('.py')]
    # DONE =['001', '002']
    print("Checking {} problems.".format(len(DONE)))

    for problem in DONE:
        p_file = importlib.import_module("done.euler_{}".format(problem))

        try:
            my_ans = getattr(p_file, 'p{}'.format(problem))
        except AttributeError as e:
            print("{} has no pXXX() method")

        try:
            p_ans = p_file.__sol__
        except AttributeError as e:
            print("{} has no __sol__ variable".format(problem))

        try:
            # p_ans = answers[problem]
            assert p_ans == my_ans()
            print("{} PASSED".format(problem))
        except AssertionError as e:
            print("{} FAILED".format(problem))
            print(e.message)
        except IOError as e:
            print("IO ERROR: prolly a text file")



check_answers()

