# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - update README.md

from os import listdir
from os.path import isfile, join

done_path = r'./done'

done = [int(f[6:9]) for f in listdir(done_path) if isfile(join(done_path, f))]
not_done = [
    int(f[6:9]) for f in listdir('.')
    if isfile(join('.', f)) and f.startswith("euler")
]

print(done)
print(not_done)

numEulerProbs = 600
rm_text = """#pEuler

AHA, you have found my project Euler repo. 
The file I keep lost of helper functions in is called 'helpme.py.'

##Problems table

"""

with open('README.md', 'w') as f:
    f.write(rm_text)
    f.write("| Problem # | Solved?  |\n")
    f.write("| --------- | -------- |\n")
    for i in range(1, numEulerProbs):
        status = "???     "
        if i in done:
            status = "DONE    "
        elif i in not_done:
            status = "in prog "

        this_line = "| {}       | {} |\n".format(str(i).zfill(3), status)
        f.write(this_line)

f.close()