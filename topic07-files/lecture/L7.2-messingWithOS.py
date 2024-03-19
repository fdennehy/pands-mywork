# messing with the os module
# Author: Finbar Dennehy

import os

#FILENAME = "L7.1-messingWithFiles.py"

#navigate to files
FILENAME = "..\topic06-functions\lab\lab6.1-quiz.py"

if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        for line in f:
            print(line, end="")
else:
    print(FILENAME, "does not exist")


'''
#remove a file
os.remove("data2.txt")
'''

#navigate to files
FILENAME = "..\..topic06-functions\lab\lab6.1-quiz.py"