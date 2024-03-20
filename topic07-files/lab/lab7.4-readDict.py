# readDict.py
# Function that will read in a dict object from file
# Author: Finbar Dennehy

import json
FILENAME ="testdict.json"

def readDict():
 # this will throw an error if the file does not exist
 # it should really just return an empty dict 
 # we can do this later
 with open(FILENAME) as f:
   return json.load(f)

# test the function
somedict = readDict()
print(somedict)