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
NOT_STARTED_EMOJI = ":wavy_dash:"
N_COLUMNS = 6

README_TEXT = """# pEuler

This is my primarily python project euler problems repository.
I do these problems for fun. 
Last I checked ({}) i've done {} problems, and am currently working on {}.

## Problems table

###### {} = done

###### {} = in progress

###### {} = n/a; not started

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

print("DONE: {}".format(len(DONE)))
print("NOT DONE: {}".format(len(NOT_DONE)))
print(DONE)
print(NOT_DONE)
print("\nDear Jesse,\n"
      "you updated the readme! So proud of you!\n"
      "Yourself,\n"
      "Jesse")
