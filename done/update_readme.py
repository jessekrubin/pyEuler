#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - update README.md
"""
Python script to update the README.md for this repo
"""

from datetime import datetime
from json import load, dump
from codecs import getwriter
from os import listdir

LAST_UPDATED = datetime.now().strftime("%Y-%m-%d")
EULER_IMG_URL = r'https://projecteuler.net/profile/rubinj.png'

DONE = sorted([int(f[6:9]) for f in listdir(r'./py')
               if f.startswith('euler_')
               and f.endswith('.py')])

DONE_DICT = {
    ### PYTHON
    "py" : [int(f[6:9]) for f in listdir('./py')
            if f.startswith('euler_') and f.endswith('.py')],
    ### CPP
    "cpp": [int(f[6:9]) for f in listdir('./cpp')
            if f.startswith('euler_') and f.endswith('.cpp')],
    ### JAVASCRIPT
    "js" : [int(f[6:9]) for f in listdir('./js')
            if f.startswith('euler_') and f.endswith('.js')],
    ### GO
    "go" : [int(f[6:9]) for f in listdir('./go')
            if f.startswith('euler_') and f.endswith('.go')],
    ### BASH
    "sh" : [int(f[6:9]) for f in listdir('./sh')
            if f.startswith('euler_') and f.endswith('.sh')]
    }

probs = {prob: set()
         for prob in
         set.union(*[set(n for n in v)
                     for v in DONE_DICT.values()])}

for language, probslist in DONE_DICT.items():
    for problem in probslist:
        probs[problem].add(language)

NO_CIGAR = sorted([int(f[6:9]) for f in listdir(r'../no_cigar')
                   if f.startswith('euler_') and f.endswith('.py')])

N_EULER_PROBS = 615 + 1
DONE_EMOJI = ":snake:"
INPROG_EMOJI = ":scream:"
NO_CIGAR_EMOJI = ":no_smoking:"
NOT_STARTED_EMOJI = ":see_no_evil:"
NUM_COLUMNS = 5
README_TEXT = f"""# p(y)Euler

This is my primarily python project euler problems repository.
Now with more languages and a very special someone (Ryan Saeta).
I do these problems for fun, and because if I don't do them...then who will?
Recently I have started to do some of the problems in bash. 
Check out my Pretty Useful Python package (pupy ~ `pip install pupy`);
Feel free to leave either constructive or dispariging criticism 
(no neutral criticism please). 
Solutions that are slow or brute-forcy are in the close, but "no_cigar" folder;
if you were to give feedback, this is where it would be most helpful.

![alt text]({EULER_IMG_URL})

Last I checked ({LAST_UPDATED}) i have done {(len(DONE)+len(NO_CIGAR))}.

"""

DONE_EMOJI = ":snake:"
PY_EMOJI = ":snake:"
CPP_EMOJI = ":ocean:"
JS_EMOJI = ":poop:"
SH_EMOJI = ":shell:"
GO_EMOJI = ":vertical_traffic_light:"
NO_CIGAR_EMOJI = ":no_smoking:"

EMOJI_DICTIONARY = {
    "py" : PY_EMOJI,
    "cpp": CPP_EMOJI,
    "js" : JS_EMOJI,
    "go" : GO_EMOJI,
    "sh" : SH_EMOJI
    }
TABLE_KEY = f"""## Problems table

###### KEY:
 
{PY_EMOJI} = python

{CPP_EMOJI} = cpp

{SH_EMOJI} = bash/shell

{JS_EMOJI} = bash

{GO_EMOJI} = go

{NO_CIGAR_EMOJI} = close, but no cigar; takes more than 1 min
"""

SOLUTIONS_PATH = "../txt_files/solutions.txt"


def update_solutions_txt(done):
    """

    Args:
        done:
    """
    # read in
    with open(SOLUTIONS_PATH, 'r') as f:
        solutions = load(f)
    # update
    solutions = {k: (solutions[k] if k in solutions else None)
                 for k in (str(k).zfill(3) for k in DONE)}
    # write out
    with open(SOLUTIONS_PATH, 'wb') as f:
        dump(solutions, getwriter('utf-8')(f), indent=4, sort_keys=True)

print(probs)
def table_problem(n):
    return "".join(EMOJI_DICTIONARY[p] for p in probs[int(n)])


def format_table_line(row):
    """format a line of the table
    """
    linelist = []
    for n in row:
        status = NOT_STARTED_EMOJI
        if n in DONE:
            status = table_problem(n)
            # n_string = "[{}](done/py/euler_{}.py)".format(str("p{}".format(n)), str(n).zfill(3))
        elif n in NO_CIGAR:
            status = NO_CIGAR_EMOJI
        linelist.append("|{}|{}".format(str(n).zfill(3), status))
    linelist.append('|\n')
    print(linelist)
    return "".join(linelist)


def sur_la_table():
    """
    """

    # probs = [i for i in range(1, N_EULER_PROBS)]
    all_probs = set.union(*[set(n for n in v)
                            for v in DONE_DICT.values()])
    # probs = sorted(list(set(NO_CIGAR + DONE)))
    probs = sorted(list(set(NO_CIGAR + DONE)))
    rows = [probs[i:i + NUM_COLUMNS]
            for i in range(0, N_EULER_PROBS, NUM_COLUMNS)]
    table_lines = [format_table_line(row) for row in rows
                   if any(prob_num in DONE + NO_CIGAR for prob_num in row)
                   in DONE]
    return table_lines


def write_README():
    with open('../README.md', 'w') as f:
        f.write(README_TEXT)

        # table_header = "| Problem # |" + " # |" * (NUM_COLUMNS - 1) + "\n"
        table_header = "| Problem # | # |" + " # | # |" * (NUM_COLUMNS - 1) + "\n"
        f.write(table_header)
        header_sep = "|" + " ---: | ---: |" * NUM_COLUMNS*2 + "\n"
        f.write(header_sep)
        f.writelines(sur_la_table())


# import os
# def done_dict():
# for a, b, c in os.walk(os.getcwd()):
#     print(a, b, c)

if __name__ == '__main__':
    update_solutions_txt(DONE)
    write_README()

    print("______________________")
    print("# problems done: {}".format(len(DONE) + len(NO_CIGAR)))
    print("______________________")
    print("# cigars: {}".format(len(DONE)))
    print("______________________")
    print("# not-cigars: {}".format(len(NO_CIGAR)))
    print("______________________")
    print("Dear Jesse,\n"
          "you have updated this repo's README.md.\n"
          "So proud of you,\n"
          "Yourself,\n"
          "Jesse")
