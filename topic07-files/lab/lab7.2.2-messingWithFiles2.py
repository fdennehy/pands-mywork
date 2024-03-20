# init.py
# adds initialisation and try catch loop
# Author: Finbar Dennehy

# Write some code to check if the file exists. To do this we will need to import 
# os.path and use the isfile() function. You would need to look this up.

import os.path
FILENAME = "count.txt"
if not os.path.isfile(FILENAME):
    print ("File does not exist")
    #initialise file here

FILENAME = "count.txt"

# Use a try catch loop on the read (I think the best way). 
# We will be covering exception handling later in the course, so don’t worry 
# about this yet.

def readNumber():
    try:
        with open(FILENAME) as f:
            number = int(f.read())
            return number
    except IOError:
        # this file will be created when we write back.
        # no file assumes first time running 
        # ie 0 previous runs
        return 0
    

def writeNumber(number):
    with open(FILENAME, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number)) 

# main
num = readNumber()
num += 1
print ("we have run this program {} times".format(num))
writeNumber(num)