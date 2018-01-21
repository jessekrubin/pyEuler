# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - update README.md
# Python script to update the README.md for this repo

import datetime
from os import listdir
from os.path import isfile, join

DONE_PATH = r'./done'
NOT_DONE_PATH = r'./not_done'
LAST_UPDATED = datetime.datetime.now().strftime("%Y-%m-%d")
DONE = [int(f[6:9]) for f in listdir(DONE_PATH) if isfile(join(DONE_PATH, f))]
DONE.sort()
NOT_DONE = [
    int(str(f[6:9])) for f in listdir(NOT_DONE_PATH)
    if isfile(join(NOT_DONE_PATH, f)) and f.startswith("euler")
]
NOT_DONE.sort()
DONE_LIST_STR = ("DONE: {}".format(DONE))
NOT_DONE_LIST_STR = ("IN PROGRESS: {}".format(NOT_DONE))
N_EULER_PROBS = 615 + 1
DONE_EMOJI = ":snake:"
INPROG_EMOJI = ":scream:"
NOT_STARTED_EMOJI = ":see_no_evil:"
rm_text = """# pEuler
This is my primarily python project euler problems repository.
I do these problems for fun, and because if I don't do them...then who will?
Functions I regularly use are kept in the 'helpme.py' file at the root of this repo;
Feel free to check it out and leave either constructive or dispariging criticism (no neutral criticism please).
Last I checked ({}) i've done {} problems, and am currently working on {}.

## Problems table

###### KEY: {} = done; {} = in progress; {} = n/a; not started

""".format(LAST_UPDATED, len(DONE), len(NOT_DONE), DONE_EMOJI,
           INPROG_EMOJI, NOT_STARTED_EMOJI)

print(rm_text)

NUM_COLUMNS = 6

with open('README.md', 'w') as f:
    f.write(rm_text)
    table_header = "| Problem # | Done? |" + " # | Done? |" * (
        NUM_COLUMNS - 1) + "\n"
    f.write(table_header)
    header_sep = "|" + " ---:|:--- |" * NUM_COLUMNS + "\n"
    f.write(header_sep)
    l = [i for i in range(1, N_EULER_PROBS)]
    l_chunks = [
        l[i:i + NUM_COLUMNS] for i in range(0, (N_EULER_PROBS), NUM_COLUMNS)
    ]
    for chunk in l_chunks:
        line = ""
        for n in chunk:
            status = NOT_STARTED_EMOJI
            if n in DONE:
                status = DONE_EMOJI
            if n in NOT_DONE:
                status = INPROG_EMOJI

            line += "| {} | {} ".format(str(n), status)
        line += "|\n"
        f.write(line)

f.close()

print("##################")
print("# readme updated #")
print("##################")
