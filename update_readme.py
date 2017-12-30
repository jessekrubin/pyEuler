# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - update README.md

import datetime
from os import listdir
from os.path import isfile, join

DONE_PATH = r'./done'
NOT_DONE_PATH = r'./not_done'
LAST_UPDATED = datetime.datetime.now().strftime("%Y-%m-%d")
DONE = [int(f[6:9]) for f in listdir(DONE_PATH) if isfile(join(DONE_PATH, f))]
NOT_DONE = [
    int(str(f[6:9])) for f in listdir(NOT_DONE_PATH)
    if isfile(join(NOT_DONE_PATH, f)) and f.startswith("euler")
]
DONE.sort()
NOT_DONE.sort()

DONE_LIST_STR = ("DONE: {}".format(DONE))
NOT_DONE_LIST_STR = ("NOT_DONE: {}".format(NOT_DONE))

N_EULER_PROBS = 615 + 1
rm_text = """# pEuler

AHA, you have found my project Euler repo. 
Last I heard ({}) i've done {} problems, and am currently working on {}. 

{}
{}

## Problems table

""".format(LAST_UPDATED, len(DONE), len(NOT_DONE), DONE_LIST_STR,
           NOT_DONE_LIST_STR)

print(rm_text)

with open('README.md', 'w') as f:
    f.write(rm_text)
    f.write(
        "| Problem # | :white_check_mark:? | p# | :white_check_mark:? | p# |:white_check_mark:? | p# |:white_check_mark:? |\n"
    )
    f.write("| ---:| --- | ---:| --- | ---:| --- | ---:| --- |\n")
    l = [i for i in range(1, N_EULER_PROBS)]
    l_chunks = [l[i:i + 4] for i in range(0, (N_EULER_PROBS), 4)]
    # print(l_chunks)
    for chunk in l_chunks:
        status = ":wavy_dash:"
        line = ""
        for n in chunk:
            if n in DONE:
                status = ":metal:"
            if n in NOT_DONE:
                status = ":scream:"

            line += "| {} | {} ".format(str(n).zfill(3), status)
        line += "|\n"
        # print(line)
        f.write(line)
    # for i in range(1, N_EULER_PROBS):
    #     status = "???"
    #     if i in DONE:
    #         status = "DONE"
    #     elif i in NOT_DONE:
    #         status = "in prog"

    #     this_line = "| {} | {} |\n".format(str(i).zfill(3), status)
    #     f.write(this_line)

f.close()
