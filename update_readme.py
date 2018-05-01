# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - update README.md
"""
Python script to update the README.md for this repo
"""

import datetime
from os import path
from os import listdir

DONE_PATH = r'./done'
NOT_DONE_PATH = r'./not_done'
NO_CIGAR_PATH = r'./no_cigar'
LAST_UPDATED = datetime.datetime.now().strftime("%Y-%m-%d")
DONE = [int(f[6:9]) for f in listdir(DONE_PATH)
        if path.isfile(path.join(DONE_PATH, f))
        and f.startswith('euler_')
        and f.endswith('.py')]
DONE.sort()
EULER_IMG_URL = r'https://projecteuler.net/profile/rubinj.png'
NO_CIGAR = [int(f[6:9]) for f in listdir(NO_CIGAR_PATH)
            if path.isfile(path.join(NO_CIGAR_PATH, f))
            and f.startswith('euler_')]
NO_CIGAR.sort()
NOT_DONE = [
    int(str(f[6:9])) for f in listdir(NOT_DONE_PATH)
    if path.isfile(path.join(NOT_DONE_PATH, f)) and f.startswith("euler")
    ]
NOT_DONE.sort()
DONE_LIST_STR = ("DONE: {}".format(DONE))
NOT_DONE_LIST_STR = ("IN PROGRESS: {}".format(NOT_DONE))
N_EULER_PROBS = 615 + 1
DONE_EMOJI = ":snake:"
INPROG_EMOJI = ":scream:"
NO_CIGAR_EMOJI = ":no_smoking:"
NOT_STARTED_EMOJI = ":see_no_evil:"
NUM_COLUMNS = 8
README_TEXT = """# pEuler

This is my primarily python project euler problems repository.
I do these problems for fun, and because if I don't do them...then who will?
Recently I have started to do some of the problems in bash. 
Functions I regularly use are kept in the lib package file at the root of this repo;
Feel free to check it out and leave either constructive or dispariging criticism (no neutral criticism please). 
The folder named 'no_cigar' has my solutions that take longer than a minute to run; 
if you were to give feedback, this is where it would be most helpful.


![alt text]({})

Last I checked ({}) i've done {} problems, and am currently working on {}.

## Problems table

###### KEY:
 
{} = done

{} = close, but no cigar; takes more than 1 min

{} = in progress

{} = n/a; not started

""".format(EULER_IMG_URL,
           LAST_UPDATED,
           len(DONE),
           len(NOT_DONE),
           DONE_EMOJI,
           NO_CIGAR_EMOJI,
           INPROG_EMOJI,
           NOT_STARTED_EMOJI)


def make_table_line(row):
    linelist = []
    for n in row:
        status = NOT_STARTED_EMOJI
        if n in DONE:
            status = DONE_EMOJI
            n_string = "[{}](done/euler_{}.py)".format(str(n), str(n).zfill(3))
        else:
            n_string = str(n)
            if n in NO_CIGAR:
                status = NO_CIGAR_EMOJI
            if n in NOT_DONE:
                status = INPROG_EMOJI
        linelist.append("|{} ~ {}".format(n_string, status))
    linelist.append('|\n')
    return "".join(linelist)


def sur_la_table():
    probs = [i for i in range(1, N_EULER_PROBS)]
    rows = [
        probs[i:i + NUM_COLUMNS] for i in range(0, N_EULER_PROBS, NUM_COLUMNS)
        ]
    table_lines = [make_table_line(row) for row in rows
                   if any(prob_num in DONE + NO_CIGAR for prob_num in row) in DONE]
    return table_lines


def write_README():
    with open('README.md', 'w') as f:
        f.write(README_TEXT)

        table_header = "| Problem # |" + " # |" * (
                NUM_COLUMNS - 1) + "\n"
        f.write(table_header)
        header_sep = "|" + " ---: |" * NUM_COLUMNS + "\n"
        f.write(header_sep)
        f.writelines(sur_la_table())


if __name__ == '__main__':
    write_README()
    print("______________________")
    print("# problems done: {}".format(len(DONE) + len(NO_CIGAR)))
    print("______________________")
    print("# cigars: {}".format(len(DONE)))
    print("______________________")
    print("# not-cigars: {}".format(len(NO_CIGAR)))
    print("______________________")
    print("# problems !done: {}".format(len(NOT_DONE)))
    print("______________________")
    print("Dear Jesse,\n"
          "you have updated this repo's README.md.\n"
          "So proud of you,\n"
          "Yourself,\n"
          "Jesse")
