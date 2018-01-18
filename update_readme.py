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
NOT_DONE = [
    int(str(f[6:9])) for f in listdir(NOT_DONE_PATH)
    if isfile(join(NOT_DONE_PATH, f)) and f.startswith("euler")
]
NOT_DONE.sort()
DONE_LIST_STR = ("DONE: {}".format(DONE))
NOT_DONE_LIST_STR = ("IN PROGRESS: {}".format(NOT_DONE))
N_EULER_PROBLEMS = 615 + 1
DONE_EMOJI = ":metal:"
IN_PROGRESS_EMOJI = ":scream:"
NOT_STARTED_EMOJI = ":see_no_evil:"
N_COLUMNS = 6

README_TEXT = """# pEuler

This is my primarily python project euler problems repository.
I do these problems for fun, and because if I don't do them...then who will?
Functions I regularly use are kept in the 'helpme.py' file at the root of this repo;
Feel free to check it out and leave either constructive or dispariging criticism (no neutral criticism please).
Last I checked ({}) i've done {} problems, and am currently working on {}.

## Problems table

##### KEY: 
##### {} = done; 
##### {} = in progress; 
##### {} = haven't seen it (thus the monkey)

""".format(LAST_UPDATED, len(DONE), len(NOT_DONE), DONE_EMOJI,
           IN_PROGRESS_EMOJI, NOT_STARTED_EMOJI)

with open('README.md', 'w') as f:
    f.write(README_TEXT)
    table_header = "| Problem # | Done? |" + " # | Done? |" * (
            N_COLUMNS - 1) + "\n"
    f.write(table_header)
    header_sep = "|" + " ---:|:--- |" * N_COLUMNS + "\n"
    f.write(header_sep)
    euler_prob_nums = [i for i in range(1, N_EULER_PROBLEMS)]
    l_chunks = [
        euler_prob_nums[i:i + N_COLUMNS] for i in range(0, N_EULER_PROBLEMS, N_COLUMNS)
    ]
    for chunk in l_chunks:
        line = ""
        for n in chunk:
            status = NOT_STARTED_EMOJI
            if n in DONE:
                status = DONE_EMOJI
            if n in NOT_DONE:
                status = IN_PROGRESS_EMOJI

            line += "| {} | {} ".format(str(n), status)
        line += "|\n"
        f.write(line)

f.close()

#####################
### MESSAGE TO ME ###
#####################
DONE_CHUNKS = [DONE[i:i + 20] for i in range(0, len(DONE), 20)]
NOT_DONE_CHUNKS = [NOT_DONE[i:i + 20] for i in range(0, len(NOT_DONE), 20)]
print("")
print("Jesse, you have done {} problems; they are:".format(len(DONE)))
for chunk in DONE_CHUNKS:
    print(chunk)
print("")
print("You, Jesse, have started but not finished {} problems; those are:".format(len(NOT_DONE)))
for chunk in NOT_DONE_CHUNKS:
    print(chunk)
print("")
print("Dear Jesse,\n"
      "you updated the readme! So proud of you!\n"
      "Yourself,\n"
      "Jesse")
