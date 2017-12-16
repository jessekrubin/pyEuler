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

print("DONE: {}".format(DONE))
print("NOT_DONE: {}".format(NOT_DONE))

N_EULER_PROBS = 615
rm_text = """# pEuler

AHA, you have found my project Euler repo. 
Last I heard ({}) i've done {} problems, and am currently working on {}. 

## Problems table

""".format(LAST_UPDATED, len(DONE), len(NOT_DONE))

with open('README.md', 'w') as f:
    f.write(rm_text)
    f.write("| Problem # | Solved?  |\n")
    f.write("| --------- | -------- |\n")
    for i in range(1, N_EULER_PROBS):
        status = "???     "
        if i in DONE:
            status = "DONE    "
        elif i in NOT_DONE:
            status = "in prog "

        this_line = "| {}       | {} |\n".format(str(i).zfill(3), status)
        f.write(this_line)

f.close()
