# coding=utf-8

from os import path
from os import listdir
import importlib



def add_sol(p):
    with open("./done/euler_{}.py".format(p)) as f:
        lines = [l.strip('\n') for l in  f.readlines()]
    sol_ind = [i for i in range(len(lines)) if lines[i] == '"""']
    lines.insert(sol_ind[1]+1, "__sol__ = None")
    with open("./done/euler_{}.py".format(p), 'wb') as f:
        f.writelines("\n".join(lines))

def add_pxxx(p):
    pxxx_lines = ['def p{}():'.format(p),
                  '    pass',
                  ''
                  'if __name__ == \'__main__\':'
                  '    p{}()'.format(p)
                  ]
    with open("./done/euler_{}.py".format(p), 'a') as f:
        f.write('\n'.join(pxxx_lines))
        # lines = f.readlines()
        # lines = [l.strip('\n') for l in  f.readlines()]
    # print(lines)
    #     f.write("def p{}():")

    # lines.insert(sol_ind[1]+1, "__sol__ = None")
    # with open("./done/euler_{}.py".format(p), 'wb') as f:
    #     f.writelines("\n".join(lines))

def check_answers():
    # with open("answers.txt") as f: answers = json.load(f)
    # print(answers)
    DONE_PATH = r'./done'
    # DONE = [f[6:9] for f in listdir(DONE_PATH)
    #         if path.isfile(path.join(DONE_PATH, f))
    #         and f.startswith('euler_') and f.endswith('.py')]
    DONE =['001', '002', '003', '004', '005', '006', '007', '008']
    print("Checking {} problems.".format(len(DONE)))

    for problem in DONE:
        p_file = importlib.import_module("done.euler_{}".format(problem))

        try:
            my_ans = getattr(p_file, 'p{}'.format(problem))
        except AttributeError as e:
            print("{} has no pXXX() method")
            add_pxxx(problem)

        try:
            p_ans = p_file.__sol__
        except AttributeError as e:
            print("{} has no __sol__ variable".format(problem))
            add_sol(problem)

        try:
            # p_ans = answers[problem]
            assert p_ans == my_ans()
            print("{} PASSED".format(problem))
        except AssertionError as e:
            print("{} FAILED".format(problem))
        except IOError as e:
            print("IO ERROR: prolly a text file")



check_answers()

